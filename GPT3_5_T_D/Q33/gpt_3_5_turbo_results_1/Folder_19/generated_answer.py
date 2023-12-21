
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
  
    for i in range(51, 77):
        if string[i] in vowels and string[i] > string[4] and string[i] <= '=':
            result.append(string[i])
    
    return result
