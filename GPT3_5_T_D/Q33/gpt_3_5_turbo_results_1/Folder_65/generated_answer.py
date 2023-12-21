
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[71:88]:
        if char.isdigit() and int(char) > 9 and char.upper() in vowels:
            result.append(char)
    
    return result
