
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    
    for index in range(29, 31):
        if string[index] in vowels and 'a' < string[index] <= 'f':
            vowels_in_range.append(string[index])
    
    return vowels_in_range
