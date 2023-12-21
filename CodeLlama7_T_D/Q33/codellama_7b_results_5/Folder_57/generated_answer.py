
def return_vowels(string):
    vowels = []
    for i in range(21, 23):
        if string[i].isalpha() and string[i].isupper():
            if ord(string[i]) > ord('-') and ord(string[i]) <= ord('n'):
                vowels.append(string[i])
    return vowels
