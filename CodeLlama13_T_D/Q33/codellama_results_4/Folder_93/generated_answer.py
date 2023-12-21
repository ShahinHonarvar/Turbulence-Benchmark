
def return_vowels(s):
    vowels = []
    for i in range(54, 82):
        if s[i].lower() in "aeiou":
            vowels.append(s[i])
    return vowels
