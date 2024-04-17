import numpy as np

# Read data from Alice and Bob files
with open("../Winnow_Round_2/Alice_Winnow-2_Final.txt", "r") as alice_file:
    alice_data = np.array([int(bit) for bit in alice_file.read().strip()])

with open("../Winnow_Round_2/Bob_Winnow-2_Final.txt", "r") as bob_file:
    bob_data = np.array([int(bit) for bit in bob_file.read().strip()])

# Generate a permutation
permutation = np.random.permutation(len(alice_data))

# Apply permutation to Alice's data
alice_permuted = alice_data[permutation]

# Apply the same permutation to Bob's data
bob_permuted = bob_data[permutation]

# Save permuted data to new files
with open("Alice_Permuted_3.txt", "w") as alice_permuted_file:
    alice_permuted_file.write("".join(map(str, alice_permuted)))

with open("Bob_Permuted_3.txt", "w") as bob_permuted_file:
    bob_permuted_file.write("".join(map(str, bob_permuted)))

print("Files Alice_Permuted and Bob_Permuted saved successfully.")
