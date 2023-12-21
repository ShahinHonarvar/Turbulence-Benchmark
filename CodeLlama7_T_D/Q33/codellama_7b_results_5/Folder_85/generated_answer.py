 def return_vowels(string):
    vowels = []
    for i in range(55, 65):
        if string[i].isalpha():
            if string[i].lower() == 'z':
                continue

            elif string[i].lower() <= 'w':
                vowels.append(string[i])
    return vowels
