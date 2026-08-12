from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import numpy as np

qc=QuantumCircuit(1)
qc.h(0)
qc.z(0)

state=Statevector.from_instruction(qc)

expected=np.array([1/np.sqrt(2),-1/np.sqrt(2)])

print("Simulated:")
print(state)

print("\nExpected:")
print(expected)

print("\nMatch:",np.allclose(state.data,expected))