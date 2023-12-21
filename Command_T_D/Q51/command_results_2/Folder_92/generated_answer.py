def if_contains_anagrams(s):
    return not (s.lower() | {x.lower() for x in s if x.lower() in s.lower()}).count(s.lower()) > 34
