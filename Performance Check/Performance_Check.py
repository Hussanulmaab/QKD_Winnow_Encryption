import os
def count_directories(folder_path):
    # Initialize a counter for directories
    directory_count = 0

    # Iterate over all items in the folder
    for item in os.listdir(folder_path):
        # Check if the item is a directory
        if os.path.isdir(os.path.join(folder_path, item)):
            directory_count += 1

    return directory_count


# Specify the path to the folder you want to check
folder_path = '../Permutation_Winnow/'

# Get the count of directories in the folder
n = count_directories(folder_path) + 1

print("----------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------ROUND 1----------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------")


# with open("Transmitter_Sifted_File.txt", 'r') as Transmitter_Sifted_bits:
#     Transmitter_Bits = Transmitter_Sifted_bits.read()
#
# with open("Receiver_Sifted_File.txt", 'r') as Receiver_Sifted_bits:
#     Receiver_Bits = Receiver_Sifted_bits.read()

with open("Transmitter_Sifted.txt", 'r') as Transmitter_Sifted_bits:
    Transmitter_Bits = Transmitter_Sifted_bits.read()

with open("Receiver_Sifted.txt", 'r') as Receiver_Sifted_bits:
    Receiver_Bits = Receiver_Sifted_bits.read()

# Before Winnow Encryption
print("\n-------------------------------------------BEFORE WINNOW ENCRYPTION -----------------------------------------\n")

Transmitter_Bits_spaced = ' '.join(Transmitter_Bits[i:i+7] for i in range(0, len(Transmitter_Bits), 7))
print("Tx Bits are : " + Transmitter_Bits_spaced[:3000])
Receiver_Bits_spaced = ' '.join(Receiver_Bits[i:i+7] for i in range(0, len(Receiver_Bits), 7))
print("Rx Bits are : " + Receiver_Bits_spaced[:3000])

check_Error_String = ""
Error_Bits = 0

for i in range(0, int(len(Transmitter_Bits))):
    if Transmitter_Bits[i] == Receiver_Bits[i]:
        check_Error_String = check_Error_String + " "
    elif Transmitter_Bits[i] != Receiver_Bits[i]:
        check_Error_String = check_Error_String + "x"
        Error_Bits += 1

Error_String_Spaced = ' '.join(check_Error_String[i:i+7] for i in range(0, len(check_Error_String), 7))
print("Error Bits  : " + Error_String_Spaced[:3000])


print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Transmitter_Bits)))
Error_Percentage = (Error_Bits/int(len(Transmitter_Bits))) * 100
print("Error Percentage is " + str(Error_Percentage))


# After Winnow Encryption

with open("../Winnow Encryption Main Algorithm/Transmitter/Transmitter_Winnow-1_Final.txt", 'r') as Transmitter_Sifted_bits:
    Transmitter_Bits = Transmitter_Sifted_bits.read()

with open("../Winnow Encryption Main Algorithm/Receiver/Receiver_Winnow-1_Final.txt", 'r') as Receiver_Sifted_bits:
    Receiver_Bits = Receiver_Sifted_bits.read()

print("\n-------------------------------------------After WINNOW ENCRYPTION -----------------------------------------\n")

Transmitter_Bits_spaced = ' '.join(Transmitter_Bits[i:i+7] for i in range(0, len(Transmitter_Bits), 7))
print("Tx Bits are : " + Transmitter_Bits_spaced[:3000])
Receiver_Bits_spaced = ' '.join(Receiver_Bits[i:i+7] for i in range(0, len(Receiver_Bits), 7))
print("Rx Bits are : " + Receiver_Bits_spaced[:3000])

check_Error_String = ""
Error_Bits = 0

for i in range(0, int(len(Transmitter_Bits))):
    if Transmitter_Bits[i] == Receiver_Bits[i]:
        check_Error_String = check_Error_String + " "
    elif Transmitter_Bits[i] != Receiver_Bits[i]:
        check_Error_String = check_Error_String + "x"
        Error_Bits += 1

Error_String_Spaced = ' '.join(check_Error_String[i:i+7] for i in range(0, len(check_Error_String), 7))
print("Error Bits  : " + Error_String_Spaced[:3000])

