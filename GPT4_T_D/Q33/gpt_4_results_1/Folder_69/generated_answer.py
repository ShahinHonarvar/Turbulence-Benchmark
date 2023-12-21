
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    specified_range = s[641:872]
    return_list = []
    for char in specified_range:
        if char > '>' and char <= 'q' and char in vowels:
            return_list.append(char)
    return return_list
