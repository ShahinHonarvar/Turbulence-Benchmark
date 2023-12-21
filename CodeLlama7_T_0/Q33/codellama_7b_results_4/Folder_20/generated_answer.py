
def return_vowels(string):
    vowels = []
    for i in range(59, 61):
        if string[i].isalpha() and string[i].lower() in "aeiou" and string[i] > "+":
            if string[i] <= "h":
                vowels.append(string[i])
    return vowels
