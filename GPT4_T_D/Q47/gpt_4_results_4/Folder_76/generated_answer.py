
import re

def palindromes_of_specific_lengths(strng):
    strng = strng[101:293]
    palindromes = set()
    for i in range(len(strng)):
        for j in range(i+154, min(i+183, len(strng)+1)):
            if strng[i:j] == strng[i:j][::-1]:
                cleaned = re.sub("[^a-zA-Z]+", "", strng[i:j])
                if len(cleaned) == len(strng[i:j]) and len(cleaned) >= 154 and len(cleaned) <= 182:
                    palindromes.add(cleaned.lower())
    return palindromes
