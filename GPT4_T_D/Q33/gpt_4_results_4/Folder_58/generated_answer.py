
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return_vowels_list = []
    for char in string[260:322]:
        if char > '%' and char <= 'U' and char in vowels:
            return_vowels_list.append(char)
    return return_vowels_list
