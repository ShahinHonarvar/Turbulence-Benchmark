
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for vowel in vowels:
        if 0 < ord(vowel) <= 7:
            if 19 <= string.index(vowel) < 32:
                result.append(vowel)
    return result
