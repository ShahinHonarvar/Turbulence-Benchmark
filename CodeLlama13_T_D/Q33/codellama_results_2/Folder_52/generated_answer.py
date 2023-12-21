
def return_vowels(string):
    vowels = []
    for i in range(24, 68):
        if string[i].lower() in "aeiou" and string[i] <= "|":
            vowels.append(string[i])
    return vowels
