
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 54
    end_index = 82
    result = []

    for i in range(start_index, end_index):
        if string[i] > '=' and string[i] <= '@':
            if string[i].lower() in vowels:
                result.append(string[i])

    return result
