
def return_vowels(s):
    vowels = []
    english_vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in s[31:37]:
        if i in english_vowels and ';' < i <= 't':
            vowels.append(i)

    return vowels
