
def return_vowels(s):
    vowels = []
    english_vowels = 'aeiouAEIOU'
    for char in s[11:53]:
        if (ord(char) > ord('+')) and (ord(char) <= ord('W')) and (char in english_vowels):
            vowels.append(char)
    return vowels
