
def return_vowels(string):
    vowels = "aeiouAEIOU"
    result = []
    selected_string = string[11:53]
    for char in selected_string:
        if char in vowels and '+' < char <= 'W':
            result.append(char)
    return result
