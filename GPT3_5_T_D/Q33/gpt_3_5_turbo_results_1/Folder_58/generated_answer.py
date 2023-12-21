
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    for index in range(260, 322):
        if string[index] in vowels and string[index] > '%' and string[index] <= 'U':
            vowels_in_range.append(string[index])
    return vowels_in_range
