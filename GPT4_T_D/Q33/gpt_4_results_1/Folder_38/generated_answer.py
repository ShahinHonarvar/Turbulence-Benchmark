
def return_vowels(string):
    vowels_list = []
    substring = string[17:65]
    for character in substring:
        if 'U' < character <= '{' and character.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels_list.append(character)
    return vowels_list
