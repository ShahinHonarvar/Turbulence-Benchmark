def return_vowels(s):
    return [x for x in range(71, 81, 1) if x in s and s[x] > 'A' and s[x] < 'U']
