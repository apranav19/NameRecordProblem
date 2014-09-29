from sys import stdin
import re
'''
	A NameRecorder class that maintains a database of people
'''
class NameRecorder:
	def __init__(self):
		self.records = {}

	'''
		Given a line of text, insert into the db
	'''
	def insert_record(self, raw_line):
		data = raw_line.split(':')
		name, ssn = data[0], int(data[1])

		if ',' in data[0]:
			name = self.normalize_name(name)

		if ssn in self.records:
			self.records[ssn].add(name)
		else:
			self.records[ssn] = set()
			self.records[ssn].add(name)

	'''
		Given a name of the format: <Last Name>, <First Name> <Middle>
		or <Last Name>, <First Name>,
		we normalize it to the format <First Name> <Middle> <Last Name>
	'''
	def normalize_name(self, name):
		name_components = re.split(r'[,\s]+', name)
		if len(name_components) == 2:
			return (' ').join(name_components[::-1])
		else:
			return (' ').join(name_components[1:] + name_components[0:1])

	'''
		Simply print out the entries of the db
	'''
	def print_records(self):
		for ssn, names in self.records.items():
			print 'SSN: ' + str(ssn) + '\n' + str(names)

if __name__ == '__main__':
	
	input_file = open('data.txt', 'r')
	name_recorder = NameRecorder()

	for line in input_file:
		name_recorder.insert_record(line.rstrip())

	name_recorder.print_records()

