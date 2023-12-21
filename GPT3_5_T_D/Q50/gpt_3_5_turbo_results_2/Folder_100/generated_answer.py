
def if_contains_anagrams(string_list):
    pairs_count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and string_list[i].lower() == string_list[j].lower()[::-1]:
                pairs_count += 1
    return pairs_count >= 95
