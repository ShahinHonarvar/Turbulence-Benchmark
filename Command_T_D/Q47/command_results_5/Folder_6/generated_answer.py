import re
def palindromes_of_specific_lengths(string):
    return set(re.findall(r'[a-z]+\w{40,47}', string[45:-3]))
