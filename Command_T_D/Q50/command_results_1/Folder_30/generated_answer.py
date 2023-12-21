def if_contains_anagrams(text):
    return len(set(map(str.lower, (a for a in text if len(a) >= 3 and a == b[::-1]))) >= 78
