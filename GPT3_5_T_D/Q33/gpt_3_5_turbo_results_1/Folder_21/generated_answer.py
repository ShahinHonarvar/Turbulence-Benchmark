
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in string[464:574]:
        if 'a' < char <= 'g' and char in vowels:
            result.append(char)
    
    return result
