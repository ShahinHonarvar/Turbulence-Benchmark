
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for index in range(770, 852):
        if string[index].isalpha() and string[index].lower() in vowels and string[index] > 'B' and string[index] <= 'i':
            result.append(string[index])
    
    return result
