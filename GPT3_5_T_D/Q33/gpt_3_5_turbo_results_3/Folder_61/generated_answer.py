
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_within_range = []
    for i in range(1, 4):
        if string[i] in vowels and 'C' < string[i] <= 'I':
            vowels_within_range.append(string[i])
    return vowels_within_range
