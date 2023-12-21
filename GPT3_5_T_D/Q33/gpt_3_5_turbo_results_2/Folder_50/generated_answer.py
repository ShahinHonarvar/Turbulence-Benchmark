
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for index in range(11, 53):
        if string[index] in vowels and string[index] > '+' and string[index] <= 'W':
            result.append(string[index])
    
    return result
