import random, string, hashlib

def generate(length = 12):
	if length < 4:
		raise ValueError("La contraseña debe ser mayor a 4 Caracteres")

	capital_letters = string.ascii_uppercase
	small_letters = string.ascii_lowercase
	numbers = string.digits
	special_characters = "!@#$%&*"

	password = [
		random.choice(capital_letters),
		random.choice(small_letters),
		random.choice(numbers),
		random.choice(special_characters),
	]

	all_characters = capital_letters + small_letters + numbers + special_characters
	password += random.choices(all_characters, k=length - 4)

	random.shuffle(password)
	return "".join(password)

def encrypt(password):
	hashobj = hashlib.sha256(password.encode('utf-8'))
	return hashobj.hexdigest()





def main():
	try:
		length = int(input("Ingrese la longitud de la contraseña: "))
		generated_password = generate(length)
		encrypted_password = encrypt(generated_password)

		print(f"La contraseña generada es: {generated_password}")
		print(f"La contraseña encriptada es: {encrypted_password}")
	except ValueError as e:
		print(e)

if __name__ == "__main__":
	main()
