
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for index in range(17, 65):
        if string[index] in vowels and string[index] > 'U' and string[index] <= '{':
            result.append(string[index])
    
    return result
