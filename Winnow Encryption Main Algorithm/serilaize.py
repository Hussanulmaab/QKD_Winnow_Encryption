import numpy as np

f = open("../Algorithm Check/Making Erreneous Files/My_Alice_Sifted.txt", "r")
data = f.read()

with open("Alice_Winnow-1-Encrypted_File.txt", "w") as Alice_Encrypted:
    print("Alice Encryption created")
Alice_Encrypted.close()

global x_bits


def main():
    for i in range(int(len(data) / 7)):
        block = ""
        for j in range(0, 7):
            block += data[(7 * i) + j]
        print("Block " + '%s' % i + " :: " + block)
        global x_bits
        x_bits = block

        Syndrome_Calculation()


# Error Correction
def Syndrome_Calculation():
    # Syndrome Calculation
    H3_Syndrome_Cal_Matrix = [
        [1, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1]
    ]

    Synd_Vector = ""
    temp_Synd_Vector = ""

    # Extended Winnow Parity check (8,4)
    parity_check = 0
    for col in range(7):
        parity_check += int(x_bits[col])

    if (parity_check % 2) == 0:
        Synd_Vector += str(0)
    elif (parity_check % 2) == 1:
        Synd_Vector += str(1)

    with open("Alice_Winnow-1-Encrypted_File.txt", "a") as Alice_Encrypted:

        for row in range(len(H3_Syndrome_Cal_Matrix)):
            temp = 0
            for col in range(7):
                temp += H3_Syndrome_Cal_Matrix[row][col] * int(x_bits[col])
            temp = temp % 2
            temp_Synd_Vector += str(temp)

        temp_Synd_Vector = temp_Synd_Vector[::-1]
        Synd_Vector += temp_Synd_Vector

        Alice_Encrypted.write(Synd_Vector)

        print("Syndrome -- " + Synd_Vector)

    Alice_Encrypted.close()


main()


import numpy as np

f = open("../Algorithm Check/Making Erreneous Files/My_Bob_Sifted.txt", "r")
data = f.read()

with open("Bob_Winnow-1-Encrypted_File.txt", "w") as Bob_Encrypted:
    print("Bob Encryption created")
Bob_Encrypted.close()

global x_bits


def main():
    for i in range(int(len(data) / 7)):
        block = ""
        for j in range(0, 7):
            block += data[(7 * i) + j]
        print("Block " + '%s' % i + " :: " + block)
        global x_bits
        x_bits = block

        Syndrome_Calculation()


# Error Correction
def Syndrome_Calculation():
    # Syndrome Calculation
    H3_Syndrome_Cal_Matrix = [
        [1, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1]
    ]

    Synd_Vector = ""
    temp_Synd_Vector = ""

    # Extended Winnow Parity check (8,4)
    parity_check = 0
    for col in range(7):
        parity_check += int(x_bits[col])

    if (parity_check % 2) == 0:
        Synd_Vector += str(0)
    elif (parity_check % 2) == 1:
        Synd_Vector += str(1)

    with open("Bob_Winnow-1-Encrypted_File.txt", "a") as Bob_Encrypted:

        for row in range(len(H3_Syndrome_Cal_Matrix)):
            temp = 0
            for col in range(7):
                temp += H3_Syndrome_Cal_Matrix[row][col] * int(x_bits[col])
            temp = temp % 2
            temp_Synd_Vector += str(temp)

        temp_Synd_Vector = temp_Synd_Vector[::-1]
        Synd_Vector += temp_Synd_Vector

        Bob_Encrypted.write(Synd_Vector)

        print("Syndrome -- " + Synd_Vector)

    Bob_Encrypted.close()


main()

import pickle

with open("Bob_Winnow-1-Encrypted_File.txt", 'r') as Bob_Encrypted:
    Bob_Encrypted_Var = Bob_Encrypted.read()

with open("Alice_Winnow-1-Encrypted_File.txt", 'r') as Alice_Encrypted:
    Alice_Encrypted_Var = Alice_Encrypted.read()

# with open("Bob_Sifted_File.txt", 'r') as Bob_Sifted:
#     Bob_Sifted_Var = Bob_Sifted.read()
#
# with open("Alice_Sifted_File.txt", 'r') as Alice_Sifted:
#     Alice_Sifted_Var = Alice_Sifted.read()

with open("../Algorithm Check/Making Erreneous Files/My_Bob_Sifted.txt", 'r') as Bob_Sifted:
    Bob_Sifted_Var = Bob_Sifted.read()

with open("../Algorithm Check/Making Erreneous Files/My_Alice_Sifted.txt", 'r') as Alice_Sifted:
    Alice_Sifted_Var = Alice_Sifted.read()

print("Ali 1 : " + Alice_Sifted_Var)
print("Bob 1 : " + Bob_Sifted_Var)
Corrected_Bob_Sifted_Var = ""

