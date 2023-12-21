def return_vowels(string):
    return [c for c in range(65, 70, 1) if c in string and c > string[0] and c <= string[1]]
