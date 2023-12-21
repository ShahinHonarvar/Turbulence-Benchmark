
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for index in range(13, 35):
        if 8 < index <= ord('F'):
            if string[index].lower() in vowels:
                result.append(string[index])
    
    return result
