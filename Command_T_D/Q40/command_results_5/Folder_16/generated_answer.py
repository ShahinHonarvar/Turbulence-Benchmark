import re
def return_n_smallest_chars(s):
    #group by character, count the number of times each character appears
    return sorted(re.findall("[A-z]", s), key=lambda x: ord(x))[:64]
