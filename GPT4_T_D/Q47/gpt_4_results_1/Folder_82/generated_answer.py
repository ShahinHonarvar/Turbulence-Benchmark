
import re
def palindromes_of_specific_lengths(s):
    s = s[3:301]
    s = re.sub("[^a-zA-Z]*", "", s)
    s = s.lower()
    palindromes = set()

    for length in range(30, 301):
        for i in range(len(s)):
            if i + length > len(s):
                break
            substring = s[i:i+length]
            if substring == substring[::-1]:
                palindromes.add(substring)
                
    return palindromes
