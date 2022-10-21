import string
import random
import sys


letters = string.ascii_lowercase
if len(sys.argv) < 2:
	print("Please provide a file as input!")
	sys.exit()
f = open(sys.argv[1], 'r')
s = f.read()
o = []
z = []
while s:
    o.append(s[:400])
    s = s[400:]

for line in o:
	rand = ''.join(random.choice(letters) for i in range(8))
	z.append(rand)
	print("$" + rand + " = \"" + line + "\"")

tempstring = "$all = "
count = 0
for line in z:
	if count == 0:
		tempstring += "$" + line 
	else:
		tempstring += "+" + "$" + line 
	count+=1
print(tempstring)
