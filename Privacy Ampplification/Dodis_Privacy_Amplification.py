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
    dodis = cryptomite.Dodis(n_1, m)
    # Perform Toeplitz extraction and return the output
    return dodis.extract(raw_key_bits, seed_bits)


n, m, error = 50, 50, 0.0001
input_bits = [randint(0, 1) for _ in range(n)]
seed_bits = [randint(0, 1) for _ in range(n)]
final = privacy_amplification(input_bits, seed_bits, n, m)

print("Input")
print(input_bits)
print("Seed")
print(seed_bits)
print("Output")
print(final)