# In this file, We are permuting the bits and then applying Winnow again

import numpy as np
import os
import pickle
import shutil

#-----------------------------Deleting Previous Useless Data Directries---------------------

for Dir in os.listdir('./'):
    Dir_Path = os.path.join('./', Dir)

    if os.path.isdir(Dir_Path):
        # Use shutil.rmtree() to delete the directory and its contents recursively
        shutil.rmtree(Dir_Path)


n = input("Enter the No. of times to apply Winnow : ")

for i in range(2, int(n) + 1):

    # -----------------------------Making New directry for separate rounds data ---------------------

    if os.path.exists("./Winnow_Round_" + str(i)):
        print("Directory " + str(i) + "already exists")
    else:
        os.mkdir("Winnow_Round_" + str(i))

    # -----------------------------Permuting--------------------------------------

    # Read data from Transmitter and Receiver Final files from previous rounds files for Permuting

    print("-------------------------------Permuting--------------------------------")
    if i == 2:
        with open("../Winnow Encryption Main Algorithm/Transmitter/Transmitter_Winnow-1_Final.txt", "r") as Transmitter_file:
            Transmitter_data = np.array([int(bit) for bit in Transmitter_file.read().strip()])

        with open("../Winnow Encryption Main Algorithm/Receiver/Receiver_Winnow-1_Final.txt", "r") as Receiver_file:
            Receiver_data = np.array([int(bit) for bit in Receiver_file.read().strip()])

    elif i > 2:
        with open("./Winnow_Round_" + str(i - 1) + "/Transmitter_Winnow-" + str(i - 1) + "_Final.txt", "r") as Transmitter_file:
            Transmitter_data = np.array([int(bit) for bit in Transmitter_file.read().strip()])

        with open("./Winnow_Round_" + str(i - 1) + "/Receiver_Winnow-" + str(i - 1) + "_Final.txt", "r") as Receiver_file:
            Receiver_data = np.array([int(bit) for bit in Receiver_file.read().strip()])

    # Generate a permutation
    permutation = np.random.permutation(len(Transmitter_data))

    # Apply permutation to Transmitter's data
    Transmitter_permuted = Transmitter_data[permutation]

    # Apply the same permutation to Receiver's data
    Receiver_permuted = Receiver_data[permutation]

    # Save permuted data to new files
    with open("./Winnow_Round_" + str(i) + "/Transmitter_Permuted_" + str(i) + ".txt", "w") as Transmitter_permuted_file:
        Transmitter_permuted_file.write("".join(map(str, Transmitter_permuted)))

    with open("./Winnow_Round_" + str(i) + "/Receiver_Permuted_" + str(i) + ".txt", "w") as Receiver_permuted_file:
        Receiver_permuted_file.write("".join(map(str, Receiver_permuted)))

    print("Permuted Round " + str(i) + " Files Transmitter_Permuted and Receiver_Permuted saved successfully.")

    # ---------------------------------------Permutation End-----------------------\

    # ----------------------------------------Transmitter Encryption of Round i----------------------------------------

    print("-------------------------------Transmitter Encryption--------------------------------")
    f = open("./Winnow_Round_" + str(i) + "/Transmitter_Permuted_" + str(i) + ".txt", "r")
    data = f.read()

    with open("./Winnow_Round_" + str(i) + "/Transmitter_Winnow-" + str(i) + "-Encrypted_File.txt", "w") as Transmitter_Encrypted:
        print("\nTransmitter Encryption " + str(i) + " created")
    Transmitter_Encrypted.close()

    global x_bits


    def Transmitter_Encrypting_Function():
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

        with open("./Winnow_Round_" + str(i) + "/Transmitter_Winnow-" + str(i) + "-Encrypted_File.txt",
                  "a") as Transmitter_Encrypted:

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


    Transmitter_Encrypting_Function()

    # ----------------------------------------Transmitter Encryption End of Round i----------------------------------------

    # ----------------------------------------Receiver Encryption of Round i----------------------------------------
    print("-------------------------------Receiver Encryption--------------------------------")

    f = open("./Winnow_Round_" + str(i) + "/Receiver_Permuted_" + str(i) + ".txt", "r")
    data = f.read()

    with open("./Winnow_Round_" + str(i) + "/Receiver_Winnow-" + str(i) + "-Encrypted_File.txt", "w") as Receiver_Encrypted:
        print("\nReceiver Encryption " + str(i) + " created")
    Receiver_Encrypted.close()

    global x_bits


    def Receiver_Encrypting_Function():
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

        with open("./Winnow_Round_" + str(i) + "/Receiver_Winnow-" + str(i) + "-Encrypted_File.txt",
                  "a") as Receiver_Encrypted:

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


    Receiver_Encrypting_Function()

    # ----------------------------------------Receiver Encryption End of Round i----------------------------------------

    # --------------------------------------------Receiver Decryption of Round i---------------------------------
    print("-------------------------------Receiver Decryption--------------------------------")

    with open("./Winnow_Round_" + str(i) + "/Receiver_Winnow-" + str(i) + "-Encrypted_File.txt", 'r') as Receiver_Encrypted:
        Receiver_Encrypted_Var = Receiver_Encrypted.read()

    with open("./Winnow_Round_" + str(i) + "/Transmitter_Winnow-" + str(i) + "-Encrypted_File.txt", 'r') as Transmitter_Encrypted:
        Transmitter_Encrypted_Var = Transmitter_Encrypted.read()

    # with open("Receiver_Sifted_File.txt", 'r') as Receiver_Sifted:
    #     Receiver_Sifted_Var = Receiver_Sifted.read()
    #
    # with open("Transmitter_Sifted_File.txt", 'r') as Transmitter_Sifted:
    #     Transmitter_Sifted_Var = Transmitter_Sifted.read()

    with open("./Winnow_Round_" + str(i) + "/Receiver_Permuted_" + str(i) + ".txt", 'r') as Receiver_Sifted:
        Receiver_Sifted_Var = Receiver_Sifted.read()

    with open("./Winnow_Round_" + str(i) + "/Transmitter_Permuted_" + str(i) + ".txt", 'r') as Transmitter_Sifted:
        Transmitter_Sifted_Var = Transmitter_Sifted.read()

    print("Tx " + str(i) + " : " + Transmitter_Sifted_Var)
    print("Rx " + str(i) + " : " + Receiver_Sifted_Var)
    Corrected_Receiver_Sifted_Var = ""

    counter = -1
    Transmitter_Removal_Blocks = []
    for j in range(0, int(len(Transmitter_Encrypted_Var) / 4)):
        counter += 1
        Transmitter_Syndrome = ""
        Receiver_Syndrome = ""
        for k in range(0, 4):
            Transmitter_Syndrome = Transmitter_Syndrome + Transmitter_Encrypted_Var[4 * j + k]
            Receiver_Syndrome = Receiver_Syndrome + Receiver_Encrypted_Var[4 * j + k]

        resultant_syndrome = str((int(Transmitter_Syndrome[0]) + int(Receiver_Syndrome[0])) % 2) + str(
            (int(Transmitter_Syndrome[1]) + int(Receiver_Syndrome[1])) % 2) + str(
            (int(Transmitter_Syndrome[2]) + int(Receiver_Syndrome[2])) % 2) + str(
            (int(Transmitter_Syndrome[3]) + int(Receiver_Syndrome[3])) % 2)

        temp = ""
        for l in range(0, 7):
            temp = temp + Receiver_Sifted_Var[(7 * j) + l]

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
            after_Removal_bits = new_Temp[2:3] + new_Temp[3 + 1:]
            Corrected_Receiver_Sifted_Var = Corrected_Receiver_Sifted_Var + after_Removal_bits

            # saving the values of those blocks in which Receiver has removed the information leaking bits and now Transmitter will
            # also remove
            Transmitter_Removal_Blocks.append(counter)

    # Out of loop
    print("Receiver 2 : " + Corrected_Receiver_Sifted_Var)
    print("List : " + str(Transmitter_Removal_Blocks))

    with open("./Winnow_Round_" + str(i) + "/Receiver_Winnow-" + str(i) + "_Final.txt", "w") as Final_Receiver_Bits:
        Final_Receiver_Bits.write(Corrected_Receiver_Sifted_Var)

    with open("./Winnow_Round_" + str(i) + "/Removal_Block_file_" + str(i) + ".txt", 'wb') as Removal_bits:
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
    print("-------------------------------Transmitter Decryption--------------------------------")

    with open("./Winnow_Round_" + str(i) + "/Removal_Block_file_" + str(i) + ".txt", 'rb') as Removal_bits:
        Transmitter_Removal_Blocks = pickle.load(Removal_bits)
        Removal_bits.close()

    # with open("Transmitter_Sifted_File.txt", 'r') as Transmitter_Sifted:
    #     Unchanged_data = Transmitter_Sifted.read()
    #     Transmitter_Sifted.close()

    with open("./Winnow_Round_" + str(i) + "/Transmitter_Permuted_" + str(i) + ".txt", 'r') as Transmitter_Sifted:
        Unchanged_data = Transmitter_Sifted.read()
        Transmitter_Sifted.close()

    print("Before : " + Unchanged_data)

    Corrected_Transmitter_Bits = ""
    counter = 0
    list_counter = 0

    for j in range(int(len(Unchanged_data) / 7)):

        temp = ""
        for l in range(0, 7):
            temp = temp + Unchanged_data[(7 * j) + l]

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
    print("Removed Transmitter bits and Created the file 'NAMED = Transmitter_Winnow-" + str(i) + "_Final.txt'")

    with open("./Winnow_Round_" + str(i) + "/Transmitter_Winnow-" + str(i) + "_Final.txt", "w") as Final_Transmitter_Bits:
        Final_Transmitter_Bits.write(Corrected_Transmitter_Bits)

    Final_Transmitter_Bits.close()

    # ---------------------------------------------------Transmitter Decryption End of Round i----------------------------------
