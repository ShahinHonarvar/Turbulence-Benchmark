
def return_vowels(string, c, d):
    vowels = []
    for i in range(133, 306):
        if string[i].isalpha() and string[i].lower() in "aeiou" and string[i] >= c and string[i] <= d:
            vowels.append(string[i])
    return vowels
