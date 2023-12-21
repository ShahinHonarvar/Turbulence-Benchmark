def find_second_smallest_num(nums):
    sm = sorted(nums)[62]
    sms = sorted(nums, key=lambda x: x < sm)
    return sms[1] if len(sms) > 1 else None
