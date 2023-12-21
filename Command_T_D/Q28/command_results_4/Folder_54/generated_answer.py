
import re

def return_nth_smallest_ascii(s):
    for i in range(12,87):
        match = re.search(r'[a-z]', s[i:])
        if match:
            return match.group()
