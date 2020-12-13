<<<<<<< HEAD
import re

print("Genius")
teka = [123,'abu', 34.92]

print(teka[1])
print(str(123))
print(type(b'8.32'))

file = open('ayat1.txt', 'r')
ayat = file.read()

file = open('ayat2.txt','r')
ayat1 = file.read()

if re.search("^nama.*sholahudin$",ayat):
	print("sama")
else:
	print("Tak sama")
=======

nama = input("Tolong masukkan nama anda: ")
print(nama + str(type(nama)))
print("hello world")

panggilan = ['azfar','aspalela','zayn']
teka = ['zack', 423, 0.32]

print(panggilan)
print(panggilan[1])

file = open('name.txt','r')

print(file.read())


if nama[1] == 'zayn':
	print('hai kacak')
else:
	print('kau bukan zayn')

print(type(teka[1]))
>>>>>>> commit lab5 fro server
