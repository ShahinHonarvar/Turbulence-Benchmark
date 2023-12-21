
import re

def palindromes_of_specific_lengths(input_string):
    substr = input_string[100:296]
    substr = re.sub('[^a-zA-Z]', '', substr)
    substr = substr.lower()
    palindromes = set()

    for length in range(136, 161):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    
    return palindromes
