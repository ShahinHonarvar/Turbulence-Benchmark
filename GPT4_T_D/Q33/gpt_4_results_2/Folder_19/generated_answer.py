
def return_vowels(string):
    vowels = []
    sub_string = string[51:77]
    for char in sub_string:
        if 'a' <= char <= 'u' and char in 'aeiou':
            vowels.append(char)
    return vowels
