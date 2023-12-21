
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []

    for index in range(51, 77):
        if string[index] in vowels:
            if string[index] > string[4] and string[index] <= '=':
                vowel_list.append(string[index])

    return vowel_list
