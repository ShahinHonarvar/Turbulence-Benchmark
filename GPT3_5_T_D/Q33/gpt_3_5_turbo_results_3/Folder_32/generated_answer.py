
def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    
    for char in text[45:76]:
        if 'b' < char <= 'z' and char.lower() in vowels:
            result.append(char)
    
    return result
