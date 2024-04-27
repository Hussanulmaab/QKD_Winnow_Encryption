 # creating the Sift File
with open("sifted_File.txt", 'w') as sifted:
  sifted.write(" ------------------------SIFTED FILE-------------------------\n")
  sifted.write("                 ALICE                    |                                 BOB\n")
  sifted.write(
    "__________________________________________|__________________________________________________________________\n")
  sifted.write(
    "                   |                      |               |     +                  |             x\n")
  sifted.write(
    "       BASE        |   Polarization       |     BASE      |    D0           D1     |      D2           D3\n")
  sifted.write(
    "___________________|______________________|_______________|________________________|_________________________\n")

sifted.close()

# Opening raw data file
with open("../Data_File.txt", 'r') as file:
    i = -1
    for line in file:
      i+=1
      if(i<=6):
        print(str(i) + line, end="")
      else:
        if (line[8] == line[50]):
          print(str(i) + " Valid Sift")
          # writing to the sift file
          with open("sifted_File.txt", 'a') as sifted:
            # Write content to the file
            sifted.write(line)
            sifted.close()
        elif (line[8] != line[50]):
          print(str(i) + " Invalid Sift")







