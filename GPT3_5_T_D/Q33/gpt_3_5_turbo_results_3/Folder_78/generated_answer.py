
def return_vowels(string):
    vowels = []
    for i in range(46, 90):
        if string[i] > "@" and string[i] <= "[":
            if string[i] in 'aeiouAEIOU':
                vowels.append(string[i])
    return vowels
