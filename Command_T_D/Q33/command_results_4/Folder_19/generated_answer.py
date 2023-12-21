def return_vowels(s):
    return [x for x in range(51, 77) if s[x-1] > 4 and x <= len(s)]
