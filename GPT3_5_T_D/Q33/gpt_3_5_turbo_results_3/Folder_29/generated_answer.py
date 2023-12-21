
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    vowels_between = []
    
    for index in range(19, 20):
        if string[index] in vowels and string[index] > '<' and string[index] <= 'p':
            vowels_between.append(string[index])
    
    return vowels_between
