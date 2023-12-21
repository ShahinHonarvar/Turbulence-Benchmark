import re
def palindrome_of_length_at_least_n(s):
    return {p for p in pal(s) if len(p)>=48 and p[::-1]==p}
