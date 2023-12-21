
import re

def palindromes_of_specific_lengths(string):
    substr = string[16:95]
    substr = re.sub('[^a-zA-Z]', '', substr)
    substr = substr.lower()
    palindromes = set()
    for length in range(39, 53):
        for i in range(len(substr) - length + 1):
            if substr[i:i+length] == substr[i:i+length][::-1]:
                palindromes.add(substr[i:i+length])
    return palindromes
