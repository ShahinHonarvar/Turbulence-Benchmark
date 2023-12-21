def return_vowels(s):
    vowels = [c for c in range(27, 57) if c in s and c > 'o' and c <= 'w']
    return vowels
