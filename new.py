def is_palindromic(number: int) -> bool:
	num_str = str(number)[::-1]
	if number == int(num_str):
		return True
	return False

if __name__ == '__main__':
	for i in range(100000, 1000000):
		if is_palindromic(i + 1):
			print(i + 1)