import re
def palindromes_between_indices(s):
    return re.findall(r"((?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[@#$%&*])(?=.*?[!<>?/])(?=.*?[ \t])".upper(), s[3:-9], flags=re.I)
