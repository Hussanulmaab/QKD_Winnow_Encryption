import numpy as np

f = open("../Algorithm Check/Making Erreneous Files/My_Alice_Sifted.txt", "r")
data = f.read()

with open("Alice_Winnow-1-Encrypted_File.txt", "w") as Alice_Encrypted:
    print("Alice Encryption created")
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


Alice_Encrypting_Function()
