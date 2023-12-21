
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    for i in range(64, 82):
        if chr(i).lower() in vowels and chr(i) > 'P' and chr(i) <= 'z':
            vowels_in_range.append(chr(i))
    return vowels_in_range
