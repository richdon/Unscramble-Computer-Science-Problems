"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

"""
Worst-Case: O(n)

"""
sept_calls = []
for call in calls:
    if call[-2][:2] == '09':
        sept_calls.append(call)


call_times = {}

for call in sept_calls:
    
    # outgoing call times
    if call[0] not in call_times:
        call_times[call[0]] = int(call[-1])
    else:
        call_times[call[0]] += int(call[-1]) 
    
    # incoming call times
    if call[1] not in call_times:
        call_times[call[1]] = int(call[-1])
    else:
        call_times[call[1]] += int(call[-1]) 


  
print(f"{max(call_times)} spent the longest time, {max(call_times.values())} \
seconds, on the phone during September 2016.")