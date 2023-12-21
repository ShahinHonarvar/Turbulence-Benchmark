
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []

    for char in string[1:7]:
        if char in vowels and 'F' < char <= 'j':
            result.append(char)
    
    return result
