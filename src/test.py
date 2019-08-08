import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import test.testReadWrite as ReadWrite

'''
This is your main testing script, this should call several other testing scripts on its own
'''
def main():
	ReadWrite.main()
	

if __name__ == '__main__':
	main()
