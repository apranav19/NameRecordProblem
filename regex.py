import re

def regex(name):
	'''
			Regular Expression to Parse Names of the following types

			First Middle Last
			First M. Last
			F. M. Last
			First Last
			First
	'''
	patterns = [r'[\w]+\s[\w]+\s[\w]+',
				r'[\w]+\s[A-Z]{1}\.\s[\w]+',
				r'[A-Z]{1}\.\s[A-Z]{1}\.\s[\w]+',
				r'[\w]+\s[\w]+',
				r'[\w]+']

	first_middle_last = re.compile(patterns[0])
	first_m_last = re.compile(patterns[1])
	f_m_last = re.compile(patterns[2])
	first_last = re.compile(patterns[3])
	first = re.compile(patterns[4])

	if first_middle_last.match(name):
		return 0
	if first_m_last.match(name):
		return 1
	if f_m_last.match(name):
		return 2
	if first_last.match(name):
		return 3
	if first.match(name):
		return 4

if __name__ =='__main__':
	print(regex("John Mason"))

