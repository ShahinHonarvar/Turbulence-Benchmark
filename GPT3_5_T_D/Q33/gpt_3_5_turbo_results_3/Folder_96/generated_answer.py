
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    vowels_in_range = []
    for i in range(77, 84):
        if string[i] in vowels and ord('(') < ord(string[i]) <= ord('G'):
            vowels_in_range.append(string[i])
    return vowels_in_range
