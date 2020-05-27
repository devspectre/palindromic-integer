def is_palindromic(number: int) -> bool:
	num_str = str(number)[::-1]
	if number == int(num_str):
		return True
	return False

if __name__ == '__main__':

	max_value = 0
	for i in range(100000, 1000000):
		if is_palindromic(i):
			max_value = i

	print(max_value)