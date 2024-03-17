import random

def induce_errors(bits, error_percentage):
    """Induce errors in the bits based on the error percentage."""
    num_errors = int(len(bits) * error_percentage / 100)
    error_indices = random.sample(range(len(bits)), num_errors)
    new_bits = list(bits)
    for index in error_indices:
        new_bits[index] = '0' if new_bits[index] == '1' else '1'
    return ''.join(new_bits)

def main():
    try:
        num_bits = int(input("Enter the number of bits: "))
        if num_bits <= 0:
            print("Please enter a positive integer.")
            return
        error_percentage = float(input("Enter the percentage of errors: "))
        if error_percentage < 0 or error_percentage > 100:
            print("Please enter a percentage between 0 and 100.")
            return
        with open('../check.txt', 'r') as file:
            bits = file.read().strip()
        error_bits = induce_errors(bits, error_percentage)
        with open('../checkError.txt', 'w') as error_file:
            error_file.write(error_bits)
        print(f"File 'checkError.txt' created with induced errors ({error_percentage}%).")
    except ValueError:
        print("Please enter valid inputs.")

if __name__ == "__main__":
    main()
