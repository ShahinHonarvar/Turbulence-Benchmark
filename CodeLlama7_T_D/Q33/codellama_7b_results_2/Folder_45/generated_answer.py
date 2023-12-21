 def return_vowels(string):
    vowels = []
    for i in range(43, 70):
        if string[i].isalpha() and string[i] in 'aeiou' and string[i] > '*' and string[i] <= 'b':
            vowels.append(string[i])
    return vowels
