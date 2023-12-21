
def if_contains_anagrams(string_list):
    count = 0
    for i in range(len(string_list)):
        string1 = string_list[i].lower()
        for j in range(i+1, len(string_list)):
            string2 = string_list[j].lower()
            if sorted(string1) == sorted(string2) and len(string1) >= 3:
                count += 1
                if count > 445:
                    return False
    return True
