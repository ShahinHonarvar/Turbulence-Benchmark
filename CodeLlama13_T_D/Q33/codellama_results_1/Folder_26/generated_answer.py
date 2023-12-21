
def return_vowels(s):
    vowels = []
    for i in range(10, 82):
        if s[i].lower() in 'aeiou' and s[i] > '$' and s[i] <= '@':
            vowels.append(s[i])
    return vowels
