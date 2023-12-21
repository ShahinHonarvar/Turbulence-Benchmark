
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    
    for i in range(133, 306):
        if string[i] in vowels and string[i] > c and string[i] <= d:
            result.append(string[i])
    
    return result
