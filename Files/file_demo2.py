import re
from time import *
def search_keyword_in_file(filename,keyword,start_time,end_time):
	match_list = ['']
	with open(filename) as ff:
		for line in ff.xreadlines():
			pre_line_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
			line_time = get_matched_time(line)
			# if line_time not null
			if line_time:
				#save pre line time before line not contains time;
				#if the first line containes time it's ok;
				#if first line in file not contains time,search result will ...
				pre_line_time = line_time
				match_list.apmatch_line_by_time(line,start_time,end_time,line_time)
			else:
				match_line_by_time(line,start_time,end_time,pre_line_time)

def match_line_by_time(line,start_time,end_time,line_time,):

					#start_time not null and end_time not null
				if start_time and end_time:
					if start_time > end_time:
						raise Exception("start_time larger than end_time!")
					if line_time >= start_time and line_time <= end_time:
						match_keyword(line,keyword)
				#start_time not null and end_time is null
				elif start_time and not end_time:
					current_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
					if line_time >= start_time and start_time <= current_time:
						match_keyword(line,keyword)

				#start_time is null and end_time not null
				elif not start_time and end_time:
					if line_time <= end_time:
						match_keyword(line,keyword)

				#start_time is null and end_time is null
				else:
					current_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
					if line_time <= current_time:
						match_keyword(line,keyword)

def match_keyword2(text,keyword):
	seach = keyword
	result = re.search(seach,text,re.IGNORECASE)
	if result:
		print text
		print '---------------------------------'
		return True
	else:
		return False

def match_keyword(text,keyword):
	seach = keyword
	pattern = re.compile(seach, re.IGNORECASE)
	result = pattern.search(text)
	if result:
		print text
		return True
	else:
		return False

def match_keyword1(text,keyword):
	if keyword in text or keyword.lower() in text or keyword.upper() in text or keyword.capitalize() in text:
		print text
		print '---------------------------------'	


def get_matched_time(text):
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    
    if re.search(pattern, text):
		match = re.search(pattern, text)
		return match.group()

def get_matched_time1(text):
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    
    if re.search(pattern, text):
		match = re.search(pattern, text)
		s = match.start()
		e = match.end()
		return text[s:e]
if __name__ == '__main__':
	# search_keyword_in_file("..//Example//catalina_2016-04-05.log","ThreadPoolExecutor")

	filename = "..//Example//catalina_2016-04-05.log"
	keyword = "error"
	start_time = "2016-04-05 08:00:14"
	end_time = "2016-04-05 18:00:14"
	search_keyword_in_file(filename,keyword,start_time,end_time)