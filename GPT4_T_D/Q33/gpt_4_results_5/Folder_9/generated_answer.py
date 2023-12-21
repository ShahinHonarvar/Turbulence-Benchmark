
def return_vowels(string):
    vowels = "aeiouAEIOU"
    result = []
    for char in string[13:35]:
        if char in vowels and "8" < char <= "F":
            result.append(char)
    return result
