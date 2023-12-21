
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    if len(string) >= 76:
        for i in range(70, 76):
            if string[i] in vowels and string[i] > string[2] and string[i] <= ':':
                result.append(string[i])
    
    return result
