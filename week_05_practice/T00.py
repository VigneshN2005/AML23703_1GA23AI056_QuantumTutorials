from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def measure_superposition(shots):
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    sim = AerSimulator()
    job = sim.run(transpile(qc, sim), shots=shots)
    result = job.result()
    counts = result.get_counts()

    p1 = counts.get('1', 0) / shots
    return counts, p1

shot_list = [100, 1000, 10000]
print(f"{'Shots':>8} | {'Counts':>25} | {'P(1)':>8} | {'|P(1)-0.5|':>10}")
print("-" * 60)
for shots in shot_list:
    counts, p1 = measure_superposition(shots)
    print(f"{shots:>8} | {str(counts):>25} | {p1:>8.4f} | {abs(p1 - 0.5):>10.4f}")