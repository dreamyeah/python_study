from time import *
import re
text = '''2016-04-06 08:00:15.386  INFO 7427 --- [o-8183-exec-124] c.n.p.b.f.BusinessTaskStatisticsFacade   : executeRecorder, info: {start=1459900815366, aftersale=1459900815386, item=1459900815370, cancel=1459900815379, waitingDeliver=1459900815375}'''

def get_matched_time(text):
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    
    match = re.search(pattern, text)
    
    s = match.start()
    e = match.end()
    
    return text[s:e]


print strftime("%Y-%m-%d %H:%M:%S", localtime())

print get_matched_time(text) < strftime("%Y-%m-%d %H:%M:%S", localtime())