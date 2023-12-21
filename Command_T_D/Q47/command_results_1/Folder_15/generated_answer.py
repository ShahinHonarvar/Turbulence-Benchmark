 
import re
def palindromes_of_specific_lengths(test_str):
    return re.findall(r'(?i)([a-z]+)(?i)[a-z]+'.replace('(i)',''), test_str[0:6])
