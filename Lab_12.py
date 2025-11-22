# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal
# # Parameters
# fs = 500  # Sampling frequency
# f = 5  # Frequency of the signal
# t = np.linspace(0, 1, fs, endpoint=False)  # Time array
# # Create a sine wave signal
# sine_wave = np.sin(2 * np.pi * f * t)
# # Create a square wave signal using scipy
# square_wave = signal.square(2 * np.pi * f * t)
# # Plot the signals
# plt.figure(figsize=(10, 5))
# plt.subplot(2, 1, 1)
# plt.plot(t, sine_wave)
# plt.title('Sine Wave')
# plt.xlabel('Time [s]')
# plt.ylabel('Amplitude')
# plt.subplot(2, 1, 2)
# plt.plot(t, square_wave)
# plt.title('Square Wave')
# plt.xlabel('Time [s]')
# plt.ylabel('Amplitude')
# plt.tight_layout()
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal
# # Parameters
# fs = 500  # Sampling frequency
# f = 5  # Frequency of the signal
# t = np.linspace(0, 1, fs, endpoint=False)  # Time array
# # Create a triangular wave signal using scipy
# triangular_wave = signal.sawtooth(2 * np.pi * f * t, 0.5)
# # Create a ramp (sawtooth) signal using scipy
# ramp_signal = signal.sawtooth(2 * np.pi * f * t)
# # Plot the signals
# plt.figure(figsize=(10, 5))
# plt.subplot(2, 1, 1)
# plt.plot(t, triangular_wave)
# plt.title('Triangular Wave')
# plt.xlabel('Time [s]')
# plt.ylabel('Amplitude')
# plt.subplot(2, 1, 2)
# plt.plot(t, ramp_signal)
# plt.title('Ramp Signal')
# plt.xlabel('Time [s]')
# plt.ylabel('Amplitude')
# plt.tight_layout()
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal
# # Parameters
# fs = 500  # Sampling frequency
# t = np.linspace(-1, 1, fs, endpoint=False)  # Time array
# # 1. Unit Step Signal
# unit_step = np.heaviside(t, 1)
# # 2. Unit Impulse Signal (Dirac Delta)
# unit_impulse = np.zeros_like(t)
# unit_impulse[fs//2] = 1  # Impulse at t=0
# # 3. Ramp Signal
# ramp_signal = signal.sawtooth(2 * np.pi * t, 1)
# # 4. Sine Wave
# f_sine = 5  # Frequency of the sine wave
# sine_wave = np.sin(2 * np.pi * f_sine * t)
# # 5. Cosine Wave
# f_cosine = 5  # Frequency of the cosine wave
# cosine_wave = np.cos(2 * np.pi * f_cosine * t)
# # 6. Exponential Signal
# exponential_signal = np.exp(t)
# # 7. Triangular Wave
# triangular_wave = signal.sawtooth(2 * np.pi * 5 * t, 0.5)
# # 8. Square Wave
# square_wave = signal.square(2 * np.pi * 5 * t)
# # Plot the signals
# plt.figure(figsize=(12, 12))
# plt.subplot(4, 2, 1)
# plt.plot(t, unit_step)
# plt.title('Unit Step Signal')
# plt.xlabel('Time [s]')
# plt.ylabel('Amplitude')
# plt.subplot(4, 2, 2)
# plt.plot(t, unit_impulse)
# plt.title('Unit Impulse Signal')
# plt.xlabel('Time [s]')
# plt.ylabel('Amplitude')
# plt.subplot(4, 2, 3)
# plt.plot(t, ramp_signal)
# plt.title('Ramp Signal')
# plt.xlabel('Time [s]')
# plt.ylabel('Amplitude')
# plt.subplot(4, 2, 4)
# plt.plot(t, sine_wave)
# plt.title('Sine Wave')
# plt.xlabel('Time [s]')
# plt.ylabel('Amplitude')
# plt.subplot(4, 2, 5)
# plt.plot(t, cosine_wave)
# plt.title('Cosine Wave')
# plt.xlabel('Time [s]')
# plt.ylabel('Amplitude')
# plt.subplot(4, 2, 6)
# plt.plot(t, exponential_signal)
# plt.title('Exponential Signal')
# plt.xlabel('Time [s]')
# plt.ylabel('Amplitude')
# plt.subplot(4, 2, 7)
# plt.plot(t, triangular_wave)
# plt.title('Triangular Wave')
# plt.xlabel('Time [s]')
# plt.ylabel('Amplitude')
# plt.subplot(4, 2, 8)
# plt.plot(t, square_wave)
# plt.title('Square Wave')
# plt.xlabel('Time [s]')
# plt.ylabel('Amplitude')
# plt.tight_layout()
# plt.show()

# import numpy as np 
# import matplotlib.pyplot as plt 

# # Parameters 
# n = np.arange(0, 20)  # Discrete time array (0 to 19) 
# signal = np.sin(0.2 * np.pi * n)  # Example discrete-time signal (sine wave) 

# # Delay the signal by 3 samples
# delay = 3 
# delayed_signal = np.zeros_like(signal) 
# # Shift elements to the right, filling the first 'delay' spots with zeros
# delayed_signal[delay:] = signal[:-delay] 

