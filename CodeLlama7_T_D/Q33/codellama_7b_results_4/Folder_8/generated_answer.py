 def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(64, 82):
        char = string[i]
        if char.isalpha() and char.lower() in vowels and char > 'P' and char <= 'z':
            result.append(char)
    return result
