def return_vowels(s):
    return [i for i in range(1, 7) if s[i] in "AEIOU" and s[i] > "F" and s[i] <= "j"]
