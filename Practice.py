import random

def generate_bits(num_bits):
    """Generate a string of 0s and 1s."""
    return ''.join(random.choice(['0', '1']) for _ in range(num_bits))

def main():
    try:
        num_bits = int(input("Enter the number of bits: "))
        if num_bits <= 0:
            print("Please enter a positive integer.")
            return
        bits = generate_bits(num_bits)
        with open('check.txt', 'w') as file:
            file.write(bits)
        print(f"File 'check.txt' created with {num_bits} random bits.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
