
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_within_range = []
    for char in string[50:77]:
        if char in vowels and '#' < char <= 'r':
            vowels_within_range.append(char)
    return vowels_within_range
