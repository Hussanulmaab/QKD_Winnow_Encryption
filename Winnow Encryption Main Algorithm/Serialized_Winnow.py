# ----------------------------------------Transmitter Encryption Start----------------------------------------
import pickle

f = open("../Performance Check/Making Erreneous Files/Transmitter_Sifted.txt", "r")
data = f.read()

with open("Transmitter_Winnow-1-Encrypted_File.txt", "w") as Transmitter_Encrypted:
    print("Transmitter Encryption created")
Transmitter_Encrypted.close()

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

    with open("Transmitter_Winnow-1-Encrypted_File.txt", "a") as Transmitter_Encrypted:

        for row in range(len(H3_Syndrome_Cal_Matrix)):
            temp = 0
            for col in range(7):
                temp += H3_Syndrome_Cal_Matrix[row][col] * int(x_bits[col])
            temp = temp % 2
            temp_Synd_Vector += str(temp)

        temp_Synd_Vector = temp_Synd_Vector[::-1]
        Synd_Vector += temp_Synd_Vector

        Transmitter_Encrypted.write(Synd_Vector)

        print("Syndrome -- " + Synd_Vector)

    Transmitter_Encrypted.close()


main()

# ----------------------------------------Transmitter Encryption End----------------------------------------

# ----------------------------------------Receiver Encryption Start----------------------------------------

f = open("../Performance Check/Making Erreneous Files/Receiver_Sifted.txt", "r")
data = f.read()

with open("Receiver_Winnow-1-Encrypted_File.txt", "w") as Receiver_Encrypted:
    print("Receiver Encryption created")
Receiver_Encrypted.close()

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

    with open("Receiver_Winnow-1-Encrypted_File.txt", "a") as Receiver_Encrypted:

        for row in range(len(H3_Syndrome_Cal_Matrix)):
            temp = 0
            for col in range(7):
                temp += H3_Syndrome_Cal_Matrix[row][col] * int(x_bits[col])
            temp = temp % 2
            temp_Synd_Vector += str(temp)

        temp_Synd_Vector = temp_Synd_Vector[::-1]
        Synd_Vector += temp_Synd_Vector

        Receiver_Encrypted.write(Synd_Vector)

        print("Syndrome -- " + Synd_Vector)

    Receiver_Encrypted.close()


main()

# ----------------------------------------Receiver Encryption End----------------------------------------

# --------------------------------------------Receiver Decryption Start---------------------------------

with open("Receiver_Winnow-1-Encrypted_File.txt", 'r') as Receiver_Encrypted:
    Receiver_Encrypted_Var = Receiver_Encrypted.read()

with open("Transmitter_Winnow-1-Encrypted_File.txt", 'r') as Transmitter_Encrypted:
    Transmitter_Encrypted_Var = Transmitter_Encrypted.read()

# with open("Receiver_Sifted_File.txt", 'r') as Receiver_Sifted:
#     Receiver_Sifted_Var = Receiver_Sifted.read()
#
# with open("Transmitter_Sifted_File.txt", 'r') as Transmitter_Sifted:
#     Transmitter_Sifted_Var = Transmitter_Sifted.read()

with open("../Performance Check/Making Erreneous Files/Receiver_Sifted.txt", 'r') as Receiver_Sifted:
    Receiver_Sifted_Var = Receiver_Sifted.read()

with open("../Performance Check/Making Erreneous Files/Transmitter_Sifted.txt", 'r') as Transmitter_Sifted:
    Transmitter_Sifted_Var = Transmitter_Sifted.read()

print("Tx 1 : " + Transmitter_Sifted_Var)
print("Rx 1 : " + Receiver_Sifted_Var)
Corrected_Receiver_Sifted_Var = ""

