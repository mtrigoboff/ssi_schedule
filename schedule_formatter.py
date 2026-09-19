import csv, os.path as op, string, sys
from collections import UserDict

class SSI_Class(UserDict):

	def __str__(self):
		separator = '|'
		item = self.data
		ret_str = ''
		if item['Title'] != '':
			if item['Location'] != '':					# special case for holidays, etc
				ret_str += '<b>Title</b>: '
			ret_str += item['Title'] + '<br />\n'
		if item['HostType'] != '':
			host = item['Host']
			ret_str += '<b>' + item['HostType'] + '</b>: '
			if separator in host:
				hosts = host.split(separator)
				ret_str += hosts[0]
				for host in hosts[1:]:
					ret_str += ', ' + host
				ret_str += '<br />\n'
			else:
				ret_str += host + '<br />\n'
		if item['Location'] != '':
			ret_str += '<b>Location</b>: ' + item['Location'] + '<br />\n'
		if item['Description'] != '':
			ret_str += '<b>Description</b>: ' + item['Description'] + '<br />\n'
		if item['Bio'] != '':
			bio = item['Bio']
			if separator in bio:
				ret_str += '<b>Bios</b>:<br />'
				bios = bio.split(separator)
				ret_str += bios[0] + '<br />\n'
				for bio in bios[1:]:
					ret_str += '&mdash; <br />' + bio + '<br />'
			else:
				ret_str += '<b>Bio</b>: ' + item['Bio'] + '<br />\n'

		return ret_str + '<br />\n'

def format_csv(csv_file_name):

	html_file_name = op.splitext(csv_file_name)[0] + '.html'
	html_file = open(html_file_name, mode='w', encoding='utf-8')

	csv_file = open(csv_file_name, mode='r', newline='', encoding='utf-8-sig')
	csv_reader = csv.DictReader(csv_file)

	for row in csv_reader:
		if row.get('Date') != '':
			print(SSI_Class(row), file=html_file)

	csv_file.close()
	html_file.close()

usage_str = 'usage: schedule_formatter input_file'

# for use as a Python script -- not used from Jupyter notebook
if __name__ == '__main__':
	if len(sys.argv) == 2:
		format_csv(sys.argv[1])
	else:
		print(usage_str)
