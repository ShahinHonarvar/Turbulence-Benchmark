
def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    
    for i in range(41, 50):
        if i < len(str): 
            if str[i] in vowels and 'W' < str[i] <= '[': 
                result.append(str[i]) 

    return result
