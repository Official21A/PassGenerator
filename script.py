import random

input_list = []
keys = []
upper_letters = [chr(i) for i in range(65, 91)]
lower_letters = [chr(i) for i in range(97, 123)]
digits = [str(i) for i in range(0, 10)]


def password_get(size=10, chars=upper_letters+lower_letters+digits):
	global input_listm

	password = []

	while size:
		stat = random.randint(0, 200)
		if stat % 3 == 0 and input_list:
			string = random.choice(input_list)
			if not string in password:
				password.append(string)
				keys.append(string)
				size-=1
				continue

		password.append(random.choice(chars))
		size-=1
							
	return ''.join(password)


def result(password, keys):
	print("Result ::")
	print(f">> Your password: {password}")	
	print(f"	:> consists {len(keys)} of your inputs ", end="")
	print(f"with total {len(password)} characters.")
	if keys:
		print(f"	>: keys in use {keys}")


def main():
	global input_list, keys
	while True:
		string = input("Enter >> ")
		if string == "done()":
			break
		input_list.append(string)

	result(password_get(), keys)	


if __name__ == "__main__":
	main()	