import matplotlib.pyplot as plt

ns = list(range(2, 11))
classical = [2 ** (n - 1) + 1 for n in ns]
quantum = [1 for _ in ns]

print(f"{'n':>3} | {'Classical':>10} | {'Quantum':>8}")
for n, c, q in zip(ns, classical, quantum):
    print(f"{n:>3} | {c:>10} | {q:>8}")

plt.plot(ns, classical, marker='s', label="Classical worst case: 2^(n-1)+1")
plt.plot(ns, quantum, marker='o', label="Deutsch-Jozsa: 1 query")
plt.yscale('log')
plt.xlabel("Number of input bits (n)")
plt.ylabel("Oracle queries (log scale)")
plt.title("Deutsch-Jozsa: Classical vs Quantum Queries")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.savefig("Output_T08_Realworld.png")
plt.show()