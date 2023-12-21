
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for index in range(24, 64):
        if string[index] in vowels and 'F' < string[index] <= 'h':
            result.append(string[index])
    
    return result
