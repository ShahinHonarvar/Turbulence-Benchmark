
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_within_range = []
    for index in range(464, 574):
        if string[index] in vowels and 'a' < string[index] <= 'g':
            vowels_within_range.append(string[index])
    return vowels_within_range
