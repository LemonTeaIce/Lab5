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
