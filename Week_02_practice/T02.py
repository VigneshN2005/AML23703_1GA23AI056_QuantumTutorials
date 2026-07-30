import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

qc = QuantumCircuit(2)
qc.h(0)
qc.h(1)

sv = Statevector.from_instruction(qc)
print("Statevector:", sv.data)

probabilities = sv.probabilities()
print("Sum of probabilities:", np.sum(probabilities))
