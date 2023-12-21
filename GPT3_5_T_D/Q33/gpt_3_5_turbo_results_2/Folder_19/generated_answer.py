
def return_vowels(string):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    vowels = []
    for i in range(51, 77):
        if i > 4 and i <= ord('=') and string[i].lower() in vowel_list:
            vowels.append(string[i])
    return vowels
