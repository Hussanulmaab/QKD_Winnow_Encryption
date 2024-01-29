import numpy as np

#Hamming (7,4) Winnow

# Breaking file data into blocks
f = open("Bob_Sifted_File.txt", "r")
data = f.read()

with open("Bob_Encrypted_File.txt", "w") as Bob_Encrypted:
    print("Bob Encryption created")
Bob_Encrypted.close()

global x_bits

def main():
  for i in range(int(len(data)/7)):
    block = ""
    for j in range(0, 7):
      block += data[(7*i) + j]
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


    temp_Synd_Vector = ""

    with open("Bob_Encrypted_File.txt", "a") as Bob_Encrypted:

      for row in range(len(H3_Syndrome_Cal_Matrix)):
        temp = 0
        for col in range(7):
          temp += H3_Syndrome_Cal_Matrix[row][col] * int(x_bits[col])
        temp = temp%2
        temp_Synd_Vector += '%s' % (temp)

      Synd_Vector = temp_Synd_Vector [::-1]

      Bob_Encrypted.write(Synd_Vector)

      print("Syndrome -- " + Synd_Vector)

    Bob_Encrypted.close()

main()