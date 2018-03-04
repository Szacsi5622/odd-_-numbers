import random
class Card:
	COLOURS = ('Hearts', 'Clubs', 'Spades', 'Diamonds')
	VALUES = ('none', 'Ace','2','3','4','5','6','7','8','9','10', 'Jack','Queen','King')
	
	def __init__(self, colours = 0, values = 0 ):
		self.colours = colours
		self.values = values
	def __str__(self):
		return '{0} {1}'.format(Card.VALUES[self.values],Card.COLOURS[self.colours])
		
	def __cmp__(self, other):
		t1 = self.colours, self.values
		t2 = other.colours, other.values
		return cmp(t1, t2)

	def __lt__(self, other):
		if self.colours < other.colours:
			return True
		elif self.colours > other.colours:
			return False
		else:
			return self.values < other.values


class Deck(object):
    
	def __init__(self):
		self.cards = []
		for colours in range(4):
			for values in range(1, 14):
				card = Card(colours, values)
				self.cards.append(card)

	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)

	def add_card(self, card):
       
		self.cards.append(card)

	def pop_card(self, i=-1):
        
		return self.cards.pop(i)

	def shuffle(self):
       
		random.shuffle(self.cards)

	def sort(self):
        
		self.cards.sort()

	def move_cards(self, hand, num):
        
		for i in range(num):
			hand.add_card(self.pop_card())


class Hand(Deck):
    
	def __init__(self, label=''):
		self.label = label
		self.cards = []

def find_defining_class(obj, meth_name):
    
	for ty in type(obj).mro():
		if meth_name in ty.__dict__:
			return ty
	return None


if __name__ == '__main__':
	deck = Deck()
	deck.shuffle()
	db = input("How many cards do you want? ")
	hand = Hand()
	#print(find_defining_class(hand, 'shuffle'))

	deck.move_cards(hand, int(db))
	hand.sort()
	print("First cards are: \n")
	print(hand)
	print("----------------------")
	#hand.pop_card(0)
	print("the top card is : ",hand.pop_card(0))
	print("----------------------")
	print("The remains are:\n")
	print(hand)