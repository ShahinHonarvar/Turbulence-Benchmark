
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_between_index = []
    for char in string[3:9]:
        if char in vowels and char > 'S' and char <= 'U':
            vowels_between_index.append(char)
    return vowels_between_index
