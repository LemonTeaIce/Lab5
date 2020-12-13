import re

ayat = "i'm genius awesome"
ayat1 = "semua orang penting"

check = re.search("^i.*awesome$",ayat)

if check:
	print("sama")
else:
	print("Tak sama")

check = re.search("^i.awesome$",ayat1)

if check:
	print("sama")
else:
	print("Tak sama")
