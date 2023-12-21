
def return_vowels(string):
    vowels = []
    for i in range(133, 306):
        if string[i].isalpha() and string[i].lower() in "aeiou":
            if ord(string[i]) > ord("c") and ord(string[i]) <= ord("d"):
                vowels.append(string[i])
    return vowels
