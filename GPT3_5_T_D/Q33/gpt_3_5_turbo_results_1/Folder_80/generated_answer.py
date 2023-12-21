
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for index in range(85, 99):
        if string[index] > '/' and string[index] <= 'n' and string[index] in vowels:
            result.append(string[index])

    return result
