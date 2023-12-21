def if_contains_anagrams(s):
    return s.count(set(s).intersection(s, key=lambda i: i[0].lower() == i[1].lower())) >= 6
