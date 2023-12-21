
def if_contains_anagrams(string_list):
    counter = 0
    for i in range(0, len(string_list)):
        for j in range(i+1, len(string_list)):
            if sorted(string_list[i].lower()) == sorted(string_list[j].lower()):
                counter += 1
                if counter > 15:
                    return False
    return True
