
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    if len(string) >= 76 and len(string) > 2:
        for i in range(70, 76):
            if string[i] > string[2] and string[i] <= ':':
                if string[i] in vowels:
                    result.append(string[i])
    
    return result
