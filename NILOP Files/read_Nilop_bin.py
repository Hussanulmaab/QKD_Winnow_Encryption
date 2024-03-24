import os

def read_binary_file(file_name):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Combine the directory with the file name
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, 'rb') as file:
        # Read the entire binary content
        binary_data = file.read()

        # Convert binary data to a sequence of 0s and 1s
        binary_string = ''.join(format(byte, '08b') for byte in binary_data)

        return binary_string

# Example usage:
file_name = 'transmitter_key.bin'
binary_data = read_binary_file(file_name)
print(binary_data)
