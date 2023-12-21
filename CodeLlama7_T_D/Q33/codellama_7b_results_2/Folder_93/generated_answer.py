
def return_vowels(string):
    vowels = []
    for i in range(54, 82):
        if string[i].isalpha() and string[i].lower() in "aeiou":
            if string[i] > "=" and string[i] <= "@":
                vowels.append(string[i])
    return vowels
