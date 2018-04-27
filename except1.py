def main():
	try:
	  for line in readfile('file1.doc'):
	    print(line.strip())
	except IOError as e:
	  print('can not read error',e)
	except ValueError as e:
	  print('Wrong file extension',e)

def readfile(filename):
	if filename.endswith('.txt'):
		fh=open(filename)
		return fh.readlines()
	else: raise ValueError('Filename must end with .txt')
     





main()
