import marshal, base64, zlib, sys

stri = input("File ~> ")
pswd = input("Password ~> ")
arr = []
key = len(pswd)

f = open(stri, "r")
fr = f.read()
f.close()

def encrypt(text):
	for char in text:
		arr.append(chr(ord(char)+key))
	res = "".join(arr)
	return res

enc_bytes = marshal.dumps(encrypt(fr))
lib = zlib.compress(enc_bytes)
result = base64.b64encode(lib).decode("ascii")
print("Result : "+result)

izin = input("Want to save this?[y/n]:")
if izin == "y" or izin == "Y":
	fw = open("encrypted.txt", "w")
	fw.write("Encrypted By ZenxDev\n\n"+result)
	print("Save to dummy.txt")
elif izin == "n" or izin == "N":
	sys.exit()
else:
	sys.exit()