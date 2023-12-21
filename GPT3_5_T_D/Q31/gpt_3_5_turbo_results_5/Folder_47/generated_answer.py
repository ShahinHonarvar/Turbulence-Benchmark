
def if_perfect_num(nums):
    def sum_of_divisors(num):
        divisors = [1]
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                if i == num / i:
                    divisors.append(i)
                else:
                    divisors.append(i)
                    divisors.append(num // i)
        return sum(divisors)

    return sum_of_divisors(nums[34]) == nums[34]
