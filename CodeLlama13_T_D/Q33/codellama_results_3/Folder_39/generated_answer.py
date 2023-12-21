
def return_vowels(s):
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    for i in range(32, 97):
        if s[i] in vowels and s[i].lower() < "q":
            result.append(s[i])
    return result
