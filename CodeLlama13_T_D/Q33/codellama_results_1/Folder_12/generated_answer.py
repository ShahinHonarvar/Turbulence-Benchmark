
def return_vowels(string):
    vowels = []
    for i in range(13, 37):
        if string[i].isalpha() and string[i].lower() in "aeiou" and string[i] <= "}" and string[i] > "z":
            vowels.append(string[i])
    return vowels
