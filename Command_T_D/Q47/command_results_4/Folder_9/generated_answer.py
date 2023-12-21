def palindromes_of_specific_lengths(text):
    letters = set(map(str.lower, range(ord('a'), ord('z') + 1)))
    return set(s for s in text[0:300].split() if s[::-1] in text[0:300] and len(s) in range(50, 61)) & letters
