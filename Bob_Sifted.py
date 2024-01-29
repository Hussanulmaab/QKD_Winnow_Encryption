with open("Bob_Sifted_File.txt", 'w') as Bob_Sifted:
  print("Bob Sifted Created")
Bob_Sifted.close()

with open("Bob_Sifted_File.txt", 'a') as Bob_Sifted:

  with open("sifted_File.txt", 'r') as Sifted:
    i = 0
    for line in Sifted:
      i+=1
      if(i<=6):
        continue
      else:
        if(line[50] == "+"):
          if(line[64] == "1"):
            Bob_Sifted.write("0")
          elif(line[71] == "1"):
            Bob_Sifted.write("1")
          elif(line[64] == "0" and line[71] == "0"):
            Bob_Sifted.write("0")
        elif(line[50] == "x"):
          if(line[93] == "1"):
            Bob_Sifted.write("0")
          elif(line[102] == "1"):
            Bob_Sifted.write("1")
          elif(line[93] == "0" and line[102] == "0"):
            Bob_Sifted.write("0")

Bob_Sifted.close()

with open("Bob_Sifted_File.txt", 'r') as file:
  data = file.read()
  print(len(data))
