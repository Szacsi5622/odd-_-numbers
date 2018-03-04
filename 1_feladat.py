numbers = list()
odds = []
for i in range(1,10):
	inputnumbers = int(input("Your numbers:"))
	numbers.append(inputnumbers)
try:
	nb = int(inputnumbers)
except ValueError:
	print ("Invalid number!")


def find_odds(numbers, odds):
	if len(numbers) ==0:
		return
	v = numbers.pop()
	if v%2==1:
		odds.append(v)
		
	find_odds(numbers, odds)

find_odds(numbers, odds)
print ("Odd numbers:", odds)

sm = sum(odds[0:len(odds)])
print("Sum of odds numbers: ", sm)

if len(odds) ==0:
	print("There is no odds numbers")
else:
	db=(len(odds))
	print ("Piece of odds numbers: ", db)
atlag = sm / db
print("Average of odds numbers:", float(atlag))