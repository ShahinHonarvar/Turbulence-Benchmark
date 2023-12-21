
import re

def palindromes_of_specific_lengths(string):
    string = string[15:73]
    string = re.sub('[^a-zA-Z]', '', string).lower()
    palindromes = set()
    for length in range(19, 56):
        for i in range(len(string) - length + 1):
            substring = string[i:i+length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
