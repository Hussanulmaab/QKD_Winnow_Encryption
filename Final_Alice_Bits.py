with open("Alice_Sifted_File.txt", 'r') as Alice_Sifted:
  data = Alice_Sifted.read()

with open("Final_Alice_Bits_File.txt", "w") as Final_Alice_Bits:
    Final_Alice_Bits.write(data)

Alice_Sifted.close()
Final_Alice_Bits.close()