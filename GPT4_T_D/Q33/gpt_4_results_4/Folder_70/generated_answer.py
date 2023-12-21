
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for i in string[171:402]:
        if i in vowels and 'I' < i <= 'k':
            result.append(i)
    if not result:
        return []
    return result
