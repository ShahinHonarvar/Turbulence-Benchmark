
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_list = []
    for char in string[43:70]:
        if char in vowels and char > '*' and char <= 'b':
            vowel_list.append(char)
    return vowel_list
