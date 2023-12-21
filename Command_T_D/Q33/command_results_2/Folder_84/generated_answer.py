def return_vowels(s):
    return [c for c in range(ord('B') + 1, ord('i') + 1) if c in s and c.lower() in 'aeiouAEIOU']
