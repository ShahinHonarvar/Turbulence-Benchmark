 
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    
    for i in range(171, 402):
        if string[i] in vowels and string[i] > 'I' and string[i] <= 'k':
            vowels_in_range.append(string[i])
            
    return vowels_in_range
