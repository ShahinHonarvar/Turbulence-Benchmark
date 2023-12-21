
def return_vowels(string):
    vowels = []
    for i in range(32, 97):
        if string[i].isalpha() and string[i].lower() in "aeiou" and string[i] > "q":
            vowels.append(string[i])
    return vowels
