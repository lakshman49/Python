def main():

	try:
		fh=open('file2.txt')
	except IOError as e :
		print('can not found file:',e)
	for l in fh:print(l.strip())

main()