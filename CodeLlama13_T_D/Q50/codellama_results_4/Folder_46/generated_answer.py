
def if_contains_anagrams(my_list):
    return len([word for word in my_list if (len(word) >= 3 and word in "".join(my_list))]) >= 38
