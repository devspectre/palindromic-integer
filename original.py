def is_palindromic(n):
	# temp variable
	tmp = n
	# we get reversed number from orginal number given
	reverse = 0
	# loop from the end to get reversed number
	while tmp > 0:
		# get the last digit
	    dig = tmp % 10
	    # attach current digit to the end of current reverse variable
	    reverse = reverse * 10 + dig
	    # get remaining forehead number excluding last digit for next step
	    tmp = tmp // 10
	if n == reverse:
	    return True
	else:
	    return False

if __name__ == '__main__':

	maxValue = 0

	for i in range(100000, 1000000):
		if is_palindromic(i):
			maxValue = i

	if maxValue != 0:
		print(maxValue)
	else:
		print("No Palindromic!")
