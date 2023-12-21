
def return_vowels(string):
    vowels = []
    for i in range(44, 95):
        if string[i].isalpha() and string[i].lower() in 'aeiou' and ord(string[i]) > 5:
            vowels.append(string[i])
    return vowels
