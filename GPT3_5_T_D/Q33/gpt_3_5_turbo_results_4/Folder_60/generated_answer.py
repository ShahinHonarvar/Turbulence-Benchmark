
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for index in range(24, 59):
        if index < len(string):
            letter = string[index]
            if letter in vowels and letter > 'N' and letter <= 'U':
                vowel_list.append(letter)
    return vowel_list
