
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = []
    for i in range(37, 57):
        if string[i] in vowels and string[i] > '*' and string[i] <= 'P':
            output.append(string[i])
    return output
