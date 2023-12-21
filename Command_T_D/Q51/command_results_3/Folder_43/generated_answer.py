def if_contains_anagrams(s):
    return not (s.count(set(s).intersection(set("aeiou")).upper()) > 3)
