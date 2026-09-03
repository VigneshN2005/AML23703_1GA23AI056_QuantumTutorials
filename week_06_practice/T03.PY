from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

lengths = [2, 3, 4, 5, 6]
quantum_queries = [n - 1 for n in lengths]          # Simon's: ~n-1 queries suffice
classical_queries = [2 ** (n // 2) for n in lengths]  # brute-force worst case

print(f"{'n':>3} | {'Quantum':>10} | {'Classical':>10}")
for n, q, c in zip(lengths, quantum_queries, classical_queries):
    print(f"{n:>3} | {q:>10} | {c:>10}")

plt.plot(lengths, quantum_queries, marker='o', label="Simon's Algorithm")
plt.plot(lengths, classical_queries, marker='s', label="Classical brute force")
plt.yscale('log')
plt.xlabel("Secret string length (n)")
plt.ylabel("Oracle queries (log scale)")
plt.title("Simon's Algorithm vs Classical Brute Force")
plt.legend()
plt.savefig("Output_T06_Realworld.png")
plt.show()