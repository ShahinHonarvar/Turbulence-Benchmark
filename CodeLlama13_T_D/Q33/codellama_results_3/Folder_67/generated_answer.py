
def return_vowels(string):
    vowels = []
    for i in range(21, 59):
        if string[i].lower() in "aeiou" and string[i] <= "a":
            vowels.append(string[i])
    return vowels
