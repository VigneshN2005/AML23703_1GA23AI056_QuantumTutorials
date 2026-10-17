import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

def bell(name):
    qc = QuantumCircuit(2)
    if name in ("Psi+", "Psi-"):
        qc.x(1)
    qc.h(0)
    qc.cx(0, 1)
    if name in ("Phi-", "Psi-"):
        qc.z(0)
    return qc

sim = AerSimulator()
for name in ["Phi+", "Phi-", "Psi+", "Psi-"]:
    qc = bell(name)
    print(f"{name} statevector:", np.round(Statevector.from_instruction(qc).data, 3))
    qc.measure_all()
    counts = sim.run(transpile(qc, sim), shots=1024).result().get_counts()
    print(f"{name} counts:", counts, "\n")