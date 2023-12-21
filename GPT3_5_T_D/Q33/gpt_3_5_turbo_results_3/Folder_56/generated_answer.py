
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for letter in string[15:86]:
        if letter in vowels and ord('@') < ord(letter) <= ord('~'):
            vowel_list.append(letter)
    return vowel_list
