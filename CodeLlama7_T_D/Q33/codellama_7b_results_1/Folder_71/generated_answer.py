
def return_vowels(string):
    vowels = []
    for i in range(36, 57):
        if string[i] in "aeiou" and string[i] > "+":
            if string[i] <= "/":
                vowels.append(string[i])
    return vowels
