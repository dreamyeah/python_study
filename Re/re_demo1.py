import re


def match_time(text):
	pattern = [r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}']
    
	for p in pattern:
		if re.search(p, text):
			return True
		else:
			return False

def match_time1(text):
	pattern = [r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}']
    
	for p in pattern:
		print 'Looking for "%s" in "%s" ->' % (p, text),
    
		if re.search(p, text):
			print 'found a match!'
		else:
			print 'no match'
    
	print "-------------------------------"

def get_matched_time(text):
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    
    match = re.search(pattern, text)
    
    s = match.start()
    e = match.end()
    
    return text[s:e]

if __name__ == '__main__':

	text = '''2016-04-06 08:00:15.386  INFO 7427 --- [o-8183-exec-124] c.n.p.b.f.BusinessTaskStatisticsFacade   : executeRecorder, info: {start=1459900815366, aftersale=1459900815386, item=1459900815370, cancel=1459900815379, waitingDeliver=1459900815375}'''
	if match_time(text):
		print 'Match!'
	else:
		print 'No Match!'
	match_time1(text)

	print get_matched_time(text)



	source = 'geqinGyangsbsbsssssb'
	seach = 'geqingyanG'

	pattern = re.compile(seach, re.IGNORECASE)
	result = pattern.search(source)
	print result;

