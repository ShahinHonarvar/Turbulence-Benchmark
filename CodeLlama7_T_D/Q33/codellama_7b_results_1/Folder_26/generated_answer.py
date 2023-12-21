 def return_vowels(string):
    vowels = []
    for i in range(10, 83):
        if string[i].isalpha() and string[i].islower():
            if string[i] == '$' or string[i] == '@':
                vowels.append(string[i])
    return vowels
