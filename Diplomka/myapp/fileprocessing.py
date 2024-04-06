import scipy.io as sci
import numpy as np
from math import *
def file_read(file):
    #TODO Vypocet fs
    fs= 100


    mat = sci.loadmat(file)
    #TODO: OSEKAT TO NEJAK
    matrix_name = list(mat.keys())[3]

    acc_hours = mat[matrix_name][0]
    acc_minutes = mat[matrix_name][1]
    acc_seconds = mat[matrix_name][2]
    time = time_handling(acc_hours, acc_minutes, acc_seconds)

    acc_x = mat[matrix_name][3]
    acc_y = mat[matrix_name][4]
    acc_z = mat[matrix_name][5]
    acc = np.sqrt(np.square(acc_x-np.mean(acc_x))+np.square(acc_y-np.mean(acc_y))+np.square(acc_z-np.mean(acc_z)))

    fft_normalized = np.abs(np.fft.fft(acc-np.mean(acc)))
    fft_normalized = fft_normalized/max(fft_normalized)
    fft_normalized_one_nyquist = fft_normalized[0:ceil(len(fft_normalized)/2)]

    N = len(acc)

    f = np.array(list(range(0,N-1)))*fs/N
    f = f[0:ceil(len(acc-1)/2)]




    acc = list(acc)
    time = list(time)
    fft_normalized_one_nyquist = list(fft_normalized_one_nyquist)
    f = list(f)

    return time, acc, fft_normalized_one_nyquist, f


def time_handling(hours,minutes, seconds):
    sec = hours*3600 + minutes*60+seconds
    sec = sec-sec[0]
    return sec



