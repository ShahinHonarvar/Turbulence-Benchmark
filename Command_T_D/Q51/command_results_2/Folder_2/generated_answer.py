import re
def if_contains_anagrams(str_list):
    return sum(re.fullmatch(r'(?=([A-Z]\d){2})([A-Z]\d){3}\1', s.lower()) for s in str_list) <= 81
