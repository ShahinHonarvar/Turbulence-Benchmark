
def return_vowels(str_arg):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sub_str = str_arg[20:43]
    vowels_list = [i for i in sub_str if i in vowels and '5' < i <= 'M']
    return vowels_list
