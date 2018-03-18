from random import shuffle

def jumble(word):
    anargam = list(word)
    shuffle(anargam)
    return ''.join(anargam)

# map(function,data)
        # map creates a new list
        # 1st argument is the function that would be called for every item
        # 2nd argument is the list itself
words = ['beetroot', 'carrots', 'potatoes']
anargam = []

#normal / conventional way
for word in words:
    anargam.append(jumble(word))
print(anargam)

#using map ----- the best
sp = list(map(jumble,words))
print(sp)

#using comprehension
anargam = [jumble(word) for word in words]
print(anargam)

thirsty = 0
hungry = 1
if(thirsty):
	print("eat fries")
else:
	print("drink soda")