
import re

def palindromes_of_specific_lengths(s):
    substring = s[33:86]
    all_substrings = [substring[i: j] for i in range(len(substring)) for j in range(i + 1, len(substring) + 1)]
    palindrome_set = set()

    for sub in all_substrings:
        if 26 <= len(sub) <= 31:
            if sub.lower() == sub[::-1].lower():
                if re.match("^[A-Za-z]*$", sub):
                    palindrome_set.add(sub)

    return palindrome_set
