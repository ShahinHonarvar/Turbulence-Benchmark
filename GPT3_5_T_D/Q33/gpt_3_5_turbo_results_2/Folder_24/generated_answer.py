
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    
    for i in range(23, 57):
        if string[i] in vowels and string[i] > string[0] and string[i] <= "d":
            result.append(string[i])
    
    return result
