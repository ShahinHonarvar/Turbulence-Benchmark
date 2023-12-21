
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    results = []
    for index in range(142, 145):
        if index < len(string):
            char = string[index]
            if char in vowels and char > string[4] and char <= 'o':
                results.append(char)
    return results
