n = input("Enter n : ")

print("----------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------ROUND 1----------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------")


# with open("Transmitter_Sifted_File.txt", 'r') as Transmitter_Sifted_bits:
#     Transmitter_Bits = Transmitter_Sifted_bits.read()
#
# with open("Receiver_Sifted_File.txt", 'r') as Receiver_Sifted_bits:
#     Receiver_Bits = Receiver_Sifted_bits.read()

with open("Making Erreneous Files/Transmitter_Sifted.txt", 'r') as Transmitter_Sifted_bits:
    Transmitter_Bits = Transmitter_Sifted_bits.read()

with open("Making Erreneous Files/Receiver_Sifted.txt", 'r') as Receiver_Sifted_bits:
    Receiver_Bits = Receiver_Sifted_bits.read()

# Before Winnow Encryption
print("\n-------------------------------------------BEFORE WINNOW ENCRYPTION -----------------------------------------\n")

Transmitter_Bits_spaced = ' '.join(Transmitter_Bits[i:i+7] for i in range(0, len(Transmitter_Bits), 7))
print("Ali Bits are : " + Transmitter_Bits_spaced[:1000])
Receiver_Bits_spaced = ' '.join(Receiver_Bits[i:i+7] for i in range(0, len(Receiver_Bits), 7))
print("Receiver Bits are : " + Receiver_Bits_spaced[:1000])

check_Error_String = ""
Error_Bits = 0

for i in range(0, int(len(Transmitter_Bits))):
    if Transmitter_Bits[i] == Receiver_Bits[i]:
        check_Error_String = check_Error_String + " "
    elif Transmitter_Bits[i] != Receiver_Bits[i]:
        check_Error_String = check_Error_String + "x"
        Error_Bits += 1

Error_String_Spaced = ' '.join(check_Error_String[i:i+7] for i in range(0, len(check_Error_String), 7))
print("Error Bits   : " + Error_String_Spaced[:1000])


print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Transmitter_Bits)))
Error_Percentage = (Error_Bits/int(len(Transmitter_Bits))) * 100
print("Error Percentage is " + str(Error_Percentage))


# After Winnow Encryption

with open("../Winnow Encryption Main Algorithm/Transmitter_Winnow-1_Final.txt", 'r') as Transmitter_Sifted_bits:
    Transmitter_Bits = Transmitter_Sifted_bits.read()

with open("../Winnow Encryption Main Algorithm/Receiver_Winnow-1_Final.txt", 'r') as Receiver_Sifted_bits:
    Receiver_Bits = Receiver_Sifted_bits.read()

print("\n-------------------------------------------After WINNOW ENCRYPTION -----------------------------------------\n")

Transmitter_Bits_spaced = ' '.join(Transmitter_Bits[i:i+7] for i in range(0, len(Transmitter_Bits), 7))
print("Ali Bits are : " + Transmitter_Bits_spaced[:1000])
Receiver_Bits_spaced = ' '.join(Receiver_Bits[i:i+7] for i in range(0, len(Receiver_Bits), 7))
print("Receiver Bits are : " + Receiver_Bits_spaced[:1000])

check_Error_String = ""
Error_Bits = 0

for i in range(0, int(len(Transmitter_Bits))):
    if Transmitter_Bits[i] == Receiver_Bits[i]:
        check_Error_String = check_Error_String + " "
    elif Transmitter_Bits[i] != Receiver_Bits[i]:
        check_Error_String = check_Error_String + "x"
        Error_Bits += 1

Error_String_Spaced = ' '.join(check_Error_String[i:i+7] for i in range(0, len(check_Error_String), 7))
print("Error Bits   : " + Error_String_Spaced[:1000])

print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Transmitter_Bits)))
Error_Percentage = (Error_Bits/int(len(Transmitter_Bits))) * 100
print("Error Percentage is " + str(Error_Percentage))


for k in range(2, int(n)+1):
    # New Approach
    print("----------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------ROUND " + str(k) + "----------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------")

    with open("../New PseudoRandom Approach/Winnow_Round_" + str(k) + "/Transmitter_Permuted_" + str(k) + ".txt", 'r') as Transmitter_Sifted_bits:
        Transmitter_Bits = Transmitter_Sifted_bits.read()

    with open("../New PseudoRandom Approach/Winnow_Round_" + str(k) + "/Receiver_Permuted_" + str(k) + ".txt", 'r') as Receiver_Sifted_bits:
        Receiver_Bits = Receiver_Sifted_bits.read()

    # Before Winnow Encryption
    print("\n-------------------------------------------BEFORE WINNOW ENCRYPTION -----------------------------------------\n")

    Transmitter_Bits_spaced = ' '.join(Transmitter_Bits[i:i + 7] for i in range(0, len(Transmitter_Bits), 7))
    print("Ali Bits are : " + Transmitter_Bits_spaced[:1000])
    Receiver_Bits_spaced = ' '.join(Receiver_Bits[i:i + 7] for i in range(0, len(Receiver_Bits), 7))
    print("Receiver Bits are : " + Receiver_Bits_spaced[:1000])

    check_Error_String = ""
    Error_Bits = 0

    for i in range(0, int(len(Transmitter_Bits))):
        if Transmitter_Bits[i] == Receiver_Bits[i]:
            check_Error_String = check_Error_String + " "
        elif Transmitter_Bits[i] != Receiver_Bits[i]:
            check_Error_String = check_Error_String + "x"
            Error_Bits += 1

    Error_String_Spaced = ' '.join(check_Error_String[i:i + 7] for i in range(0, len(check_Error_String), 7))
    print("Error Bits   : " + Error_String_Spaced[:1000])

    print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Transmitter_Bits)))

    Error_Percentage = (Error_Bits/int(len(Transmitter_Bits))) * 100
    print("Error Percentage is " + str(Error_Percentage))


    # After Winnow Encryption

    with open("../New PseudoRandom Approach/Winnow_Round_" + str(k) + "/Transmitter_Winnow-" + str(k) + "_Final.txt", 'r') as Transmitter_Sifted_bits:
        Transmitter_Bits = Transmitter_Sifted_bits.read()

    with open("../New PseudoRandom Approach/Winnow_Round_" + str(k) + "/Receiver_Winnow-" + str(k) + "_Final.txt", 'r') as Receiver_Sifted_bits:
        Receiver_Bits = Receiver_Sifted_bits.read()

    print("\n-------------------------------------------After WINNOW ENCRYPTION -----------------------------------------\n")

    Transmitter_Bits_spaced = ' '.join(Transmitter_Bits[i:i + 7] for i in range(0, len(Transmitter_Bits), 7))
    print("Ali Bits are : " + Transmitter_Bits_spaced[:1000])
    Receiver_Bits_spaced = ' '.join(Receiver_Bits[i:i + 7] for i in range(0, len(Receiver_Bits), 7))
    print("Receiver Bits are : " + Receiver_Bits_spaced[:1000])

    check_Error_String = ""
    Error_Bits = 0

    for i in range(0, int(len(Transmitter_Bits))):
        if Transmitter_Bits[i] == Receiver_Bits[i]:
            check_Error_String = check_Error_String + " "
        elif Transmitter_Bits[i] != Receiver_Bits[i]:
            check_Error_String = check_Error_String + "x"
            Error_Bits += 1

    Error_String_Spaced = ' '.join(check_Error_String[i:i + 7] for i in range(0, len(check_Error_String), 7))
    print("Error Bits   : " + Error_String_Spaced[:1000])

    print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Transmitter_Bits)))
    Error_Percentage = (Error_Bits/int(len(Transmitter_Bits))) * 100
    print("Error Percentage is " + str(Error_Percentage))

