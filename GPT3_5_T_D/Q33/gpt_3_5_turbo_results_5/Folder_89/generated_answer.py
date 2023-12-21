
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_between_50_and_51 = []
    for i in range(50, 51):
        if string[i] in vowels:
            if 'a' < string[i] <= 'v':
                vowels_between_50_and_51.append(string[i])
    
    return vowels_between_50_and_51
