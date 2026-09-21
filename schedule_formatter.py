import csv, os.path as op, string, sys
from collections import UserDict
from datetime import datetime, timedelta

class SSI_Class(UserDict):

	def __str__(self):
		separator = '|'
		item = self.data
		ret_str = ''
		if item['Start Time'] != '':
			ret_str += '<i><u>'
			ret_str += f'{item['Weekday']} {item['Month']} {item['Day']} &ndash; '
			ret_str += f'{item['Start Time']} &ndash; {item['End Time']}'
			ret_str += '</u></i><br /><br />\n'
		if item['Title'] != '':
			if item['Location'] == '':				# special case for holidays, etc
				ret_str += f'{item['Title']}<br />\n'
			else:
				ret_str += f'<b>Title</b>: {item['Title']}<br />\n'
		if item['Speaker Type'] != '':
			speaker = item['Speaker']
			ret_str += f'<b>{item['Speaker Type']}</b>: '
			if separator in speaker:
				speakers = speaker.split(separator)
				ret_str += speakers[0]
				for speaker in speakers[1:]:
					ret_str += f', {speaker}'
				ret_str += '<br />\n'
			else:
				ret_str += f'{speaker}<br />\n'
		if item['Location'] != '':
			ret_str += f'<b>Location</b>: {item['Location']}<br />\n'
		if item['Description'] != '':
			ret_str += f'<b>Description</b>: {item['Description']}<br />\n'
		if item['Speaker Bio'] != '':
			bio = item['Speaker Bio']
			if separator in bio:
				ret_str += '<b>Bios</b>:<br />'
				bios = bio.split(separator)
				ret_str += f'{bios[0]}<br />\n'
				for bio in bios[1:]:
					ret_str += f'&mdash; <br />{bio}<br />'
			else:
				ret_str += f'<b>Bio</b>: {item['Speaker Bio']}<br />\n'

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

# for use as a Python script and in VS Code -- not used from Jupyter notebook
if __name__ == '__main__':
	if len(sys.argv) == 2:
		format_csv(sys.argv[1])
	else:
		print(usage_str)
