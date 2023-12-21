
import re

def palindrome_of_length_n(string):
    string = re.sub("[^a-zA-Z]+", "", string).lower()
    palindromes = set()
    length = len(string)

    for i in range(length - 77):
        substring = string[i:i+78]
        if substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
