import random
a = int(input("Del 0 hasta que numero quieres que sea el juego: "))
random_number = random.randint(0, a)
while True:
	user_number = int(input("Introduce el numero que crees que es: "))
	if user_number == random_number:
		print("felicidades, has adividado el numero")
		break
	elif user_number < random_number:
		print("El numero secreto es mayor que el tuyo")
	elif user_number > random_number:
		print("El numero secreto es menor que le tuyo")
	else:
		print("Introduce un numero valido diferente de 0")