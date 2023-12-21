
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for index in range(43, 70):
        letter = string[index]
        if letter in vowels and '*' < letter <= 'b':
            result.append(letter)
    
    return result
