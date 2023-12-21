
import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = re.sub('[^A-Za-z]', '', string).lower()
    for i in range(len(string) - 92):
        for j in range(93, len(string) - i + 1):
            sub_str = string[i:i+j]
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    return palindromes
