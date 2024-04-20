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

print("Alice Bits are : " + Alice_Bits)
print("Bob bits are   : " + Bob_Bits)
check_Error_String = ""
Error_Bits = 0

for i in range(0, int(len(Alice_Bits))):
    if Alice_Bits[i] == Bob_Bits[i]:
        check_Error_String = check_Error_String + " "
    elif Alice_Bits[i] != Bob_Bits[i]:
        check_Error_String = check_Error_String + "x"
        Error_Bits += 1

print("Error Bits     : " + check_Error_String)
print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Alice_Bits)))

Error_Percentage = (Error_Bits/int(len(Alice_Bits))) * 100
print("Error Percentage is " + str(Error_Percentage))


# After Winnow Encryption

with open("../Winnow Encryption Main Algorithm/Alice_Winnow-1_Final.txt", 'r') as Alice_Sifted_bits:
    Alice_Bits = Alice_Sifted_bits.read()

with open("../Winnow Encryption Main Algorithm/Bob_Winnow-1_Final.txt", 'r') as Bob_Sifted_bits:
    Bob_Bits = Bob_Sifted_bits.read()

print("\n-------------------------------------------After WINNOW ENCRYPTION -----------------------------------------\n")

print("Alice Bits are : " + Alice_Bits)
print("Bob bits are   : " + Bob_Bits)
check_Error_String = ""
Error_Bits = 0

for i in range(0, int(len(Alice_Bits))):
    if Alice_Bits[i] == Bob_Bits[i]:
        check_Error_String = check_Error_String + " "
    elif Alice_Bits[i] != Bob_Bits[i]:
        check_Error_String = check_Error_String + "x"
        Error_Bits += 1

print("Error Bits     : " + check_Error_String)
print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Alice_Bits)))

Error_Percentage = (Error_Bits/int(len(Alice_Bits))) * 100
print("Error Percentage is " + str(Error_Percentage))


# New Approach
print("----------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------ROUND 2----------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------")

with open("../New PseudoRandom Approach/Winnow_Round_2/Alice_Permuted_2.txt", 'r') as Alice_Sifted_bits:
    Alice_Bits = Alice_Sifted_bits.read()

with open("../New PseudoRandom Approach/Winnow_Round_2/Bob_Permuted_2.txt", 'r') as Bob_Sifted_bits:
    Bob_Bits = Bob_Sifted_bits.read()

# Before Winnow Encryption
print("\n-------------------------------------------BEFORE WINNOW ENCRYPTION -----------------------------------------\n")

print("Alice Bits are : " + Alice_Bits)
print("Bob bits are   : " + Bob_Bits)
check_Error_String = ""
Error_Bits = 0

for i in range(0, int(len(Alice_Bits))):
    if Alice_Bits[i] == Bob_Bits[i]:
        check_Error_String = check_Error_String + " "
    elif Alice_Bits[i] != Bob_Bits[i]:
        check_Error_String = check_Error_String + "x"
        Error_Bits += 1

print("Error Bits     : " + check_Error_String)
print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Alice_Bits)))

Error_Percentage = (Error_Bits/int(len(Alice_Bits))) * 100
print("Error Percentage is " + str(Error_Percentage))


# After Winnow Encryption

with open("../New PseudoRandom Approach/Winnow_Round_2/Alice_Winnow-2_Final.txt", 'r') as Alice_Sifted_bits:
    Alice_Bits = Alice_Sifted_bits.read()

with open("../New PseudoRandom Approach/Winnow_Round_2/Bob_Winnow-2_Final.txt", 'r') as Bob_Sifted_bits:
    Bob_Bits = Bob_Sifted_bits.read()

print("\n-------------------------------------------After WINNOW ENCRYPTION -----------------------------------------\n")

print("Alice Bits are : " + Alice_Bits)
print("Bob bits are   : " + Bob_Bits)
check_Error_String = ""
Error_Bits = 0

for i in range(0, int(len(Alice_Bits))):
    if Alice_Bits[i] == Bob_Bits[i]:
        check_Error_String = check_Error_String + " "
    elif Alice_Bits[i] != Bob_Bits[i]:
        check_Error_String = check_Error_String + "x"
        Error_Bits += 1

print("Error Bits     : " + check_Error_String)
print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Alice_Bits)))

Error_Percentage = (Error_Bits/int(len(Alice_Bits))) * 100
print("Error Percentage is " + str(Error_Percentage))




# New Approach
print("----------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------ROUND 3----------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------")

with open("../New PseudoRandom Approach/Winnow_Round_3/Alice_Winnow-3_Final.txt", 'r') as Alice_Sifted_bits:
    Alice_Bits = Alice_Sifted_bits.read()

