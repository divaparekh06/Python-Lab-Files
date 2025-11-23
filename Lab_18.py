# import numpy as np
# # Define two input signals
# x = [1, 2, 3, 4]
# h = [1, 0, -1]
# # Perform linear convolution using numpy
# linear_conv = np.convolve(x, h)
# print("Linear Convolution: ", linear_conv) 

# import numpy as np

# # Define two input signals
# x = [1, 2, 3, 4]
# h = [1, 0, -1]
# # Determine the length for circular convolution
# N = max(len(x), len(h))
# # Zero-pad the shorter sequence to match the length of the longer one
# x_padded = np.pad(x, (0, N - len(x)), mode='constant')
# h_padded = np.pad(h, (0, N - len(h)), mode='constant')
# # Perform circular convolution using FFT
# X_fft = np.fft.fft(x_padded)
# H_fft = np.fft.fft(h_padded)
# circular_conv = np.fft.ifft(X_fft * H_fft)
# # Only the real part is considered (since the imaginary part should be zero)
# circular_conv = np.real(circular_conv)
# print("Circular Convolution: ", circular_conv)

# import numpy as np
# import matplotlib.pyplot as plt

# # Define two signals
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 3, 4, 5, 6])

# # Perform cross-correlation using numpy
# cross_corr = np.correlate(x, y, mode='full')

# # Plot cross-correlation
# plt.stem(cross_corr)
# plt.title('Cross-Correlation')
# plt.show()

# x = np.array([1, 2, 3, 4, 5])
# # Perform autocorrelation using numpy
# auto_corr = np.correlate(x, x, mode='full')
# # Plot autocorrelation
# plt.stem(auto_corr)
# plt.title('Autocorrelation')
# plt.show()

#---------------POST LABS----------------

#Question 1
# import matplotlib.pyplot as plt
# from scipy.io import wavfile
# import numpy as np

# # Read audio
# fs1, x = wavfile.read(r"C:\Users\Diva Parekh\Downloads\Bollywood Dance Music Song.wav")
# fs2, h = wavfile.read(r"C:\Users\Diva Parekh\Downloads\Bollywood Dance Music Song.wav")

# # Convert stereo → mono
# if x.ndim > 1:
#     x = x[:, 0]

# if h.ndim > 1:
#     h = h[:, 0]

# # Convert to float and trim
# x = x[:2000].astype(float)
# h = h[:500].astype(float)

# # Linear convolution
# y_linear = np.convolve(x, h)

# # Circular convolution
# N = len(x)
# M = len(h)
# L = max(N, M)

# x_padded = np.pad(x, (0, L - N))
# h_padded = np.pad(h, (0, L - M))
# y_circular = np.fft.ifft(np.fft.fft(x_padded) * np.fft.fft(h_padded)).real

# # Plot everything
# plt.figure(figsize=(10, 10))

# # Original audio
# plt.subplot(3, 1, 1)
# plt.plot(x)
# plt.title("My Audio Signal")

# # Linear convolution
# plt.subplot(3, 1, 2)
# plt.plot(y_linear)
# plt.title("Linear Convolution")

# # Circular convolution
# plt.subplot(3, 1, 3)
# plt.plot(y_circular)
# plt.title("Circular Convolution")

# plt.tight_layout()
# plt.show()

#Question 2
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Read audio files
fs1, clean = wavfile.read(r"C:\Users\Diva Parekh\Downloads\Bollywood Dance Music Song.wav")
fs2, noisy = wavfile.read(r"C:\Users\Diva Parekh\Downloads\Bollywood Dance Music Song.wav")
fs3, periodic = wavfile.read(r"C:\Users\Diva Parekh\Downloads\Bollywood Dance Music Song.wav")

# Convert stereo to mono
if clean.ndim > 1:
    clean = clean[:, 0]
if noisy.ndim > 1:
    noisy = noisy[:, 0]
if periodic.ndim > 1:
    periodic = periodic[:, 0]

# Select first 4000 samples as float
clean = clean[:4000].astype(float)
noisy = noisy[:4000].astype(float)
periodic = periodic[:4000].astype(float)


# Auto-correlation function

def autocorrelation(x):
    n = len(x)
    r = np.zeros(2*n - 1)
    for lag in range(-n + 1, n):
        for i in range(n):
            j = i + lag
            if 0 <= j < n:
                r[lag + n - 1] += x[i] * x[j]
    return r


# Cross-correlation function

def cross_correlation(x, y):
    n = len(x)
    m = len(y)
    r = np.zeros(n + m - 1)
    for lag in range(-m + 1, n):
        for i in range(n):
            j = i + lag
            if 0 <= j < m:
                r[lag + m - 1] += x[i] * y[j]
    return r

# Compute auto-correlation
acClean = autocorrelation(clean)
acNoisy = autocorrelation(noisy)
acPeriodic = autocorrelation(periodic)

# Compute cross-correlation
ccCleanNoisy = cross_correlation(clean, noisy)
ccCleanPeriodic = cross_correlation(clean, periodic)


# Normalization function

def normalize(x):
    x = x - np.mean(x)
    max_val = np.max(np.abs(x))
    return x / max_val if max_val != 0 else x

# Normalize results
acClean = normalize(acClean)
acNoisy = normalize(acNoisy)
acPeriodic = normalize(acPeriodic)
ccCleanNoisy = normalize(ccCleanNoisy)
ccCleanPeriodic = normalize(ccCleanPeriodic)


# Plotting

plt.figure(figsize=(12, 10))

plt.subplot(3, 2, 1)
plt.plot(acClean)
plt.title("Autocorrelation - Clean Audio")

plt.subplot(3, 2, 2)
plt.plot(acNoisy)
plt.title("Autocorrelation - Noisy Audio")

plt.subplot(3, 2, 3)
plt.plot(acPeriodic)
plt.title("Autocorrelation - Periodic Audio")

plt.subplot(3, 2, 4)
plt.plot(ccCleanNoisy)
plt.title("Cross-Correlation - Clean vs Noisy")

plt.subplot(3, 2, 5)
plt.plot(ccCleanPeriodic)
plt.title("Cross-Correlation - Clean vs Periodic")

plt.tight_layout()
plt.show()








