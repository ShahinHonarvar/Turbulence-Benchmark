
def return_vowels(s):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    result = []

    substring = s[133:306]
    
    for letter in substring:
        if letter in vowels and 'c' < letter <= 'd':
            result.append(letter)
            
    return result
