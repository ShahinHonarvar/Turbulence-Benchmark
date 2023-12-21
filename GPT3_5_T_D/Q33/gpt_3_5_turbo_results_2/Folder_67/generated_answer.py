
def return_vowels(string):
    vowels = 'aeiou'
    output = []
    for char in string[21:59]:
        if char > '/' and char <= 'a' and char.lower() in vowels:
            output.append(char)
    return output
