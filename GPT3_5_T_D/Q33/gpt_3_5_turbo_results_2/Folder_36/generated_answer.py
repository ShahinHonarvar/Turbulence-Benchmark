
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    
    if len(string) >= 949:
        for i in range(604, 949):
            if string[i] > 'N' and string[i] <= 'U' and string[i] in vowels:
                result.append(string[i])
    
    return result
