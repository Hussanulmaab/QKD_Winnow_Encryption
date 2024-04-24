# In this file, We are permuting the bits and then applying Winnow again

import numpy as np
import os
import pickle
import shutil

# -----------------------------Deleting Previous Data---------------------

for Dir in os.listdir('./'):
    Dir_Path = os.path.join('./', Dir)

    if os.path.isdir(Dir_Path):
        # Use shutil.rmtree() to delete the directory and its contents recursively
        shutil.rmtree(Dir_Path)


n = input("Enter the No. of times to apply Winnow : ")

for i in range(2, int(n)+1):

    #-----------------------------Making New directry for separate rounds data ---------------------

    if os.path.exists("./Winnow_Round_" + str(i)):
        print("Directory " + str(i) + "already exists")
    else :
        os.mkdir("Winnow_Round_" + str(i))



    #-----------------------------Permuting--------------------------------------

    # Read data from Alice and Bob Final files from previous rounds files for Permuting
    if i==2:
        with open("../Winnow Encryption Main Algorithm/Alice_Winnow-1_Final.txt", "r") as alice_file:
            alice_data = np.array([int(bit) for bit in alice_file.read().strip()])

        with open("../Winnow Encryption Main Algorithm/Bob_Winnow-1_Final.txt", "r") as bob_file:
            bob_data = np.array([int(bit) for bit in bob_file.read().strip()])

    elif i > 2:
        with open("./Winnow_Round_" + str(i-1) + "/Alice_Winnow-" + str(i-1) + "_Final.txt", "r") as alice_file:
            alice_data = np.array([int(bit) for bit in alice_file.read().strip()])

        with open("./Winnow_Round_" + str(i-1) + "/Bob_Winnow-" + str(i-1) + "_Final.txt", "r") as bob_file:
            bob_data = np.array([int(bit) for bit in bob_file.read().strip()])

    # Generate a permutation
    permutation = np.random.permutation(len(alice_data))

    # Apply permutation to Alice's data
    alice_permuted = alice_data[permutation]

    # Apply the same permutation to Bob's data
    bob_permuted = bob_data[permutation]

    # Save permuted data to new files
    with open("./Winnow_Round_" + str(i) + "/Alice_Permuted_" + str(i) + ".txt", "w") as alice_permuted_file:
        alice_permuted_file.write("".join(map(str, alice_permuted)))

    with open("./Winnow_Round_" + str(i) + "/Bob_Permuted_" + str(i) + ".txt", "w") as bob_permuted_file:
        bob_permuted_file.write("".join(map(str, bob_permuted)))

    print("Permuted Round " + str(i) + " Files Alice_Permuted and Bob_Permuted saved successfully.")
    #---------------------------------------Permutation End-----------------------\



    #----------------------------------------Alice Encryption of Round i----------------------------------------

    f = open("./Winnow_Round_" + str(i) + "/Alice_Permuted_" + str(i) + ".txt", "r")
    data = f.read()

    with open("./Winnow_Round_" + str(i) + "/Alice_Winnow-" + str(i) + "-Encrypted_File.txt", "w") as Alice_Encrypted:
        print("Alice Encryption " + str(i) + " created")
    Alice_Encrypted.close()

    global x_bits

    def Alice_Encrypting_Function():
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

        with open("./Winnow_Round_" + str(i) + "/Alice_Winnow-" + str(i) + "-Encrypted_File.txt", "a") as Alice_Encrypted:

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

    Alice_Encrypting_Function()

    #----------------------------------------Alice Encryption End of Round i----------------------------------------



    # ----------------------------------------Bob Encryption of Round i----------------------------------------

    f = open("./Winnow_Round_" + str(i) + "/Bob_Permuted_" + str(i) + ".txt", "r")
    data = f.read()

    with open("./Winnow_Round_" + str(i) + "/Bob_Winnow-" + str(i) + "-Encrypted_File.txt", "w") as Bob_Encrypted:
        print("Bob Encryption " + str(i) + " created")
    Bob_Encrypted.close()

    global x_bits

    def Bob_Encrypting_Function():
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

        with open("./Winnow_Round_" + str(i) + "/Bob_Winnow-" + str(i) + "-Encrypted_File.txt",
                  "a") as Bob_Encrypted:

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


    Bob_Encrypting_Function()

    # ----------------------------------------Bob Encryption End of Round i----------------------------------------



    #--------------------------------------------Bob Decryption of Round i---------------------------------

    with open("./Winnow_Round_" + str(i) + "/Bob_Winnow-" + str(i) + "-Encrypted_File.txt", 'r') as Bob_Encrypted:
        Bob_Encrypted_Var = Bob_Encrypted.read()

    with open("./Winnow_Round_" + str(i) + "/Alice_Winnow-" + str(i) + "-Encrypted_File.txt", 'r') as Alice_Encrypted:
        Alice_Encrypted_Var = Alice_Encrypted.read()

    # with open("Bob_Sifted_File.txt", 'r') as Bob_Sifted:
    #     Bob_Sifted_Var = Bob_Sifted.read()
    #
    # with open("Alice_Sifted_File.txt", 'r') as Alice_Sifted:
    #     Alice_Sifted_Var = Alice_Sifted.read()

    with open("./Winnow_Round_" + str(i) + "/Alice_Permuted_" + str(i) + ".txt", 'r') as Bob_Sifted:
        Bob_Sifted_Var = Bob_Sifted.read()

    with open("./Winnow_Round_" + str(i) + "/Bob_Permuted_" + str(i) + ".txt", 'r') as Alice_Sifted:
        Alice_Sifted_Var = Alice_Sifted.read()

    print("Ali 1 : " + Alice_Sifted_Var)
    print("Bob 1 : " + Bob_Sifted_Var)
    Corrected_Bob_Sifted_Var = ""

    counter = -1
    Alice_Removal_Blocks = []
    for j in range(0, int(len(Alice_Encrypted_Var) / 4)):
        counter += 1
        Alice_Syndrome = ""
        Bob_Syndrome = ""
        for k in range(0, 4):
            Alice_Syndrome = Alice_Syndrome + Alice_Encrypted_Var[4 * j + k]
            Bob_Syndrome = Bob_Syndrome + Bob_Encrypted_Var[4 * j + k]

        resultant_syndrome = str((int(Alice_Syndrome[0]) + int(Bob_Syndrome[0])) % 2) + str(
            (int(Alice_Syndrome[1]) + int(Bob_Syndrome[1])) % 2) + str(
            (int(Alice_Syndrome[2]) + int(Bob_Syndrome[2])) % 2) + str(
            (int(Alice_Syndrome[3]) + int(Bob_Syndrome[3])) % 2)

        temp = ""
        for l in range(0, 7):
            temp = temp + Bob_Sifted_Var[(7 * j) + l]

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
            after_Removal_bits = new_Temp[2:3] + new_Temp[3 + 1:]
            Corrected_Bob_Sifted_Var = Corrected_Bob_Sifted_Var + after_Removal_bits

            # saving the values of those blocks in which Bob has removed the information leaking bits and now Alice will
            # also remove
            Alice_Removal_Blocks.append(counter)

    # Out of loop
    print("Bob 2 : " + Corrected_Bob_Sifted_Var)
    print("List : " + str(Alice_Removal_Blocks))

    with open("./Winnow_Round_" + str(i) + "/Bob_Winnow-" + str(i) + "_Final.txt", "w") as Final_Bob_Bits:
        Final_Bob_Bits.write(Corrected_Bob_Sifted_Var)

    with open("./Winnow_Round_" + str(i) + "/Removal_Block_file_" + str(i) + ".txt", 'wb') as Removal_bits:
        pickle.dump(Alice_Removal_Blocks, Removal_bits)

    # closing files
    Final_Bob_Bits.close()
    Bob_Encrypted.close()
    Alice_Encrypted.close()
    Bob_Sifted.close()
    Alice_Sifted.close()
    Removal_bits.close()

    #---------------------------------------------------Bob Decryption end of Round i----------------------------------



    #---------------------------------------------------Alice Decryption of Round i----------------------------------

    with open("./Winnow_Round_" + str(i) + "/Removal_Block_file_" + str(i) + ".txt", 'rb') as Removal_bits:
        Alice_Removal_Blocks = pickle.load(Removal_bits)
        Removal_bits.close()

    # with open("Alice_Sifted_File.txt", 'r') as Alice_Sifted:
    #     Unchanged_data = Alice_Sifted.read()
    #     Alice_Sifted.close()

    with open("./Winnow_Round_" + str(i) + "/Alice_Permuted_" + str(i) + ".txt", 'r') as Alice_Sifted:
        Unchanged_data = Alice_Sifted.read()
        Alice_Sifted.close()

    print("Before : " + Unchanged_data)

    Corrected_Alice_Bits = ""
    counter = 0
    list_counter = 0

    for j in range(int(len(Unchanged_data) / 7)):

        temp = ""
        for l in range(0, 7):
            temp = temp + Unchanged_data[(7 * j) + l]

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
    print("Removed Alice bits and Created the file 'NAMED = Alice_Winnow-" + str(i) + "_Final.txt'")

    with open("./Winnow_Round_" + str(i) + "/Alice_Winnow-" + str(i) + "_Final.txt", "w") as Final_Alice_Bits:
        Final_Alice_Bits.write(Corrected_Alice_Bits)

    Final_Alice_Bits.close()


    #---------------------------------------------------Alice Decryption End of Round i----------------------------------


