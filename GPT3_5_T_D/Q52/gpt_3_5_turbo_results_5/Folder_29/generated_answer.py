
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    palindromes = set()
    for i in range(len(string) - 18):
        substring = string[i: i + 19]
        if substring[::-1].lower() == substring.lower():
            palindromes.add(substring)
    return palindromes
