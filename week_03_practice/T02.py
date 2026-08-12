from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

H=(1/np.sqrt(2))*np.array([[1,1],[1,-1]])
X=np.array([[0,1],[1,0]])
Y=np.array([[0,-1j],[1j,0]])
Z=np.array([[1,0],[0,-1]])

psi=np.array([1,0])

psi=H@psi
psi=X@psi
psi=Z@psi
psi=Y@psi
psi=H@psi

print("Analytical:")
print(psi)

qc=QuantumCircuit(1)
qc.h(0)
qc.x(0)
qc.z(0)
qc.y(0)
qc.h(0)

sim=Statevector.from_instruction(qc)

print("\nSimulation:")
print(sim.data)

print("\nMatch:",np.allclose(psi,sim.data))