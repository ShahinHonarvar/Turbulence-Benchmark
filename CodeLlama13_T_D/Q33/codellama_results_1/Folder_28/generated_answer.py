
def return_vowels(string):
    vowels = []
    for i in range(41, 50):
        if string[i].isalpha() and string[i].lower() not in "aeiou" and string[i] > "w":
            vowels.append(string[i])
    return vowels
