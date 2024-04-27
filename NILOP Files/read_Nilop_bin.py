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

# Alice read
file_name = './receiver_sift.bin'
binary_data = read_binary_file(file_name)

with open('../Algorithm Check/Making Erreneous Files/Transmitter_Sifted.txt', 'w') as Alice_Sifted:
    Alice_Sifted.write(binary_data)
    Alice_Sifted.close()

print(binary_data)

# Bob read
file_name = './transmitter_sift.bin'
binary_data = read_binary_file(file_name)
with open('../Algorithm Check/Making Erreneous Files/Receiver_Sifted.txt', 'w') as Bob_Sifted:
    Bob_Sifted.write(binary_data)
    Bob_Sifted.close()
