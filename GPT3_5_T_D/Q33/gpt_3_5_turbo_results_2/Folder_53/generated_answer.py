
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    
    for i in range(27, 57):
        if string[i] in vowels and string[i] > "o" and string[i] <= "w":
            result.append(string[i])
    
    return result
