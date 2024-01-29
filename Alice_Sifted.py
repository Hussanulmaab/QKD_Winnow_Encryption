with open("Alice_Sifted_File.txt", 'w') as Alice_Sifted:
  print("Alice Sifted Created")
Alice_Sifted.close()

with open("Alice_Sifted_File.txt", 'a') as Alice_Sifted:

  with open("sifted_File.txt", 'r') as Sifted:
    i = 0
    for line in Sifted:
      i+=1
      if(i<=6):
        continue
      else:
        if(line[28] == "H"):
          Alice_Sifted.write("0")
        elif(line[28] == "V"):
          Alice_Sifted.write("1")
        elif(line[28] == "D"):
          Alice_Sifted.write("0")
        elif(line[28] == "A"):
          Alice_Sifted.write("1")

Alice_Sifted.close()

with open("Alice_Sifted_File.txt", 'r') as file:
  data = file.read()
  print(len(data))