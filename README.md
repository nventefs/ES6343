# ES6343
Resistors for impulse generation of 8/20µs waveform


# Front-time waveshaping
The impulse front-time can be controlled by the time constant of either a series R and shunt C circuit or a series L and shunt R circuit.
In terms of the circuit time constant **tau<sub>front<sub>**, the 10% to the 90% time is 2.2**tau<sub>front<sub>** and the 30% to 90% time is 1.95**tau<sub>front<sub>**.  Multiplying by the extrapolation factors of 1.25 and 1/0.6 gives:

- 10% to 90% based front-time = 2.75 **tau<sub>front<sub>**
- 30% to 90% based front-time = 3.24 **tau<sub>front<sub>**

