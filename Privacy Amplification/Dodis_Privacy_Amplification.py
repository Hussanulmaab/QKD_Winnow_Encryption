#For Privacy Amplification, I am using Cryptomite Library of Quantinuum

import cryptomite
from random import randint, sample

def privacy_amplification(raw_key_bits: list, seed_bits: list, n_1, m):
    dodis = cryptomite.Dodis(n_1, m)
    return dodis.extract(raw_key_bits, seed_bits)

def flip_random_bits(bits, flip_count):
    """Flip `flip_count` bits in the `bits` list."""
    indices = sample(range(len(bits)), flip_count)
    flipped_bits = bits[:]
    for i in indices:
        flipped_bits[i] = 1 - flipped_bits[i]
    return flipped_bits

# n, m, error = 2154816, 2154816, 0.0000

# files reading
with open('receiver_sifted.txt', 'r') as file:
    content = file.read().strip()

bit_list = list(content)
input_bits = [int(bit) for bit in bit_list]

n = m = len(content)
with open('transmitter_sifted.txt', 'r') as file:
    content = file.read().strip()

bit_list = list(content)
input_bits_2 = [int(bit) for bit in bit_list]

#printing
print("---Inputs----")
print("I1:", input_bits)
print("I2:", input_bits_2)
seed_bits = [randint(0, 1) for _ in range(n)]
print("S1:", seed_bits)

# performing PRNG
final = privacy_amplification(input_bits, seed_bits, n, m)
final_2 = privacy_amplification(input_bits_2, seed_bits, n, m)

#printing
print("---Outputs----")
print("O1:", final)
print("O2:", final_2)


#Calculate Error rate
def calculate_error_rate(final, final_2):
    errors = sum(1 for a, b in zip(final, final_2) if a != b)
    error_rate = (errors / len(final)) * 100
    return error_rate

error_rate = calculate_error_rate(final, final_2)
print(f"Error rate: {error_rate:.2f}%")

