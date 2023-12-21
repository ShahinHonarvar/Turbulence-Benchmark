
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(260, 322):
        if string[i] in vowels and string[i] > '%' and string[i] <= 'U':
            result.append(string[i])
    
    return result
