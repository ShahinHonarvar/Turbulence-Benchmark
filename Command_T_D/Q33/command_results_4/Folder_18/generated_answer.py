def return_vowels(s):
    vowels = [i for i in range(528, 606) if s[i] in 'AEIOU']
    return [s[i] for i in vowels if s[i] > 'M' and s[i] <= 'X']
