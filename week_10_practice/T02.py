from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, pauli_error

def superdense(message):
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.barrier()
    if message[1] == '1':
        qc.x(0)
    if message[0] == '1':
        qc.z(0)
    qc.barrier()
    qc.id(0)                     # the transmission channel (noise attached here)
    qc.barrier()
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0, 1], [1, 0])
    return qc

messages = ["00", "01", "10", "11"]
shots = 2000
print(f"{'p(flip)':>7} | " + " ".join(f"{m:>6}" for m in messages) + " | Average")

for p in [0, 0.05, 0.1, 0.2, 0.3, 0.5]:
    nm = NoiseModel()
    nm.add_quantum_error(pauli_error([('X', p), ('I', 1 - p)]), ['id'], [0])
    sim = AerSimulator(noise_model=nm)
    accs = []
    for msg in messages:
        t = transpile(superdense(msg), sim, optimization_level=0)
        counts = sim.run(t, shots=shots).result().get_counts()
        accs.append(counts.get(msg, 0) / shots)
    print(f"{p:>7.2f} | " + " ".join(f"{a:>6.3f}" for a in accs) + f" | {sum(accs) / 4:.3f}")