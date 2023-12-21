
import re

def palindrome_of_length_at_least_n(string):
    palindrome_set = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i+22, len(string)+1):
            palindrome = string[i:j]
            if palindrome == palindrome[::-1] and re.match("^[a-zA-Z]+$", palindrome):
                palindrome_set.add(palindrome)
    return palindrome_set
