
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sub_string = string[13:35]
    result = [ch for ch in sub_string if ch in vowels and '8' < ch <= 'F']
    return result
