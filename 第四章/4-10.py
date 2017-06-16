list1 = [1,2,3,4,5,6,7,8,9]
print("The first items in the list are:")
for value in list1[0:3]:
	print(value)

print("The mid items in the list are")
for value in list1[3:6]:
	print(value, end = " ")

print("The last three items in the list are:")
for value in list1[-3:]:
	print(value,)
