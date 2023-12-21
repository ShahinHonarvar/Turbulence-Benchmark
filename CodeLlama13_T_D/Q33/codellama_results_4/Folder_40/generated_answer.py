
def return_vowels(s):
    vowels = "aeiou"
    result = []
    for i in range(2, 7):
        if s[i].lower() in vowels and s[i] <= "d":
            result.append(s[i])
    return result
