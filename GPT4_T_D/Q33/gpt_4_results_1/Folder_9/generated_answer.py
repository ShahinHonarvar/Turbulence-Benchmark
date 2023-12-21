
def return_vowels(string):
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_between_indexes = [character for character in string[13:35] if character in vowel_list and ('8' < character <= 'F')]
    return vowels_between_indexes
