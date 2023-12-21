import re
def if_contains_anagrams(s):
    return (sum( (1 for a in s if b in s and a != b)
                    for b in s if a == b and len(a) >= 3) <= 81 )
