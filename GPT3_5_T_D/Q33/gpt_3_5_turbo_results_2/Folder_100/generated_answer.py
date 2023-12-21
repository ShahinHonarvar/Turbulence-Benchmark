
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    
    for char in string[23:75]:
        if 'L' < char <= 'd' and char.lower() in vowels:
            vowels_in_range.append(char)
            
    return vowels_in_range