with open("../New PseudoRandom Approach/Winnow_Round_3/Bob_Winnow-3_Final.txt", 'r') as Bob_Sifted_bits:
    Bob_Bits = Bob_Sifted_bits.read()

# Before Winnow Encryption
print("\n-------------------------------------------BEFORE WINNOW ENCRYPTION -----------------------------------------\n")

print("Alice Bits are : " + Alice_Bits)
print("Bob bits are   : " + Bob_Bits)
check_Error_String = ""
Error_Bits = 0

for i in range(0, int(len(Alice_Bits))):
    if Alice_Bits[i] == Bob_Bits[i]:
        check_Error_String = check_Error_String + " "
    elif Alice_Bits[i] != Bob_Bits[i]:
        check_Error_String = check_Error_String + "x"
        Error_Bits += 1

print("Error Bits     : " + check_Error_String)
print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Alice_Bits)))

Error_Percentage = (Error_Bits/int(len(Alice_Bits))) * 100
print("Error Percentage is " + str(Error_Percentage))


# After Winnow Encryption

with open("../New PseudoRandom Approach/Winnow_Round_3/Alice_Winnow-3_Final.txt", 'r') as Alice_Sifted_bits:
    Alice_Bits = Alice_Sifted_bits.read()

with open("../New PseudoRandom Approach/Winnow_Round_3/Bob_Winnow-3_Final.txt", 'r') as Bob_Sifted_bits:
    Bob_Bits = Bob_Sifted_bits.read()

print("\n-------------------------------------------After WINNOW ENCRYPTION -----------------------------------------\n")

print("Alice Bits are : " + Alice_Bits)
print("Bob bits are   : " + Bob_Bits)
check_Error_String = ""
Error_Bits = 0

for i in range(0, int(len(Alice_Bits))):
    if Alice_Bits[i] == Bob_Bits[i]:
        check_Error_String = check_Error_String + " "
    elif Alice_Bits[i] != Bob_Bits[i]:
        check_Error_String = check_Error_String + "x"
        Error_Bits += 1

print("Error Bits     : " + check_Error_String)
print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Alice_Bits)))

Error_Percentage = (Error_Bits/int(len(Alice_Bits))) * 100
print("Error Percentage is " + str(Error_Percentage))


# New Approach
print("----------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------ROUND 4----------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------")

with open("../New PseudoRandom Approach/Winnow_Round_4/Alice_Permuted_4.txt", 'r') as Alice_Sifted_bits:
    Alice_Bits = Alice_Sifted_bits.read()

with open("../New PseudoRandom Approach/Winnow_Round_4/Bob_Permuted_4.txt", 'r') as Bob_Sifted_bits:
    Bob_Bits = Bob_Sifted_bits.read()

# Before Winnow Encryption
print("\n-------------------------------------------BEFORE WINNOW ENCRYPTION -----------------------------------------\n")

print("Alice Bits are : " + Alice_Bits)
print("Bob bits are   : " + Bob_Bits)
check_Error_String = ""
Error_Bits = 0

for i in range(0, int(len(Alice_Bits))):
    if Alice_Bits[i] == Bob_Bits[i]:
        check_Error_String = check_Error_String + " "
    elif Alice_Bits[i] != Bob_Bits[i]:
        check_Error_String = check_Error_String + "x"
        Error_Bits += 1

print("Error Bits     : " + check_Error_String)
print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Alice_Bits)))

Error_Percentage = (Error_Bits/int(len(Alice_Bits))) * 100
print("Error Percentage is " + str(Error_Percentage))


# After Winnow Encryption

with open("../New PseudoRandom Approach/Winnow_Round_4/Alice_Winnow-4_Final.txt", 'r') as Alice_Sifted_bits:
    Alice_Bits = Alice_Sifted_bits.read()

with open("../New PseudoRandom Approach/Winnow_Round_4/Bob_Winnow-4_Final.txt", 'r') as Bob_Sifted_bits:
    Bob_Bits = Bob_Sifted_bits.read()

print("\n-------------------------------------------After WINNOW ENCRYPTION -----------------------------------------\n")

print("Alice Bits are : " + Alice_Bits)
print("Bob bits are   : " + Bob_Bits)
check_Error_String = ""
Error_Bits = 0

for i in range(0, int(len(Alice_Bits))):
    if Alice_Bits[i] == Bob_Bits[i]:
        check_Error_String = check_Error_String + " "
    elif Alice_Bits[i] != Bob_Bits[i]:
        check_Error_String = check_Error_String + "x"
        Error_Bits += 1

print("Error Bits     : " + check_Error_String)
print("Number of Error Bits are " + str(Error_Bits) + " out of " + str(len(Alice_Bits)))

Error_Percentage = (Error_Bits/int(len(Alice_Bits))) * 100
print("Error Percentage is " + str(Error_Percentage))