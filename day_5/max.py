# day 5, replicate max() function


def find_max(nums):
    max = 0
    for num in nums:
        if num > max:
            max = num
    return max

nums = [150, 143, 142, 185, 120, 171, 184, 149, 59, 199, 78, 65, 42, 12]
print(find_max(nums))