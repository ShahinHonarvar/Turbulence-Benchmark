
def return_vowels(my_string):
    vowels = []
    for char in my_string[328:455]:
        if char.isalpha() and char.lower() in "aeiou":
            vowels.append(char)
    return vowels
