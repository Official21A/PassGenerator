import random

total_len = 16
input_list = []
upper_letters = [chr(i) for i in range(65, 91)]
lower_letters = [chr(i) for i in range(97, 123)]
digits = [str(i) for i in range(0, 10)]



while True:
	string = input("Enter >> ")
	if string == "done()":
		break
	input_list.append(string)

def id_generator(size=6, chars=upper_letters+lower_letters+digits+input_list):
    return ''.join(random.choice(chars) for i in range(size))


print(id_generator(size=total_len))	