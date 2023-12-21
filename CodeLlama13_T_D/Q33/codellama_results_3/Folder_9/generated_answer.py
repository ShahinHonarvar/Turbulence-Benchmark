
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    indices = range(13, 35)
    result = []
    for i in indices:
        if string[i] in vowels and ord(string[i]) > 8 and ord(string[i]) <= ord("F"):
            result.append(string[i])
    return result
