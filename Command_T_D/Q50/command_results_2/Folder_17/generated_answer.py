import re
def if_contains_anagrams(s):
    return len(s) >= 97 and sum(1 for i in range(97) for j in range(97) if re.match(r"^([a-z]{3})([a-z]{3})$", (s[i], s[j]), flags=re.I)) >= 2
