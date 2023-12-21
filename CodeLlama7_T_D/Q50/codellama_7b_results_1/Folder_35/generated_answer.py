
def if_contains_anagrams(my_list):
    count = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                count += 1
                if count >= 153:
                    return True
    return False
