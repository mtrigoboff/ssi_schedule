import csv, os.path as op, string, sys
from collections import UserDict

class SSI_Class(UserDict):

	def __str__(self):
		item = self.data
		ret_str = ''
		if item['Title'] != '':
			ret_str += '<b>Title</b>: ' + item['Title'] + '<br />\n'
		if item['HostType'] != '':
			ret_str += '<b>' + item['HostType'] + '</b>: ' + item['Host'] + '<br />\n'
		if item['Location'] != '':
			ret_str += '<b>Location</b>: ' + item['Location'] + '<br />\n'
		if item['Description'] != '':
			ret_str += '<b>Class Description</b>: ' + item['Description'] + '<br />\n'
		if item['Bio'] != '':
			ret_str += '<b>Bio</b>: ' + item['Bio'] + '<br />\n'

		return ret_str + '<br />\n'

'''
			if len(item._bios) == 1:
				ret_str += '<br /><b>Bio</b>:' + ' ' + item._bios[0] + '<br />\n'
			else:
				ret_str += '<br /><b>Bios</b>:\n'
				for bio in item._bios:
					ret_str += '<br />' + bio + '<br />\n'
'''

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
