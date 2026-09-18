import csv, os.path as op, string, sys
from collections import UserDict

class SSI_Class(UserDict):

	def __str__(self):
		ret_str = ''
		if self.data._title is not None:
			ret_str += '<b>Title</b>: ' + self.data._title + '<br />\n'
		if self.data._presenter_title is not None:
			ret_str += '<b>' + self.data._presenter_title[:-1] + '</b>: ' + self.data._presenters + '<br />\n'
		if self.data._location is not None:
			ret_str += '<b>Location</b>: ' + self.data._location + '<br />\n'
		if self.data._description is not None:
			ret_str += '<b>Class Description</b>: ' + self.data._description + '<br />\n'
		if self.data._extra:
			ret_str += '<br />\n'
			if len(self.data._extra) == 1:
				colon = self.data._extra[0].find(':')
				if colon != -1:
					title = self.data._extra[0][0:colon]
					rest_of_line = self.data._extra[0][colon + 1:].strip()
					ret_str += '<b>' + title + '</b>: ' + rest_of_line
				else:
					ret_str += self.data._extra[0]
			else:
				for extra in self.data._extra:
					ret_str += extra
			ret_str += '<br />\n'
		if self.data._bios:
			if len(self.data._bios) == 1:
				ret_str += '<br /><b>Bio</b>:' + ' ' + self.data._bios[0] + '<br />\n'
			else:
				ret_str += '<br /><b>Bios</b>:\n'
				for bio in self.data._bios:
					ret_str += '<br />' + bio + '<br />\n'
		return ret_str + '<br />\n'

class SSI_ClassList:

	def __init__(self):
		self._class_list = []

	def add(self, ssi_class):
		self._class_list.append(ssi_class)

	def __str__(self):
		ret_str = ''
		for ssi_class in self._class_list:
			if type(ssi_class) is str:						# 'week of ...' or date and time of a class
				if ssi_class.lower().split(' ', 1)[0] == 'week':
					ret_str += '<b><u>' + ssi_class + '</u></b><br /><br />\n'
				else:
					ret_str += '<i><u>' + ssi_class + '</u></i><br /><br />\n'
			else:
				ret_str += str(ssi_class)
			ret_str += '\n'
		return ret_str

'''
# dictionary for routing a line to the appropriate SSI_Class attribute
ssi_class_attrs = {
	'title:':		SSI_Class.set_title,
	'host:':		SSI_Class.set_presenters,
	'moderator:':	SSI_Class.set_presenters,
	'presenter:':	SSI_Class.set_presenters,
	'presenters:':	SSI_Class.set_presenters,
	'organizer:':	SSI_Class.set_presenters,
	'tour':			SSI_Class.set_presenters,
	'location:':	SSI_Class.set_location,
	'class':		SSI_Class.set_description,
	'extra:':		SSI_Class.add_extra,
	'bio:':			SSI_Class.add_bio,
	'bios:':		SSI_Class.add_bio,
}
'''

def format_csv(csv_file_name):

	classes = []
	html_file_name = op.splitext(csv_file_name)[0] + '.html'
	html_file = open(html_file_name, mode='w', encoding='utf-8')
	csv_file = open(csv_file_name, mode='r', newline='', encoding='utf-8-sig')
	csv_reader = csv.DictReader(csv_file)
	for row in csv_reader:
		if row.get('Date') != '':
			classes.append(SSI_Class(row))
			print(SSI_Class(row), file=html_file)

	print(len(classes))
	csv_file.close()
	html_file.close()

usage_str = 'usage: schedule_formatter input_file'

# for use as a Python script -- not used from Jupyter notebook
if __name__ == '__main__':
	if len(sys.argv) == 2:
		format_csv(sys.argv[1])
	else:
		print(usage_str)
