import re
def if_contains_anagrams(s):
    return (len(re.findall(r"<(.)>=(?:[A-Z]+)+", s)) <= 60
