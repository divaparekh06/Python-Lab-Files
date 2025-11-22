# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import dlti

# def analyze_z_transfer_function(num, den):
#     # Digital Transfer Function (Z-domain)
#     system = dlti(num, den)

#     # Poles and zeros
#     zeros = system.zeros
#     poles = system.poles
#     print("Zeros:", zeros)
#     print("Poles:", poles)

#     # Stability check
#     stable = all(abs(p) < 1 for p in poles)
#     print("Stability:", "Stable" if stable else "Unstable")

#     # Causality check: proper system => degree(den) >= degree(num)
#     causal = len(den) >= len(num)
#     print("Causality:", "Causal" if causal else "Non-Causal")

#     print("Time Invariance: Time Invariant")

#     # ----- Bode-like Plot for Digital System -----
#     # Generate frequency response manually
#     w = np.linspace(0, np.pi, 1000)   # digital frequencies (0 to π)
#     z = np.exp(1j * w)                # e^(jw)
#     H = np.polyval(num, z) / np.polyval(den, z)

#     mag = 20 * np.log10(np.abs(H))
#     phase = np.angle(H, deg=True)

#     # ----- Plot -----
#     plt.figure(figsize=(10, 7))

#     plt.subplot(2, 1, 1)
#     plt.plot(w, mag)
#     plt.title("Magnitude Response")
#     plt.xlabel("Frequency (rad/sample)")
#     plt.ylabel("Magnitude (dB)")
#     plt.grid(True)

#     plt.subplot(2, 1, 2)
#     plt.plot(w, phase)
#     plt.title("Phase Response")
#     plt.xlabel("Frequency (rad/sample)")
#     plt.ylabel("Phase (degrees)")
#     plt.grid(True)

#     plt.tight_layout()
#     plt.show()


# # Example System
# num = [1, 0.5]
# den = [1, -1.5, 0.5]

# analyze_z_transfer_function(num, den)



#---------POST LABS-----------

#Question 1
# import numpy as np 
 
# # Unit step: 
# n = [2] 
# d = [1, -0.4] 
 
# poles = np.roots(d) 
# print("Poles =", poles) 

#Question 2
import numpy as np
n = [0.5, -0.8, 0.315] 
d = [1, -1.0, 0.24]   
 
poles = np.roots(d) 
 
print("Poles of the system = ", poles) 
 
stable = all(abs(p) < 1 for p in poles)
if stable: 
    print("Result: The system is STABLE") 
else: 
    print("Result: The system is UNSTABLE")


