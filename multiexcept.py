def main():
	try:
	  f=open('file1.txt')
	  x=1/1
	except FileNotFoundError as e:
	  print('FileNotFoundError')
	except ZeroDivisionError as e:
	  print('A problem occured',e)
	except :
	  print('Unknow error')
	
	print('No errors all DOne')



main()