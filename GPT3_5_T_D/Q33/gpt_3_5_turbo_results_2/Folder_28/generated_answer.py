
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for index in range(41, 50):
        if string[index] in vowels and 'W' < string[index] <= '[':
            result.append(string[index])
    
    return result
