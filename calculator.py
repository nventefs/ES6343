import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math
import numpy as np

# The 1.2/50-8/20 generator effective impedance is 2ohm +/- 10%
# Typical 8/20 waveform equation is I(t) = A * I_pk * t^3 * exp(-t/tau)
# Where tau is 3.911 µs and A is 0.01243 (µs)^-3

L = 100 * (10**-9)
C = 235 * (10**-6)
R = 0.105

V_0 = 5000

alpha = R / (2 * L)
w_0 = 1 / math.sqrt(L*C)

print("Alpha (R/2L) = {}".format(alpha))
print("w_0 (1/sqrt(LC)) = {}".format(w_0))

gamma = (alpha**2 - w_0**2)**0.5
print("gamma = sqrt(alpha^2 - w_0^2) = {}".format(gamma))

s_1 = -alpha + gamma
s_2 = -alpha - gamma

#TODO: write in case for overdamped, underdamped, critically damped

A = (V_0 / L) / (s_1 - s_2)

print("A = {}".format(A))

t = []
i = []
for l in range(0,10000):
    t.append(l/(100 * (10**6)))

for k in t:
    i.append(A * (math.e ** (k * s_1) - math.e ** (k * s_2)))

t2 = []
for k in t:
    t2.append(k * 10**6)

plt.plot(t2,i)
plt.ylabel("Current (A)")
plt.xlabel("Time (µs)")
plt.show()

"""
C_1 = 235 * 10**-6    # 235 µF capacitor Maxwell 32634 Capacitor
L_1 = 100 * 10**-6      # 100nH from Maxwell 32634

# Front-time
# 8µs = 3.24 * t_front -> 8µs = 3.24 * (C_1 * R_1)

R_1 = (8 * 10**-6) / (3.24 * C_1)   # 10.5mOhm

alpha = R_1 / (2 * L_1)
beta = 1 / ((L_1 * C_1) ** 0.5)

k = R_1 / ((C_1 / L_1) **0.5)

print(k)

t = []
for l in range(0,1000):
    t.append(l/10**-6)

e = 2.71828 
i = []

"""

# Half-time
# The 50% decay time is 0.693 tau_half-value
# Given R_1 of 10.5mOhms -> tau_half-value = R_1 * C_1 -> (10.5 mOhms * 235 µF) = 2.7µs
# damping factor k = R/2 * sqrt ( C/L )
# k < 1
#print(0.693 * R_1 * C_1)


# Voltage waveform
# V_out = V_charge / (R_1 * C_1) * (exp(-t/tau_tail) - exp(-t/tau_front))