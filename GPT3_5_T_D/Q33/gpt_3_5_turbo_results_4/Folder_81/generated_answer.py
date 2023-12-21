
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    for i in range(20, 43):
        if string[i] in vowels and string[i] > string[5] and string[i] <= 'M':
            vowels_in_range.append(string[i])
    return vowels_in_range
