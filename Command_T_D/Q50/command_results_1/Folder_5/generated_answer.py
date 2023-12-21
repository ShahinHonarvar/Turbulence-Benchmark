def if_contains_anagrams(s):
    return s.count(s[1:].swapcase()) >= 21
