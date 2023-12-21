
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    
    for index in range(163, 771):
        char = string[index]
        if ':' < char <= 'E' and char in vowels:
            result.append(char)
    
    return result
