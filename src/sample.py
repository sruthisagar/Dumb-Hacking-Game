
def append_fibonacci(integer_list):
	length=len(integer_list)
	if length<2:
		integer_list.append(1)
	else:
		integer_list.append(integer_list[-1]+integer_list[-2])

def fibonacci(max):

	if int(max) == 0:
		return []
	else:
		integer_list=[1,1]
	
	while (integer_list[-1]+integer_list[-2]) <=int(max):
		append_fibonacci(integer_list)

	return integer_list


def main():
	
	max=input('Enter a non-negative integer >')
	if max.isdecimal() or (max[0]=='-' and max[1:].isdecimal()):
		integer_list =  fibonacci(max)
		print('The Fibonacci series starts with: {}'.format(integer_list))
	else:
		print('{} is not a non-negative integer'.format(max))

main()