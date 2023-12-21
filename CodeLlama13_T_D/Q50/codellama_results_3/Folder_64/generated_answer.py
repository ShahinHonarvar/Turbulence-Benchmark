
def if_contains_anagrams(my_list):
    pairs = 0
    for i in range(len(my_list)):
        first_str = my_list[i].lower()
        for j in range(i+1, len(my_list)):
            second_str = my_list[j].lower()
            if len(first_str) >= 3 and len(second_str) >= 3:
                if sorted(first_str) == sorted(second_str):
                    pairs += 1
        if pairs >= 5:
            return True
    return False
