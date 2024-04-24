n = input("Enter n : ")

print("----------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------ROUND 1----------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------")


# with open("Alice_Sifted_File.txt", 'r') as Alice_Sifted_bits:
#     Alice_Bits = Alice_Sifted_bits.read()
#
# with open("Bob_Sifted_File.txt", 'r') as Bob_Sifted_bits:
#     Bob_Bits = Bob_Sifted_bits.read()

with open("Making Erreneous Files/My_Alice_Sifted.txt", 'r') as Alice_Sifted_bits:
    Alice_Bits = Alice_Sifted_bits.read()

with open("Making Erreneous Files/My_Bob_Sifted.txt", 'r') as Bob_Sifted_bits:
    Bob_Bits = Bob_Sifted_bits.read()

# Before Winnow Encryption
print("\n-------------------------------------------BEFORE WINNOW ENCRYPTION -----------------------------------------\n")

print("Ali Bits are : " + Alice_Bits[:1000])
print("Bob Bits are : " + Bob_Bits[:1000])
check_Error_String = ""
Error_Bits = 0

for i in range(0, int(len(Alice_Bits))):
    if Alice_Bits[i] == Bob_Bits[i]:
        check_Error_String = check_Error_String + " "
    elif Alice_Bits[i] != Bob_Bits[i]:
        check_Error_String = check_Error_String + "x"
        Error_Bits += 1

print("Error Bits   : " + check_Error_String[:1000])
print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Alice_Bits)))

Error_Percentage = (Error_Bits/int(len(Alice_Bits))) * 100
print("Error Percentage is " + str(Error_Percentage))


# After Winnow Encryption

with open("../Winnow Encryption Main Algorithm/Alice_Winnow-1_Final.txt", 'r') as Alice_Sifted_bits:
    Alice_Bits = Alice_Sifted_bits.read()

with open("../Winnow Encryption Main Algorithm/Bob_Winnow-1_Final.txt", 'r') as Bob_Sifted_bits:
    Bob_Bits = Bob_Sifted_bits.read()

print("\n-------------------------------------------After WINNOW ENCRYPTION -----------------------------------------\n")

print("Ali Bits are : " + Alice_Bits[:1000])
print("Bob Bits are : " + Bob_Bits[:1000])
check_Error_String = ""
Error_Bits = 0

for i in range(0, int(len(Alice_Bits))):
    if Alice_Bits[i] == Bob_Bits[i]:
        check_Error_String = check_Error_String + " "
    elif Alice_Bits[i] != Bob_Bits[i]:
        check_Error_String = check_Error_String + "x"
        Error_Bits += 1

print("Error Bits   : " + check_Error_String[:1000])
print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Alice_Bits)))

Error_Percentage = (Error_Bits/int(len(Alice_Bits))) * 100
print("Error Percentage is " + str(Error_Percentage))


for k in range(2, int(n)+1):
    # New Approach
    print("----------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------ROUND " + str(k) + "----------------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------")

    with open("../New PseudoRandom Approach/Winnow_Round_" + str(k) + "/Alice_Permuted_" + str(k) + ".txt", 'r') as Alice_Sifted_bits:
        Alice_Bits = Alice_Sifted_bits.read()

    with open("../New PseudoRandom Approach/Winnow_Round_" + str(k) + "/Bob_Permuted_" + str(k) + ".txt", 'r') as Bob_Sifted_bits:
        Bob_Bits = Bob_Sifted_bits.read()

    # Before Winnow Encryption
    print("\n-------------------------------------------BEFORE WINNOW ENCRYPTION -----------------------------------------\n")

    print("Ali Bits are : " + Alice_Bits[:1000])
    print("Bob Bits are : " + Bob_Bits[:1000])
    check_Error_String = ""
    Error_Bits = 0

    for i in range(0, int(len(Alice_Bits))):
        if Alice_Bits[i] == Bob_Bits[i]:
            check_Error_String = check_Error_String + " "
        elif Alice_Bits[i] != Bob_Bits[i]:
            check_Error_String = check_Error_String + "x"
            Error_Bits += 1

    print("Error Bits     : " + check_Error_String[:1000])
    print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Alice_Bits)))

    Error_Percentage = (Error_Bits/int(len(Alice_Bits))) * 100
    print("Error Percentage is " + str(Error_Percentage))


    # After Winnow Encryption

    with open("../New PseudoRandom Approach/Winnow_Round_" + str(k) + "/Alice_Winnow-" + str(k) + "_Final.txt", 'r') as Alice_Sifted_bits:
        Alice_Bits = Alice_Sifted_bits.read()

    with open("../New PseudoRandom Approach/Winnow_Round_" + str(k) + "/Bob_Winnow-" + str(k) + "_Final.txt", 'r') as Bob_Sifted_bits:
        Bob_Bits = Bob_Sifted_bits.read()

    print("\n-------------------------------------------After WINNOW ENCRYPTION -----------------------------------------\n")

    print("Ali Bits are : " + Alice_Bits[:1000])
    print("Bob Bits are : " + Bob_Bits[:1000])
    check_Error_String = ""
    Error_Bits = 0

    for i in range(0, int(len(Alice_Bits))):
        if Alice_Bits[i] == Bob_Bits[i]:
            check_Error_String = check_Error_String + " "
        elif Alice_Bits[i] != Bob_Bits[i]:
            check_Error_String = check_Error_String + "x"
            Error_Bits += 1

    print("Error Bits     : " + check_Error_String[:1000])
    print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Alice_Bits)))

    Error_Percentage = (Error_Bits/int(len(Alice_Bits))) * 100
    print("Error Percentage is " + str(Error_Percentage))

