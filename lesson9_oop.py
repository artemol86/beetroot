class Animal:
	paws = 4
	tail = True

	def __init__(self, name):
		self.name = name

	def voice(self):
		print('Bzzz!!!')

class Cat(Animal):
	def voice(self):
		print('MEOW!!!')

class Kitten(Cat):
	def __init__(self, name, age):
		super().__init__(name)
		self.age = age

class Dog(Animal):
	def voice(self):
		print('Bark! My name is {}'.format(self.name))

class CatDog(Cat, Dog):
	pass

cat_dog = CatDog('CatDog')
cat_dog.voice = some_voice
print(cat_dog.paws)
print(cat_dog.name)
cat_dog = voice()

"""
my_dog = Dog('India')
my_cat = Cat('Yoda')
animal = Animal('Bug')
bug = Animal('Bug')
kitty = Kitten('Kitty', '1 month')


print(type(my_cat))
print(isinstance(my_cat, Animal))
print(issubclass(Cat, Animal))
print(kitty.paws)
print(kitty.paws)
print(kitty.paws)
print(kitty.paws)
"""