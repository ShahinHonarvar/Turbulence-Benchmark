
def if_contains_anagrams(string_list):
    count = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3 and string_list[i].lower().count(string_list[j].lower()) == len(string_list[i]):
                count += 1
    return count >= 19
