name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def makeDict(arr1, arr2):
	newDict= zip(arr1, arr2)
	print newDict
makeDict(name, favorite_animal)