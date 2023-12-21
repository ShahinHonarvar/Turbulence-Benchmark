
def return_vowels(string):
    vowels = []
    for i in range(82, 90):
        if string[i].isalpha() and string[i].lower() in "aeiou" and string[i] > "T" and string[i] <= "b":
            vowels.append(string[i])
    return vowels
