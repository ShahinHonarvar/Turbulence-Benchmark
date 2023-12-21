def return_vowels(s):
    try:
        return [c for c in s[8:9]]
    except (IndexError, KeyError):
        return []
