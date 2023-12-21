 def return_vowels(string):
    vowels = []
    for i in range(32, 97):
        if string[i] > 'Q' and string[i] <= 'z':
            vowels.append(string[i])
    return vowels
