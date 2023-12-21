
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_list = []
    for char in string[24:59]:
        if char in vowels and char > 'N' and char <= 'U':
            vowels_list.append(char)
    return vowels_list
