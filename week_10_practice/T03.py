import matplotlib.pyplot as plt

messages = 100
bits_per_message = 2

classical_uses = messages * bits_per_message     # 1 classical bit per channel use
superdense_uses = messages                       # 1 qubit carries 2 bits
shared_pairs = messages                          # 1 pre-shared Bell pair per message

print(f"{'Method':>12} | {'Channel uses':>12} | {'Pre-shared Bell pairs':>21}")
print(f"{'Classical':>12} | {classical_uses:>12} | {0:>21}")
print(f"{'Superdense':>12} | {superdense_uses:>12} | {shared_pairs:>21}")

plt.bar(["Classical bits", "Superdense qubits"], [classical_uses, superdense_uses],
        color=["tab:orange", "tab:blue"])
plt.ylabel("Channel uses during transmission")
plt.title("100 Two-Bit Messages: Classical vs Superdense Coding")
plt.savefig("Output_T10_Realworld.png")
plt.show()