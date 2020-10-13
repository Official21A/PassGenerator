import random

input_list = []
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
				size-=1
				continue

		password.append(random.choice(chars))
		size-=1
							
	return ''.join(password)


def main():
	global input_list
	while True:
		string = input("Enter >> ")
		if string == "done()":
			break
		input_list.append(string)

	print(password_get())	


if __name__ == "__main__":
	main()	