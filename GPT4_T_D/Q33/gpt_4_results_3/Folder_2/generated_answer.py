
def return_vowels(string):
    vowels = []
    for i in range(170, 645):
        if i < len(string) and string[i] > 'E' and string[i] <= '~' and string[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(string[i])
    return vowels
