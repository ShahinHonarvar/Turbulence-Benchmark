
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    vowels_within_range = []
    for i in range(20, 41):
        if string[i] in vowels and string[i] > 'K' and string[i] <= 'Z':
            vowels_within_range.append(string[i])
    return vowels_within_range
