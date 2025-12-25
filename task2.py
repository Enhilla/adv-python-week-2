nums = list(map(int, input()))

# avg_salary = max(nums)-min(nums)

# print(avg_salary)

max_salary = nums[0]
min_salary = nums[0]


for x in nums:
    if max_salary < x:
        max_salary = x
    if max_salary > x:
        min_salary = x

print(max_salary - min_salary)

