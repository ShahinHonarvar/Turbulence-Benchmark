
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    result = []
    for i in range(495, 837):
        if string[i] in vowels and string[i] > "B" and string[i] <= "t":
            result.append(string[i])
    return result
