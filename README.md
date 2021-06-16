# buffer_overflow
This is a tool for generating payload and there are many c program on which you can test buffer overflow
please edit the PayloadGenerator.py file for using the payload generator script 
after editing it we have to use this script like shown here 
-#python PayloadGenerator.py | here it will be the c program 
ther is one more script named fuzzer.py it can be used for crashing a c program and also for finding the limits of a c program 
and there is one more file named as fuzzer.sh it will download a fuzzing tool which i personaly use the tool name is fuzza 
installation:-
git clone https://github.com/pavitra1129/buffer_overflow.git
cd buffer_overflow
echo we are all done!
example of PayloadGenerator.py:-
nano PayloadGenrator.py (i will edit it as my c program is)
python PayloadGenrator.py | format.c
# and boom we will get the root shell of the owner of the file 
# whoami
root
#
`
