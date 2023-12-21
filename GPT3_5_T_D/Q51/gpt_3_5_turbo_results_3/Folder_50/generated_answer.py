
def if_contains_anagrams(string_list):
    count = 0
    for i in range(len(string_list)-1):
        for j in range(i+1, len(string_list)):
            if sorted(string_list[i].lower()) == sorted(string_list[j].lower()):
                count += 1
                if count > 47:
                    return False
    return True
