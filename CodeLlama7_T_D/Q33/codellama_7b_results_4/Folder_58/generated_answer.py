
def return_vowels(string):
    vowels = []
    for i in range(260, 322):
        if string[i].isalpha() and string[i].lower() in "aeiou":
            if (len(string) > i + 1 and string[i + 1] == "%") or len(string) <= i + 1:
                vowels.append(string[i])
    return vowels
