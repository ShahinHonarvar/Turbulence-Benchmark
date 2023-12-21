
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for vowel in vowels:
        if 'U' < vowel <= 'i' and 20 <= ord(vowel) < 34:
            vowel_list.append(vowel)
    return vowel_list
