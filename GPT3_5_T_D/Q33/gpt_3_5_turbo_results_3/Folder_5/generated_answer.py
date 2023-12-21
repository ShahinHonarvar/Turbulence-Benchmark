
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for i in range(44, 95):
        if i > 5 and string[i] < '<' and string[i] in vowels:
            vowel_list.append(string[i])
    return vowel_list
