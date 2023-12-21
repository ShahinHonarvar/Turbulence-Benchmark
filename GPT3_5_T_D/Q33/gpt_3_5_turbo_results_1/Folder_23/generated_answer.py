
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    vowels_in_range = []
    for index in range(56, 96):
        character = string[index]
        if character in vowels and character > '&' and character <= 'T':
            vowels_in_range.append(character)
    return vowels_in_range
