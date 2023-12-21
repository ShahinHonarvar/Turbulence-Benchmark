
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(10, 83):
        char = string[i].lower()
        if char in vowels and char > '%' and char <= 'e':
            result.append(char)
    
    return result
