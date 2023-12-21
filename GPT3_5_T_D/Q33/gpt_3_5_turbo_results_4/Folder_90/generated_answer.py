
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for index in range(142, 145):
        if index >= len(string):
            break
        elif string[index] > 'd' and string[index] <= 'o' and string[index] in vowels:
            result.append(string[index])
    
    return result
