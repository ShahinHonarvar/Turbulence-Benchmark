import re
def palindromes_of_specific_lengths(s):
    # Write your code here
    return re.findall(r'[a-z]{12,}\d{5,}[a-z]{12}', s[12:-2])
