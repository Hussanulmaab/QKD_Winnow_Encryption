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

# Transmitter read
file_name = 'receiver_sift.bin'
binary_data = read_binary_file(file_name)

with open('../../Transmitter_Sifted.txt', 'w') as Transmitter_Sifted:
    Transmitter_Sifted.write(binary_data)
    Transmitter_Sifted.close()

print(binary_data)

# Receiver read
file_name = 'transmitter_sift.bin'
binary_data = read_binary_file(file_name)
with open('../../Receiver_Sifted.txt', 'w') as Receiver_Sifted:
    Receiver_Sifted.write(binary_data)
    Receiver_Sifted.close()
