
def return_vowels(string):
    vowels = []
    for letter in string[20:34]:
        if letter > 'U' and letter <= 'i':
            if letter in 'aeiouAEIOU':
                vowels.append(letter)
    return vowels
