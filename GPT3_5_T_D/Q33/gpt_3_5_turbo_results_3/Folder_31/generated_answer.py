
def return_vowels(string):
    vowels = []
    for char in string[65:70]:
        if '%' < char <= 'G':
            if char in 'AEIOUaeiou':
                vowels.append(char)
    return vowels
