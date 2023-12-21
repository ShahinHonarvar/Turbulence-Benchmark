 def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(1, len(string)):
        if string[i] in vowels and string[i] > string[i-1] and string[i] <= 'I':
            result.append(string[i])
    return result
