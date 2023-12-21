
import re
def palindromes_of_specific_lengths(s):
    s = s[12:57].lower()
    valid_chars = re.sub('[^a-z]', '', s)
    palindromes = set()
    for i in range(len(valid_chars)):
        for j in range(i + 20, min(i + 22, len(valid_chars) + 1)):
            substring = valid_chars[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