counter = -1
Alice_Removal_Blocks = []
for i in range(0, int(len(Alice_Encrypted_Var) / 4)):
    counter += 1
    Alice_Syndrome = ""
    Bob_Syndrome = ""
    for j in range(0, 4):
        Alice_Syndrome = Alice_Syndrome + Alice_Encrypted_Var[4 * i + j]
        Bob_Syndrome = Bob_Syndrome + Bob_Encrypted_Var[4 * i + j]

    resultant_syndrome = str((int(Alice_Syndrome[0]) + int(Bob_Syndrome[0])) % 2) + str(
        (int(Alice_Syndrome[1]) + int(Bob_Syndrome[1])) % 2) + str(
        (int(Alice_Syndrome[2]) + int(Bob_Syndrome[2])) % 2) + str((int(Alice_Syndrome[3]) + int(Bob_Syndrome[3])) % 2)

    temp = ""
    for k in range(0, 7):
        temp = temp + Bob_Sifted_Var[(7 * i) + k]

    new_Temp = ""

    if resultant_syndrome[0] == "0":
        new_Temp = temp
        Corrected_Bob_Sifted_Var = Corrected_Bob_Sifted_Var + new_Temp
    else:
        # Correcting the error and updating Bobs bits
        if resultant_syndrome == "1000":
            new_Temp = temp
            Corrected_Bob_Sifted_Var = Corrected_Bob_Sifted_Var + new_Temp
            continue
        elif resultant_syndrome == "1001":
            if temp[0] == "0":
                new_Temp = temp[:0] + "1" + temp[0 + 1:]
            elif temp[0] == "1":
                new_Temp = temp[:0] + "0" + temp[0 + 1:]

        elif resultant_syndrome == "1010":
            if temp[1] == "0":
                new_Temp = temp[:1] + "1" + temp[1 + 1:]
            elif temp[1] == "1":
                new_Temp = temp[:1] + "0" + temp[1 + 1:]

        elif resultant_syndrome == "1011":
            if temp[2] == "0":
                new_Temp = temp[:2] + "1" + temp[2 + 1:]
            elif temp[2] == "1":
                new_Temp = temp[:2] + "0" + temp[2 + 1:]

        elif resultant_syndrome == "1100":
            if temp[3] == "0":
                new_Temp = temp[:3] + "1" + temp[3 + 1:]
            elif temp[3] == "1":
                new_Temp = temp[:3] + "0" + temp[3 + 1:]

        elif resultant_syndrome == "1101":
            if temp[4] == "0":
                new_Temp = temp[:4] + "1" + temp[4 + 1:]
            elif temp[4] == "1":
                new_Temp = temp[:4] + "0" + temp[4 + 1:]

        elif resultant_syndrome == "1110":
            if temp[5] == "0":
                new_Temp = temp[:5] + "1" + temp[5 + 1:]
            elif temp[5] == "1":
                new_Temp = temp[:5] + "0" + temp[5 + 1:]

        elif resultant_syndrome == "1111":
            if temp[6] == "0":
                new_Temp = temp[:6] + "1" + temp[6 + 1:]
            elif temp[6] == "1":
                new_Temp = temp[:6] + "0" + temp[6 + 1:]

        # Removing the bits in the power of 2 (according to paper) so that no information is leaked
        after_Removal_bits = new_Temp[2:3] + new_Temp[3+1:]
        Corrected_Bob_Sifted_Var = Corrected_Bob_Sifted_Var + after_Removal_bits

        # saving the values of those blocks in which Bob has removed the information leaking bits and now Alice will
        # also remove
        Alice_Removal_Blocks.append(counter)

# Out of loop
print("Bob 2 : " + Corrected_Bob_Sifted_Var)
print("List : " + str(Alice_Removal_Blocks))

with open("Bob_Winnow-1_Final.txt", "w") as Final_Bob_Bits:
    Final_Bob_Bits.write(Corrected_Bob_Sifted_Var)

with open("Removal_Block_file_1.txt", 'wb') as Removal_bits:
    pickle.dump(Alice_Removal_Blocks, Removal_bits)

# closing files
Final_Bob_Bits.close()
Bob_Encrypted.close()
Alice_Encrypted.close()
Bob_Sifted.close()
Alice_Sifted.close()
Removal_bits.close()


import pickle

with open("Removal_Block_file_1.txt", 'rb') as Removal_bits:
    Alice_Removal_Blocks = pickle.load(Removal_bits)
    Removal_bits.close()

# with open("Alice_Sifted_File.txt", 'r') as Alice_Sifted:
#     Unchanged_data = Alice_Sifted.read()
#     Alice_Sifted.close()

with open("../Algorithm Check/Making Erreneous Files/My_Alice_Sifted.txt", 'r') as Alice_Sifted:
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
print("Removed Alice bits and Created the file 'NAMED = Alice_Winnow-1_Final.txt'")

with open("Alice_Winnow-1_Final.txt", "w") as Final_Alice_Bits:
    Final_Alice_Bits.write(Corrected_Alice_Bits)

Final_Alice_Bits.close()