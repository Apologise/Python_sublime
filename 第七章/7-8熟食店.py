sandwich_orders = ['sandwich1', 'sandwich2', 'sandwich3', 'pastrami', 'pastrami', 'pastrami','pastrami']

finished_sandwiches = []
while sandwich_orders:
	print('I made your tuna sandwich')
	finished = sandwich_orders.pop()
	finished_sandwiches.append(finished)

print(finished_sandwiches)
print(sandwich_orders)
while 'pastrami' in finished_sandwiches:
	finished_sandwiches.remove('pastrami')
print(finished_sandwiches)