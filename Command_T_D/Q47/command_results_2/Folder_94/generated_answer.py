import re
def palindromes_of_specific_lengths(text):
    return re.findall(r'(?i)(?=([a-z]+?){45,51}(?i)[a-z]+)', text[40:-4])
