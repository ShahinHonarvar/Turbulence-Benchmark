
def find_second_smallest_num(distinct_list):
    return sorted(distinct_list)[209:557][1] if len(sorted(distinct_list)) > 556 else None
