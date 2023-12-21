
def return_vowels(my_string):
    vowels = []
    for char in my_string:
        if ord(char) >= 32 and ord(char) <= 97 and ord(char) > 81 and ord(char) <= 90:
            vowels.append(char)
    return vowels
