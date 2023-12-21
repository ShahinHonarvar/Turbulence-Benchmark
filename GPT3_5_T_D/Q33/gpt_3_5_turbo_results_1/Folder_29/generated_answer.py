
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []

    for i in range(19, 20):
        if string[i] in vowels and ord(string[i]) > ord('<') and ord(string[i]) <= ord('p'):
            vowels_in_range.append(string[i])

    return vowels_in_range
