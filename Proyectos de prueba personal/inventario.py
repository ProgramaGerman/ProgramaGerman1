def fact(X):
	if (X==0):
		return 1
	else:
		return X * fact(X - 1)

var = int(input("Indique un numero:"))
resultado = fact(var)

print(resultado)
print()