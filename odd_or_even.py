def par_o_impar(numero):
	if numero % 2 == 0:
		print("El numero {} es par".format(numero))
	else:
		print("El numero {} es impar".format(numero))

numero = int(input("Ingresa un numero entero: "))

print(par_o_impar(numero))