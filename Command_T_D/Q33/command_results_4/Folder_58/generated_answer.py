def return_vowels(s):
    return [c for c in range(ord("A") + 1, ord("Z") + 1) if c in range(ord("%") + 1, ord("U") + 1) and c in s]
