
def return_vowels(input_string):
    vowels = 'AEIOUaeiou'
    result = []
    for ch in input_string[170:645]:
        if ch in vowels and 'E' < ch <= '~':
            result.append(ch)
    return result
