
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    
    for index in range(171, 402):
        if string[index] in vowels and string[index] > 'i' and string[index] <= 'k':
            vowels_in_range.append(string[index])
    
    return vowels_in_range
