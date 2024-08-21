import numpy as np
import matplotlib.pyplot as plt
import math

# Constants
m0=4*math.pi*10**(-7)
e0=8.874*10**(-12)
c = 3e8  # Speed of light in m/s
f1 = 2e9  # Frequency of the first antenna in Hz
f2 = 2e9  # Frequency of the second antenna in Hz
f_new = f2-f1 

# Distance between antennas
distance = 124.185e-3 * 2  # Distance in meters

# Range of distances along the x-axis
x_range = np.linspace(-distance/2, distance/2, 300)  # Distance along the x-axis
# print(x_range)

# Initialize arrays to store electric field values
E_wave1_values = np.zeros_like(x_range, dtype=complex)
E_wave2_values = np.zeros_like(x_range, dtype=complex)
E_total_values = np.zeros_like(x_range, dtype=complex)

# Antenna parameters
E0 = np.sqrt(1000)  # Electric field amplitude (sqrt(1W) = sqrt(1000) = 31.62)

# Calculate phase difference
# phase_difference = - 2* np.pi * distance / wavelength_new
# print(x_range)
for i,x_val in enumerate(x_range):
    # print(i,x_val)
    if(x_val<=-86.685e-3):
        # print(i,x_val)
        a1=0
        b1=2*math.pi*f1*math.sqrt(m0*e0)
        E_wave1_values[i]=E0*np.exp(-1j*b1*x_val)
        Et1=np.abs(E_wave1_values[i])
    # else: continue
    elif(x_val>-86.685e-3 and x_val<=-77.685e-3):
        e=10
        a1=0
        b1=2*math.pi*f1*math.sqrt(m0*e0*e)
        E_wave1_values[i]=Et1*np.exp(-1j*b1*x_val)
        Et2=np.abs(E_wave1_values[i])
    elif(x_val>-77.685e-3 and x_val<=77.685e-3):
        e=34.988
        s=0.96
        a1=(s/2)*math.sqrt(m0/(e0*e))
        b1=2*math.pi*f1*math.sqrt(m0*e0*e)
        E_wave1_values[i]=Et2*np.exp(-a1*x_val)*np.exp(-1j*b1*x_val)
        Et3=np.abs(E_wave1_values[i])
    elif(x_val>77.685e-3 and x_val<=86.685e-3):
        e=10
        a1=0
        b1=2*math.pi*f1*math.sqrt(m0*e0*e)
        E_wave1_values[i]=Et3*np.exp(-1j*b1*x_val)
        Et4=np.abs(E_wave1_values[i])
    else:
        a1=0
        b1=2*math.pi*f1*math.sqrt(m0*e0)
        E_wave1_values[i]=Et4*np.exp(-1j*b1*x_val)


for i,x_val in enumerate(-x_range):
    print(i,x_val)
    if(x_val>86.685e-3):
        # print(i,x_val)
        a2=0
        b2=2*math.pi*f2*math.sqrt(m0*e0)
        E_wave2_values[i]=E0*np.exp(-1j*b2*x_val)
        Et1=np.abs(E_wave2_values[i])
    elif(x_val<=86.685e-3 and x_val>77.685e-3):
        e=10
        a2=0
        b2=2*math.pi*f2*math.sqrt(m0*e0*e)
        E_wave2_values[i]=Et1*np.exp(-1j*b2*x_val)
        Et2=np.abs(E_wave2_values[i])
    elif(x_val<=77.685e-3 and x_val>-77.685e-3):
        e=34.988
        s=0.96
        a2=(s/2)*math.sqrt(m0/(e0*e))
        b2=2*math.pi*f2*math.sqrt(m0*e0*e)
        E_wave2_values[i]=Et2*np.exp(-a2*x_val)*np.exp(-1j*b2*x_val)
        Et3=np.abs(E_wave2_values[i])
    elif(x_val<=-77.685e-3 and x_val>-86.685e-3):
        e=10
        a2=0
        b2=2*math.pi*f2*math.sqrt(m0*e0*e)
        E_wave2_values[i]=Et3*np.exp(-1j*b2*x_val)
        Et4=np.abs(E_wave2_values[i])
    else:
        a2=0
        b2=2*math.pi*f2*math.sqrt(m0*e0)
        E_wave2_values[i]=Et4*np.exp(-1j*b2*x_val)

for i in range(0,len(x_range),1):
    E_total_values[i] = E_wave1_values[i] + E_wave2_values[i]



# Plot the electric field of each wave and their superposition
plt.figure(figsize=(10, 6))
plt.plot(x_range * 1e3, E_wave1_values, 'b', label='Wave 1')
plt.plot(x_range * 1e3, E_wave2_values, 'r', label='Wave 2')
plt.plot(x_range * 1e3, E_total_values, 'g--', label='Superposition')
plt.title('Electric Field Along X-axis')
plt.xlabel('Distance (mm)')
plt.ylabel('Electric Field Strength')
plt.legend()
plt.grid(True)
plt.show()

# Print phase difference
# print("Phase Difference (degrees):", np.degrees(phase_difference))
