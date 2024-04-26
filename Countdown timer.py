import time
n = int(input("De cuantos segundos quieres que sea la cuenta atras: "))
while n != 0:
	print(n)
	time.sleep(1)
	n -= 1
print("La cuenta atras ya se ha acabado")