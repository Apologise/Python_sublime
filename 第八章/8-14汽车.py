def make_car(zhizaoshang, xinghao, **info):
	profile = {}
	profile['制造商'] = zhizaoshang
	profile['型号'] = xinghao
	for key, value in info.items():
		profile[key] = value
	return profile
car = make_car('宝马制造商','BMW10001', look = '漂亮', size = '非常大')
print(car)