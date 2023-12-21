
import re

def palindromes_of_specific_lengths(s):
    sub_string = s[11:94].lower()
    palindromes = set()
    for i in range(len(sub_string)):
        for j in range(i+34, min(i+55, len(sub_string)+1)):
            slice = sub_string[i:j]
            if slice == slice[::-1] and re.match(r'^[a-z]+$', slice):
                palindromes.add(slice)
    return palindromes
