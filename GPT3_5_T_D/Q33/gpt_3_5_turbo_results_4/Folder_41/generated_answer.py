
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    
    for i in range(71, 81):
        if string[i] > '>' and string[i] <= 'U' and string[i] in vowels:
            vowels_in_range.append(string[i])

    return vowels_in_range
