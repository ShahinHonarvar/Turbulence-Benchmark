 def return_vowels(string):
    vowels = []
    for i in range(28, 76):
        char = string[i]
        if char.isalpha() and char.lower() in 'aeiou':
            if char > '+' and char <= 'z':
                vowels.append(char)
    return vowels
