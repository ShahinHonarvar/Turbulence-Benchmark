
import re

def palindromes_of_specific_lengths(string):
    string = string[17:96].lower()
    palindrome_set = set()
    for i in range(len(string)):
        for j in range(i+13, min(len(string)+1, i+50)):
            sub_string = string[i:j]
            if sub_string == sub_string[::-1] and re.match('^[a-z]*$', sub_string):
                palindrome_set.add(sub_string)
    return palindrome_set
