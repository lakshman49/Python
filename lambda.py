def add(x,y):
	return x+y


def minus(x,y):
	return x-y
result= lambda x,y : (x+y,x-y)

print(add(15,5))
print(minus(15,5))
print(result(15,5))