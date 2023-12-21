
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for i in range(47, 61):
        if string[i].lower() in vowels and string[i].lower() > '9' and string[i].lower() <= 'o':
            vowel_list.append(string[i])
    return vowel_list
