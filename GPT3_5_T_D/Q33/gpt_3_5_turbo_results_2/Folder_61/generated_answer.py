
def return_vowels(string):
    vowel_list = []
    for char in string[1:4]:
        if char > 'C' and char <= 'I' and char.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowel_list.append(char)
    return vowel_list
