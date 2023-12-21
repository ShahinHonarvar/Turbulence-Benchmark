
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for i in range(770, 852):
        if string[i].isalpha() and string[i].islower() and string[i] > 'B' and string[i] <= 'i' and string[i] in vowels:
            result.append(string[i])
    
    return result
