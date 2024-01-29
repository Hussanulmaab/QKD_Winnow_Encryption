# Hamming (7,4)

# Breaking file data into blocks
f = open("Alice.txt", "r")
data = f.read()

global x_bits
global encoded_bits
global induced_error_encoded
global corrected_bits

def main():
  for i in range(int(len(data)/4)):
    block = ""
    for j in range(0, 4):
      block += data[(4*i) + j]
    print("Block " + '%s' % i + " :: " + block)
    global x_bits
    x_bits = block
    global encoded_bits
    print("Input Bits :: " + '%s' % x_bits)

    # Calculating Parity
    calculate_parity()

    # Inducing Error
    induce_error()

    #Correcting Error
    Error_Correction()
    print("Corrected Bits : " + corrected_bits)


# Calculating Parity of Blocks
def calculate_parity():
  p1 = (int(x_bits[3]) + int(x_bits[2]) + int(x_bits[0])) %2
  p2 = (int(x_bits[3]) + int(x_bits[1]) + int(x_bits[0])) %2
  p3 = (int(x_bits[2]) + int(x_bits[1]) + int(x_bits[0])) %2

  global encoded_bits
  encoded_bits = x_bits[0] + x_bits[1] + x_bits[2] + '%s' % p3 + x_bits[3] + '%s' % p2 + '%s' % p1
  print("Encoded Bits :: " + '%s' % encoded_bits)
  # encoded_bits = encoded_bits[::-1]


# Inducing Error in the Blocks
def induce_error():
  global encoded_bits
  global induced_error_encoded

  from random import randint
  random_index = randint(0, 6)

  if(encoded_bits[random_index] == "0"):
    induced_error_encoded = encoded_bits[:random_index] + "1" + encoded_bits[random_index+1:]
    print("Error Induced Bits :: " + induced_error_encoded)

  if(encoded_bits[random_index] == "1"):
    induced_error_encoded = encoded_bits[:random_index] + "0" + encoded_bits[random_index+1:]
    print("Error Induced Bits :: " + induced_error_encoded)


# Error Correction
def Error_Correction():

  # Syndrome Calculation
  global induced_error_encoded
  import numpy as np
  # H3_Syndrome_Cal_Matrix = [
  #           [1, 0, 1, 0, 1, 0, 1],
  #           [0, 1, 1, 0, 0, 1, 1],
  #           [0, 0, 0, 1, 1, 1, 1]
  #                                 ]


  # temp_Synd_Vector = ""

  # for row in range(len(H3_Syndrome_Cal_Matrix)):
  #   temp = 0
  #   for col in range(7):
  #     temp += H3_Syndrome_Cal_Matrix[row][col] * int(induced_error_encoded[col])

  #   temp = temp%2
  #   temp_Synd_Vector += '%s' % (temp)

  # Synd_Vector = temp_Synd_Vector [::-1]

  S1 = (int(induced_error_encoded[6]) + int(induced_error_encoded[4]) + int(induced_error_encoded[2])+ int(induced_error_encoded[0])) % 2
  S2 = (int(induced_error_encoded[5]) + int(induced_error_encoded[4]) + int(induced_error_encoded[1])+ int(induced_error_encoded[0])) % 2
  S3 = (int(induced_error_encoded[3]) + int(induced_error_encoded[2]) + int(induced_error_encoded[1])+ int(induced_error_encoded[0])) % 2

  Synd_Vector = '%s' % S3 + '%s' % S2 + '%s' % S1
  print("Syndrome" + Synd_Vector)

  # Correcting Error

  global corrected_bits
  if(Synd_Vector == "000"):
    corrected_bits = induced_error_encoded

  elif(Synd_Vector == "001"):
      if(induced_error_encoded[6] == "0"):
        corrected_bits = induced_error_encoded[:6] + "1" + encoded_bits[6+1:]
      elif(induced_error_encoded[6] == "1"):
        corrected_bits = induced_error_encoded[:6] + "0" + encoded_bits[6+1:]

  elif(Synd_Vector == "010"):
      if(induced_error_encoded[5] == "0"):
        corrected_bits = induced_error_encoded[:5] + "1" + encoded_bits[5+1:]
      elif(induced_error_encoded[5] == "1"):
        corrected_bits = induced_error_encoded[:5] + "0" + encoded_bits[5+1:]

  elif(Synd_Vector == "011"):
      if(induced_error_encoded[4] == "0"):
        corrected_bits = induced_error_encoded[:4] + "1" + encoded_bits[4+1:]
      elif(induced_error_encoded[4] == "1"):
        corrected_bits = induced_error_encoded[:4] + "0" + encoded_bits[4+1:]

  elif(Synd_Vector == "100"):
      if(induced_error_encoded[3] == "0"):
        corrected_bits = induced_error_encoded[:3] + "1" + encoded_bits[3+1:]
      elif(induced_error_encoded[3] == "1"):
        corrected_bits = induced_error_encoded[:3] + "0" + encoded_bits[3+1:]

  elif(Synd_Vector == "101"):
      if(induced_error_encoded[2] == "0"):
        corrected_bits = induced_error_encoded[:2] + "1" + encoded_bits[2+1:]
      elif(induced_error_encoded[2] == "1"):
        corrected_bits = induced_error_encoded[:2] + "0" + encoded_bits[2+1:]

  elif(Synd_Vector == "110"):
      if(induced_error_encoded[1] == "0"):
        corrected_bits = induced_error_encoded[:1] + "1" + encoded_bits[1+1:]
      elif(induced_error_encoded[1] == "1"):
        corrected_bits = induced_error_encoded[:1] + "0" + encoded_bits[1+1:]

  elif(Synd_Vector == "111"):
      if(induced_error_encoded[0] == "0"):
        corrected_bits = induced_error_encoded[:0] + "1" + encoded_bits[0+1:]
      elif(induced_error_encoded[0] == "1"):
        corrected_bits = induced_error_encoded[:0] + "0" + encoded_bits[0+1:]

  corrected_bits = corrected_bits[0] + corrected_bits[1] + corrected_bits[2] + corrected_bits[4]

main()