# with open("Alice_Sifted_File.txt", 'r') as Alice_Sifted_bits:
#     Alice_Bits = Alice_Sifted_bits.read()
#
# with open("Bob_Sifted_File.txt", 'r') as Bob_Sifted_bits:
#     Bob_Bits = Bob_Sifted_bits.read()

with open("../check.txt", 'r') as Alice_Sifted_bits:
    Alice_Bits = Alice_Sifted_bits.read()

with open("../checkError.txt", 'r') as Bob_Sifted_bits:
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

with open("../FInal Files/Final_Alice_Bits_File.txt", 'r') as Alice_Sifted_bits:
    Alice_Bits = Alice_Sifted_bits.read()

with open("../FInal Files/Final_Bob_Bits_File.txt", 'r') as Bob_Sifted_bits:
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