import re
def palindromes_of_specific_lengths(str):
    return set(re.findall(r'(?<=.)(?!\1)[a-z]+(?=\1)', str[1:9], flags=re.I))
