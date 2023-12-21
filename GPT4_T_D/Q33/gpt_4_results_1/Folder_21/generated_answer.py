
def return_vowels(s):
    vowels = ['e', 'i']
    subset_s = s[464:574]
    filtered_list = [x for x in subset_s if x in vowels]
    return filtered_list
