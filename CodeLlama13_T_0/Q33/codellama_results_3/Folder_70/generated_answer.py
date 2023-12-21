
def return_vowels(string):
    vowels = []
    for i in range(171, 402):
        if string[i].isalpha() and string[i].lower() in "aeiou":
            vowels.append(string[i])
    return vowels
