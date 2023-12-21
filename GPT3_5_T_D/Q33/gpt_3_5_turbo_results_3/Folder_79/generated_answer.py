
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for letter in string[74:96]:
        if letter in vowels and letter > 'I' and letter <= 'X':
            result.append(letter)
            
    return result
