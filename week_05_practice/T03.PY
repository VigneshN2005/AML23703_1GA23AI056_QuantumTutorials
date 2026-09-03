from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np
import random

true_theta = random.uniform(0, np.pi)  # hidden from the "estimator"
shots = 4096
sim = AerSimulator()

# Z-basis measurement
qc_z = QuantumCircuit(1, 1)
qc_z.ry(true_theta, 0)
qc_z.measure(0, 0)
counts_z = sim.run(transpile(qc_z, sim), shots=shots).result().get_counts()
p1_z = counts_z.get('1', 0) / shots

# X-basis measurement
qc_x = QuantumCircuit(1, 1)
qc_x.ry(true_theta, 0)
qc_x.h(0)
qc_x.measure(0, 0)
counts_x = sim.run(transpile(qc_x, sim), shots=shots).result().get_counts()
p1_x = counts_x.get('1', 0) / shots

# Ry(theta)|0> = cos(theta/2)|0> + sin(theta/2)|1>  =>  P(1)_Z = sin^2(theta/2)
estimated_theta = 2 * np.arcsin(np.sqrt(p1_z))

print(f"True rotation angle (radians): {true_theta:.4f}")
print(f"Z-basis measurement counts:   {counts_z}")
print(f"X-basis measurement counts:   {counts_x}")
print(f"Estimated angle from Z-basis statistics: {estimated_theta:.4f}")
print(f"Estimation error: {abs(true_theta - estimated_theta):.4f}")