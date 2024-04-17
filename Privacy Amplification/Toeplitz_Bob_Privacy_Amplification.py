#For Privacy Amplification, I am using Cryptomite Library of Quantinuum

import cryptomite
from random import randint

def privacy_amplification(raw_key_bits: list, seed_bits: list, n_1, m):
    """ Perform privacy amplification for the QKD protocol.
    Parameters
    ----------
    raw_key_bits : list of bits, derived from the measurement
    outcomes (after sifting, error correction and parameter
    estimation).
    seed_bits : list of bits, generated independently.
    n_1: integer, the length of the raw key bit string.
    m: integer, the length of the output secret key bit string.
    Returns
    ---------
    list of bits,
    the extracted output (i.e. the shared secret key).
    """
    # Initialise the Toeplitz extractor with the appropriate parameters:
    toeplitz = cryptomite.Toeplitz(n_1, m)
    # Perform Toeplitz extraction and return the output
    return toeplitz.extract(raw_key_bits, seed_bits)


with open("../Winnow Encryption Main Algorithm/Bob_Winnow-1_Final.txt", 'r') as Bob_data:
    Bob_Winnow_string = Bob_data.read()
    Bob_data.close()

# Convert every character into a list of strings
Bob_Winnow_List = [int(char) for char in Bob_Winnow_string]

# n, m, error = 50, 50, 0.0001
n = int(len(Bob_Winnow_string))
m = int(len(Bob_Winnow_string))
input_bits = [randint(0, 1) for _ in range(n)]
seed_bits = [randint(0, 1) for _ in range(n+m-1)]
final = privacy_amplification(Bob_Winnow_List, seed_bits, n, m)

print("Input")
print(input_bits)
print("Seed")
print(seed_bits)
print("Output")
print(final)

#  --------------------------------------------------------------------------------------
Bob_final = ''.join(str(bit) for bit in final)

# Specify the file path
file_path = 'Bob.txt'

# Open the file in write mode and write the binary string to it
with open(file_path, 'w') as file:
    file.write(Bob_final)

print("Binary string has been written to", file_path)