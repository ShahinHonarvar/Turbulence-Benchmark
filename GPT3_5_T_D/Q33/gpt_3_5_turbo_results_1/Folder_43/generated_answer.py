
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    for i in range(22, 82):
        if string[i] in vowels and string[i] > 'N' and string[i] <= 'o':
            vowels_in_range.append(string[i])
    return vowels_in_range
