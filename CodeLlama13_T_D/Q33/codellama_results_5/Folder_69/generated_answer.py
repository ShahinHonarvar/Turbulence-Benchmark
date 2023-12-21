
def return_vowels(string):
    vowels = []
    for i in range(641, 872):
        if string[i].lower() in "aeiou" and string[i] <= 'q':
            vowels.append(string[i])
    return vowels
