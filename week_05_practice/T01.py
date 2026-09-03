from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def measure_x_basis(state, shots=1024):
    qc = QuantumCircuit(1, 1)
    if state == "+":
        qc.h(0)
    elif state == "-":
        qc.x(0)
        qc.h(0)

    qc.h(0)  # rotate to X-basis before measuring
    qc.measure(0, 0)

    sim = AerSimulator()
    job = sim.run(transpile(qc, sim), shots=shots)
    result = job.result()
    return result.get_counts()

for state in ["+", "-"]:
    counts = measure_x_basis(state)
    print(f"|{state}> state measured in X-basis: {counts}")