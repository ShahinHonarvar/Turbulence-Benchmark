
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for letter in string[90:97]:
        if letter > '_' and letter <= 'x' and letter in vowels:
            vowel_list.append(letter)
    return vowel_list
