def if_contains_anagrams(s):
    return (len(s) - s.count("") - s.count(" ") < 50)
