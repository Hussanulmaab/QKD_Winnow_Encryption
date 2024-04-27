import random

def induce_errors(bits, error_rate):
    """Induce errors in the bit string based on error rate."""
    num_errors = int(len(bits) * error_rate)
    indices_to_flip = random.sample(range(len(bits)), num_errors)
    modified_bits = list(bits)
    for index in indices_to_flip:
        modified_bits[index] = '0' if modified_bits[index] == '1' else '1'
    return ''.join(modified_bits)

def main():
    try:
        error_rate_percentage = float(input("Enter the error rate percentage (between 0 and 100): "))
        if not 0 <= error_rate_percentage <= 100:
            print("Error rate percentage must be between 0 and 100.")
            return
        error_rate = error_rate_percentage / 100  # Convert percentage to decimal
        with open('Transmitter_Sifted.txt', 'r') as alice_file:
            alice_bits = alice_file.read().strip()
        bob_bits = induce_errors(alice_bits, error_rate)
        with open('Receiver_Sifted.txt', 'w') as bob_file:
            bob_file.write(bob_bits)
        print(f"File 'Receiver_Sifted.txt' created with induced errors based on {error_rate_percentage}% error rate.")
    except ValueError:
        print("Please enter a valid error rate.")

if __name__ == "__main__":
    main()
