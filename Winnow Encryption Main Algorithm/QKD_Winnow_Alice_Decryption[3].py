import pickle

with open("../Removal_Block_file.txt", 'rb') as Removal_bits:
    Alice_Removal_Blocks = pickle.load(Removal_bits)
    Removal_bits.close()

# with open("Alice_Sifted_File.txt", 'r') as Alice_Sifted:
#     Unchanged_data = Alice_Sifted.read()
#     Alice_Sifted.close()

with open("../check.txt", 'r') as Alice_Sifted:
    Unchanged_data = Alice_Sifted.read()
    Alice_Sifted.close()

print("Before : " + Unchanged_data)

Corrected_Alice_Bits = ""
counter = 0
list_counter = 0

for i in range(int(len(Unchanged_data)/7)):

    temp = ""
    for k in range(0, 7):
        temp = temp + Unchanged_data[(7 * i) + k]

    if list_counter < len(Alice_Removal_Blocks):
        if Alice_Removal_Blocks[list_counter] == counter:
            after_Removal_bits = temp[2:3] + temp[3 + 1:]
            Corrected_Alice_Bits = Corrected_Alice_Bits + after_Removal_bits
            list_counter += 1
        elif Alice_Removal_Blocks[list_counter] != counter:
            Corrected_Alice_Bits = Corrected_Alice_Bits + temp
    else:
        Corrected_Alice_Bits = Corrected_Alice_Bits + temp

    counter += 1

print("After  : " + Corrected_Alice_Bits)
print("Removed Alice bits and Created the file 'NAMED = Final_Alice_Bits_File.txt'")

with open("../FInal Files/Final_Alice_Bits_File.txt", "w") as Final_Alice_Bits:
    Final_Alice_Bits.write(Corrected_Alice_Bits)

Final_Alice_Bits.close()