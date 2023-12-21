
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for index in range(24, 64):
        if string[index] in vowels and string[index] > 'F' and string[index] <= 'h':
            vowel_list.append(string[index])
    return vowel_list
