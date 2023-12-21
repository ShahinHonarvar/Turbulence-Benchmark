
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 19, len(string) + 1):
            sub_string = string[i:j]
            sub_string = re.sub('[^a-z]', '', sub_string)
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes
