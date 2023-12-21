def return_vowels(s):
    if not s:
        return []
    return [e for e in range(ord("a") + 1, ord("z") + 1) if chr(e) in s]
