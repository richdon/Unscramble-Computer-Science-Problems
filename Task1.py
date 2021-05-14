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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

"""
Worst-Case: O(n^2)

"""
def distinct_numbers(texts, calls):
    unique_nums = set()
    
    for call in calls:
        for num in call:
            if len(num) == 13 or len(num) == 11:
                unique_nums.add(num)
                
    
    for txt in texts:
        for num in txt:
            if len(num) == 11:
                unique_nums.add(num)
    
    print(f"There are {len(unique_nums)} different numbers in the records")
    
    
    
distinct_numbers(texts, calls)