counter = -1
Transmitter_Removal_Blocks = []
for i in range(0, int(len(Transmitter_Encrypted_Var) / 4)):
    counter += 1
    Transmitter_Syndrome = ""
    Receiver_Syndrome = ""
    for j in range(0, 4):
        Transmitter_Syndrome = Transmitter_Syndrome + Transmitter_Encrypted_Var[4 * i + j]
        Receiver_Syndrome = Receiver_Syndrome + Receiver_Encrypted_Var[4 * i + j]

    resultant_syndrome = str((int(Transmitter_Syndrome[0]) + int(Receiver_Syndrome[0])) % 2) + str(
        (int(Transmitter_Syndrome[1]) + int(Receiver_Syndrome[1])) % 2) + str(
        (int(Transmitter_Syndrome[2]) + int(Receiver_Syndrome[2])) % 2) + str((int(Transmitter_Syndrome[3]) + int(Receiver_Syndrome[3])) % 2)

    temp = ""
    for k in range(0, 7):
        temp = temp + Receiver_Sifted_Var[(7 * i) + k]

    new_Temp = ""

    if resultant_syndrome[0] == "0":
        new_Temp = temp
        Corrected_Receiver_Sifted_Var = Corrected_Receiver_Sifted_Var + new_Temp
    else:
        # Correcting the error and updating Receivers bits
        if resultant_syndrome == "1000":
            new_Temp = temp
            Corrected_Receiver_Sifted_Var = Corrected_Receiver_Sifted_Var + new_Temp
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
        Corrected_Receiver_Sifted_Var = Corrected_Receiver_Sifted_Var + after_Removal_bits

        # saving the values of those blocks in which Receiver has removed the information leaking bits and now Transmitter will
        # also remove
        Transmitter_Removal_Blocks.append(counter)

# Out of loop
print("Receiver 2 : " + Corrected_Receiver_Sifted_Var)
print("List : " + str(Transmitter_Removal_Blocks))

with open("Receiver_Winnow-1_Final.txt", "w") as Final_Receiver_Bits:
    Final_Receiver_Bits.write(Corrected_Receiver_Sifted_Var)

with open("Removal_Block_file_1.txt", 'wb') as Removal_bits:
    pickle.dump(Transmitter_Removal_Blocks, Removal_bits)

# closing files
Final_Receiver_Bits.close()
Receiver_Encrypted.close()
Transmitter_Encrypted.close()
Receiver_Sifted.close()
Transmitter_Sifted.close()
Removal_bits.close()

# ---------------------------------------------------Receiver Decryption end of Round i----------------------------------

# ---------------------------------------------------Transmitter Decryption of Round i----------------------------------

with open("Removal_Block_file_1.txt", 'rb') as Removal_bits:
    Transmitter_Removal_Blocks = pickle.load(Removal_bits)
    Removal_bits.close()

# with open("Transmitter_Sifted_File.txt", 'r') as Transmitter_Sifted:
#     Unchanged_data = Transmitter_Sifted.read()
#     Transmitter_Sifted.close()

with open("../Performance Check/Making Erreneous Files/Transmitter_Sifted.txt", 'r') as Transmitter_Sifted:
    Unchanged_data = Transmitter_Sifted.read()
    Transmitter_Sifted.close()

print("Before : " + Unchanged_data)

Corrected_Transmitter_Bits = ""
counter = 0
list_counter = 0

for i in range(int(len(Unchanged_data)/7)):

    temp = ""
    for k in range(0, 7):
        temp = temp + Unchanged_data[(7 * i) + k]

    if list_counter < len(Transmitter_Removal_Blocks):
        if Transmitter_Removal_Blocks[list_counter] == counter:
            after_Removal_bits = temp[2:3] + temp[3 + 1:]
            Corrected_Transmitter_Bits = Corrected_Transmitter_Bits + after_Removal_bits
            list_counter += 1
        elif Transmitter_Removal_Blocks[list_counter] != counter:
            Corrected_Transmitter_Bits = Corrected_Transmitter_Bits + temp
    else:
        Corrected_Transmitter_Bits = Corrected_Transmitter_Bits + temp

    counter += 1

print("After  : " + Corrected_Transmitter_Bits)
print("Removed Transmitter bits and Created the file 'NAMED = Transmitter_Winnow-1_Final.txt'")

with open("Transmitter_Winnow-1_Final.txt", "w") as Final_Transmitter_Bits:
    Final_Transmitter_Bits.write(Corrected_Transmitter_Bits)

Final_Transmitter_Bits.close()

# ---------------------------------------------------Transmitter Decryption End----------------------------------
