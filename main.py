import pandas as pd
from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('ecg.csv')

def get_random_ecg_plot(row_num):

    row_with_last_element = df.iloc[row_num]
    row = row_with_last_element.iloc[:-1]
    row_values = [(float(element)) for element in row]
    print(row_values)
    time = list(range(len(row_values)))
    return time,row_values



def get_the_plot_you_want(row_num):
    print(row_num)
    row_with_last_element = df.iloc[row_num-2]
    row = row_with_last_element.iloc[:-1]
    row_values = [(float(element)) for element in row]
    print(row_values)

    time = list(range(len(row_values)))
    plt.plot(time, row_values)
    plt.show()

def get_fft_values(row_num):
    row_with_last_element = df.iloc[row_num - 2]
    row = row_with_last_element.iloc[:-1]
    row_values = [(float(element)) for element in row]
    fft_values = fft(row_values)
    return fft_values

def get_fft_frequencies(row_num):
    row_with_last_element = df.iloc[row_num - 2]
    row = row_with_last_element.iloc[:-1]
    row_values = [(float(element)) for element in row]
    time = list(range(len(row_values)))
    fft_freq = fftfreq(len(time), d = (time[1] - time[0]))
    return fft_freq

def normal_abnormal(row_num):
    last_element = df.iloc[row_num-2, -1]

    if last_element == 0:
        return str("abnormal " + str(row_num))
    elif last_element == 1:
        return str("normal " + str(row_num))

row_num = np.random.randint(0, 4998)

fig, (ax1,ax2) = plt.subplots(2)

print(row_num)
x1,y1 = get_random_ecg_plot(row_num)
ax1.plot(x1,y1 )
ax1.set_xlabel('Time')
ax1.set_ylabel('ECG Signal')
ax1.set_title('Random ECG Plot')
x2 = np.abs(get_fft_frequencies(row_num))
y2 = np.abs(get_fft_values(row_num))
window_size = 2 # Adjust the window size to control the level of smoothing
ax2.plot(x2,y2)
ax2.set_xlabel('fft frequencies')
ax2.set_ylabel('fft amplitudes')
ax2.set_title(normal_abnormal(row_num))
print("x/FFT frequencies")
print(x2)
print("y/FFT amplitudes")
print(y2)

plt.show()
