def min_max(nums: list[float | int]):
    if len(nums)== 0:
        raise TypeError ('ValueError')
    min_num = min(nums)
    max_num = max(nums)
    return (min_num, max_num)
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5,-2,-9]))
print(min_max([]))
print(min_max([1.5,2,2.0,-3.1]))