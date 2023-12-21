
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    results = []
    for character in string[3:9]:
        if character.lower() in vowels and 's' < character.lower() <= 'u':
            results.append(character)
    return results
