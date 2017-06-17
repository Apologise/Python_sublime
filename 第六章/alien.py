alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points")
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

print("================")
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_language = {
	'jen'    : 'python' ,
	'sarah'  : 'c',
	'edward' : 'ruby',
	'phil'   :'python'
	
}

print("Sarah's favorite language is " + favorite_language['sarah'].title() + ".")
user_0 = {
	'username' : 'efermi',
	'first'    : 'enrico',
	'last'     : 'fermi',
}
for key, value in user_0.items():
	print('\nkey:' + key)
	print('Value:' + value)
for key in user_0.keys():
	print(key.title())

for name in sorted(favorite_language.keys()):
	print(name.title() + ", thank you for taking the poll")

print("The following languages have been mentioned:")
for language in favorite_language.values():
	print(language.title())

for language in set(favorite_language.values()):
	print(language.title())

alien_3 = {'color' : 'green', 'points' : 5}
alien_4 = {'color' : 'yellow', 'points' : 10}
alien_5 = {'color' : 'red', 'points' : 15}

aliens = [alien_3, alien_4, alien_5]
for alien in aliens:
	print(alien)

alens = []
for alien_number in range(30):
	new_alien = {'color' : 'green', 'points':5,'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print("==============")
print("Total number of aliens:" + str(len(aliens)))

pizza = {
	'crust' : 'thick',
	'toppings' : ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + '-crust pizza')

for toppings in pizza['toppings']:
	print("\t" + toppings)