print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Transmitter_Bits)))
Error_Percentage = (Error_Bits/int(len(Transmitter_Bits))) * 100
print("Error Percentage is " + str(Error_Percentage))


for k in range(2, int(n)+1):
    # New Approach
    print("----------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------ROUND " + str(k) + "----------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------")

    with open("../Permutation_Winnow/Winnow_Round_" + str(k) + "/Transmitter_Permuted_" + str(k) + ".txt", 'r') as Transmitter_Sifted_bits:
        Transmitter_Bits = Transmitter_Sifted_bits.read()

    with open("../Permutation_Winnow/Winnow_Round_" + str(k) + "/Receiver_Permuted_" + str(k) + ".txt", 'r') as Receiver_Sifted_bits:
        Receiver_Bits = Receiver_Sifted_bits.read()

    # Before Winnow Encryption
    print("\n-------------------------------------------BEFORE WINNOW ENCRYPTION -----------------------------------------\n")

    Transmitter_Bits_spaced = ' '.join(Transmitter_Bits[i:i + 7] for i in range(0, len(Transmitter_Bits), 7))
    print("Tx Bits are : " + Transmitter_Bits_spaced[:3000])
    Receiver_Bits_spaced = ' '.join(Receiver_Bits[i:i + 7] for i in range(0, len(Receiver_Bits), 7))
    print("Rx Bits are : " + Receiver_Bits_spaced[:3000])

    check_Error_String = ""
    Error_Bits = 0

    for i in range(0, int(len(Transmitter_Bits))):
        if Transmitter_Bits[i] == Receiver_Bits[i]:
            check_Error_String = check_Error_String + " "
        elif Transmitter_Bits[i] != Receiver_Bits[i]:
            check_Error_String = check_Error_String + "x"
            Error_Bits += 1

    Error_String_Spaced = ' '.join(check_Error_String[i:i + 7] for i in range(0, len(check_Error_String), 7))
    print("Error Bits  : " + Error_String_Spaced[:3000])

    print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Transmitter_Bits)))

    Error_Percentage = (Error_Bits/int(len(Transmitter_Bits))) * 100
    print("Error Percentage is " + str(Error_Percentage))


    # After Winnow Encryption

    with open("../Permutation_Winnow/Winnow_Round_" + str(k) + "/Transmitter_Winnow-" + str(k) + "_Final.txt", 'r') as Transmitter_Sifted_bits:
        Transmitter_Bits = Transmitter_Sifted_bits.read()

    with open("../Permutation_Winnow/Winnow_Round_" + str(k) + "/Receiver_Winnow-" + str(k) + "_Final.txt", 'r') as Receiver_Sifted_bits:
        Receiver_Bits = Receiver_Sifted_bits.read()

    print("\n-------------------------------------------After WINNOW ENCRYPTION -----------------------------------------\n")

    Transmitter_Bits_spaced = ' '.join(Transmitter_Bits[i:i + 7] for i in range(0, len(Transmitter_Bits), 7))
    print("Tx Bits are : " + Transmitter_Bits_spaced[:3000])
    Receiver_Bits_spaced = ' '.join(Receiver_Bits[i:i + 7] for i in range(0, len(Receiver_Bits), 7))
    print("Rx Bits are : " + Receiver_Bits_spaced[:3000])

    check_Error_String = ""
    Error_Bits = 0

    for i in range(0, int(len(Transmitter_Bits))):
        if Transmitter_Bits[i] == Receiver_Bits[i]:
            check_Error_String = check_Error_String + " "
        elif Transmitter_Bits[i] != Receiver_Bits[i]:
            check_Error_String = check_Error_String + "x"
            Error_Bits += 1

    Error_String_Spaced = ' '.join(check_Error_String[i:i + 7] for i in range(0, len(check_Error_String), 7))
    print("Error Bits  : " + Error_String_Spaced[:3000])

    print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Transmitter_Bits)))
    Error_Percentage = (Error_Bits/int(len(Transmitter_Bits))) * 100
    print("Error Percentage is " + str(Error_Percentage))


