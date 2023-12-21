
import re

def palindromes_of_specific_lengths(s):
    s = re.sub('[^a-zA-Z]', '', s[23:78]).lower()
    palindromes = set()

    for l in range(13, 41):
        for i in range(len(s) - l + 1):
            substr = s[i:i+l]
            if substr == substr[::-1]:
                palindromes.add(substr)

    return palindromes
