
def if_contains_anagrams(string_list):
    count = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            sorted_i = ''.join(sorted(string_list[i].lower()))
            sorted_j = ''.join(sorted(string_list[j].lower()))
            if sorted_i == sorted_j and len(sorted_i) >= 3:
                count += 1
                if count > 255:
                    return False
    return True
