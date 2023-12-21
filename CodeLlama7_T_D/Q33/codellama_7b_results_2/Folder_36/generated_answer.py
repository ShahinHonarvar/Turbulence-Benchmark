
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 604
    end_index = 949
    result = []
    for i in range(start_index, end_index + 1):
        char = string[i]
        if char.islower() and char.isalpha():
            if char in vowels:
                result.append(char)
    return result
