
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    for char in string[60:99]:
        if char in vowels and 'j' < char <= 'n':
            vowels_in_range.append(char)
    return vowels_in_range
