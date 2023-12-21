def if_contains_anagrams(text):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    return len(text) <= 318 and len(text) >= 3 and len(set(a.lower() for a in text)) == len(letters)
