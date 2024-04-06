import scipy.io as sci
import scipy
import numpy as np
import matplotlib.pyplot as plt
from math import *

def time_handling(hours,minutes, seconds):
    sec = hours*3600 + minutes*60+seconds
    sec = sec-sec[0]
    return sec

fs = 100


file_path = "matrixka2l.mat"

mat = sci.loadmat(file_path)

matrix_name = list(mat.keys())[3]

acc_hours = mat[matrix_name][0]

acc_minutes = mat[matrix_name][1]
acc_seconds = mat[matrix_name][2]

sec = time_handling(acc_hours,acc_minutes, acc_seconds)

acc_x = mat[matrix_name][3]
acc_y = mat[matrix_name][4]
acc_z = mat[matrix_name][5]
acc = np.sqrt(np.square(acc_x-np.mean(acc_x))+np.square(acc_y-np.mean(acc_y))+np.square(acc_z-np.mean(acc_z)))
acc = list(acc)
N = len(acc)

fft_normalized = np.abs(np.fft.fft(acc-np.mean(acc)))
fft_normalized = fft_normalized/max(fft_normalized)
fft_normalized_one_nyquist = fft_normalized[0:ceil((N-1)/2)]

N = len(acc)

f = np.array(list(range(0,N-1)))*fs/N
f = f[0:ceil((N-1)/2)]

print(f/N)
print(f)


plt.plot(sec,acc)
plt.show()


