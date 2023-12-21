
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for index in range(260, 322):
        letter = string[index]
        if letter in vowels and letter > '%' and letter <= 'U':
            result.append(letter)
    
    return result
