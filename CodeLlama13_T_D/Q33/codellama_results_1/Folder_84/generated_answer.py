
def return_vowels(string):
    vowels = []
    for i in range(770, 852):
        if string[i].lower() in "aeiou" and string[i] > 'b' and string[i] <= 'i':
            vowels.append(string[i])
    return vowels
