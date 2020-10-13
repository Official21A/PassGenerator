import random
import sys

input_list = []
keys = []
upper_letters = [chr(i) for i in range(65, 91)]
lower_letters = [chr(i) for i in range(97, 123)]
digits = [str(i) for i in range(0, 10)]


def password_get(size, chars=upper_letters+lower_letters+digits):
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
	print("\nResult ::")
	print(f">> Your password: {password}")	
	print(f"	:> consists {len(keys)} of your inputs ", end="")
	print(f"with total {len(password)} characters.")
	if keys:
		print(f"	>: keys in use {keys}")


def main(argv):
	global input_list, keys
	if len(argv) > 1:
		size = int(argv[1])
	else:
		size = 10	
	while True:
		string = input("Enter >> ")
		if string == "done()":
			break
		input_list.append(string)

	result(password_get(size), keys)	


if __name__ == "__main__":
	main(sys.argv)	