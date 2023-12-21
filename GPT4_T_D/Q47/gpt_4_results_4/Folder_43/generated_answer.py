
import re

def palindromes_of_specific_lengths(s):
    s = s[41:90]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = set()
    for i in range(len(s)):
        for end in range(i, len(s)):
            chunk = s[i:end + 1]
            if 23 <= len(chunk) <= 38:
                if chunk == chunk[::-1]:
                    palindromes.add(chunk)
    return palindromes
