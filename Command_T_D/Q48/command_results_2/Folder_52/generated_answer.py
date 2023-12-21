
def return_binary_or_hexa(test_tup):
    if test_tup[38] == test_tup[81]:
        return ""
    test_tup_num = len(test_tup)
    test_tup_str = list(map(str, test_tup))
    test_tup_set = set(test_tup_str)
    test_tup_idx = 38
    test_tup_idx_end = 81
    test_tup_idx_end_idx = test_tup_idx_end - 1
    test_tup_idx_start_idx = test_tup_idx - 1
    test_tup_idx_len = test_tup_idx_end_idx - test_tup_idx_start_idx
    if test_tup_idx_len % 2 == 1:
        test_tup_idx_mid = test_tup_idx_start_idx + test_tup_idx_len // 2
        if test_tup_idx_mid in test_tup_set:
            return ""