# # Advance the signal by 3 samples 
# advance = 3 
# advanced_signal = np.zeros_like(signal) 
# # Shift elements to the left, filling the last 'advance' spots with zeros
# advanced_signal[:-advance] = signal[advance:] 

# # Plot the original and shifted signals 
# plt.figure(figsize=(12, 8)) 

# # Original Signal 
# plt.subplot(3, 1, 1) 
# # FIXED: Removed 'use_line_collection=True'
# plt.stem(n, signal) 
# plt.title('Original Signal: x[n]') 
# plt.xlabel('n (Discrete Time)') 
# plt.ylabel('Amplitude') 
# plt.grid(True, linestyle=':', alpha=0.6)

# # Delayed Signal 
# plt.subplot(3, 1, 2) 
# # FIXED: Removed 'use_line_collection=True'
# plt.stem(n, delayed_signal) 
# plt.title(f'Delayed Signal: x[n - {delay}]') 
# plt.xlabel('n (Discrete Time)') 
# plt.ylabel('Amplitude') 
# plt.grid(True, linestyle=':', alpha=0.6)

# # Advanced Signal 
# plt.subplot(3, 1, 3)
# # FIXED: Removed 'use_line_collection=True'
# plt.stem(n, advanced_signal) 
# plt.title(f'Advanced Signal: x[n + {advance}]') 
# plt.xlabel('n (Discrete Time)') 
# plt.ylabel('Amplitude') 
# plt.grid(True, linestyle=':', alpha=0.6)

# plt.tight_layout() 
# plt.show()


#--------POST LABS---------
#Question 1
# import numpy as np 
# import matplotlib.pyplot as plt 
# fs = 1000 
# t = np.linspace(0, 1, fs, endpoint=False) 
# sine1 = np.sin(2 * np.pi * 5 * t) 
# sine2 = np.sin(2 * np.pi * 10 * t) 
# add = sine1 + sine2 
# # Plot: 
# plt.figure(figsize=(10, 5)) 
# plt.plot(t, sine1, label="5 Hz Sine") 
# plt.plot(t, sine2, label="10 Hz Sine") 
# plt.plot(t, add, label="Added Signal", linewidth=2) 
# plt.legend() 
# plt.title("Addition of 5 Hz and 10 Hz Sine Waves") 
# plt.xlabel("Time [s]") 
# plt.ylabel("Amplitude") 
# plt.show() 


#Question 2
# import numpy as np 
# import matplotlib.pyplot as plt 
 
# fs = 500 
# t = np.linspace(0, 2, 2*fs, endpoint=False) 
 
# sine = np.sin(2 * np.pi * 5 * t) 
# cosine = np.cos(2 * np.pi * 10 * t) 
 
# product = sine * cosine 
 
# # Plot: 
# plt.figure(figsize=(10, 5)) 
# plt.plot(t, sine, label="5 Hz Sine") 
# plt.plot(t, cosine, label="10 Hz Cosine") 
# plt.plot(t, product, label="Product Signal", linewidth=2) 
# plt.legend() 
# plt.title("Multiplication of 5 Hz Sine and 10 Hz Cosine") 
# plt.xlabel("Time [s]") 
# plt.ylabel("Amplitude") 
# plt.show()

#Question 3
# import numpy as np 
# import matplotlib.pyplot as plt 
# fs = 500 
# t = np.linspace(0, 1, fs, endpoint=False) 
# sine = np.sin(2 * np.pi * 5 * t) 
# sine_shifted = np.sin(2 * np.pi * 5 * (t - 0.1))   # shift by 0.1 sec 
# # Plot: 
# plt.figure(figsize=(10, 5)) 
# plt.plot(t, sine, label="Original (5 Hz Sine)") 
# plt.plot(t, sine_shifted, label="Shifted by 0.1s") 
# plt.legend() 
# plt.title("Time-Shifted Sine Wave (5 Hz)") 
# plt.xlabel("Time [s]") 
# plt.ylabel("Amplitude") 
# plt.show()

#Question 4
# import numpy as np 
# import matplotlib.pyplot as plt 
 
# # Parameters
# fs = 500 
# t = np.linspace(0, 1, fs, endpoint=False) 
 
# sine = np.sin(2 * np.pi * 10 * t) 
# scaled = 3 * sine  
 
# # Plot: 
# plt.figure(figsize=(10, 5)) 
# plt.plot(t, sine, label="Original (10 Hz Sine)") 
# plt.plot(t, scaled, label="Scaled (×3)") 
# plt.legend() 
# plt.title("Amplitude Scaled Sine Wave (10 Hz)") 
# plt.xlabel("Time [s]") 
# plt.ylabel("Amplitude") 
# plt.show()

#Question 5 
import numpy as np 
import matplotlib.pyplot as plt 
 
fs = 500 
t = np.linspace(0, 1, fs, endpoint=False) 
 
sine= np.sin(2 * np.pi * 5 * t) 
reversed = sine[::-1]   
 
# Plot: 
plt.figure(figsize=(10, 5)) 
plt.plot(t, sine, label="Original (5 Hz Sine)") 
plt.plot(t, reversed, label="Reversed in Time") 
plt.legend() 
plt.title("Time-Reversed Sine Wave (5 Hz)") 
plt.xlabel("Time [s]") 
plt.ylabel("Amplitude") 
plt.show()


