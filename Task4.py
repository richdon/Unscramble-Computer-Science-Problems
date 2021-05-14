"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

"""
Worst-Case: O(n log n)

"""
all_txt_nums = set()

for txt in texts:
    all_txt_nums.add(txt[0])
    all_txt_nums.add(txt[1])
    
out_num = {num[0] for num in calls}

incoming = {num[1] for num in calls}  

telemarketers = set()

for num in out_num:
    if num not in all_txt_nums and num not in incoming:
        telemarketers.add(num)
    
print("These numbers could be telemarketers: ")
[print(num) for num in sorted(telemarketers)]