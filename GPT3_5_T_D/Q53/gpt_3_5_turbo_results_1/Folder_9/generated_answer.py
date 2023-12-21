
import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindrome_set = set()
    for i in range(len(string) - 94):
        if re.match(r'^[a-z]+$', string[i:i+95]) and string[i:i+95] == string[i:i+95][::-1]:
            palindrome_set.add(string[i:i+95])
    return palindrome_set
