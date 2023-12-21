
def return_vowels(string):
    vowels = []
    for i in range(13, 37):
        if "Z" < string[i] <= "}":
            if string[i] in "aeiouAEIOU":
                vowels.append(string[i])
    return vowels
