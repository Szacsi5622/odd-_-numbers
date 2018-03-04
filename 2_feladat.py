
letter = []

words = input("Your words: ")
w1 = words.lower()
letter.append(w1)
print(letter)
firstletter = letter[0][0]
print (firstletter)

characters = []
for a in letter:
	for x in a:
		characters.append(x)
firstDb = characters.count(firstletter)
print (firstDb)



def rotate(txt, key):
	def cipher(i, low=range(97,123), upper=range(65,91)):
		if i in low or i in upper:
			s = 65 if i in upper else 97
			i = (i - s + key) % 26 + s
		return chr(i)
	return ''.join([cipher(ord(s)) for s in txt])

print(rotate(characters, firstDb))

"""
def caesar(plaintext,shift):

	alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",
	"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

	#Create our substitution dictionary
	dic={}
	for i in range(0,len(alphabet)):
		dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]

	#Convert each letter of plaintext to the corrsponding
	#encrypted letter in our dictionary creating the cryptext
	ciphertext=""
	for l in plaintext.lower():
		if l in dic:
			l=dic[l]
		ciphertext+=l

	return ciphertext
print ("Cipertext:",caesar(w1,vmi))
"""