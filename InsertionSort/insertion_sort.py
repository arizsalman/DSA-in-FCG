"""🔹 Big Picture

For loop → ek ek element ko key banata hai.

While loop → key ke liye jagah banata hai (shift karke).

nums[j+1] = key (loop ke baad) → key ko us jagah pe daal deta hai."""


def func(nums):
    nums = list(nums)
    for i in range(len(nums)):
        key = nums[i]
        j = i-1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
            nums[j+1] = key
    return nums


print(func([9, 8, 6, 5, 3, 2, 1]))


# def func(nums1):
#     nums1 = list(nums1)
#     for i in range(len(nums1)):
#         print(f'After itera i :{i+1} :{nums1}')
#         key = nums1[i]
#         j = i-1
#         print(f'after i -1 :{j}')
#         while j >= 0 and nums1[j] > key:
#             nums1[j+1] = nums1[j]
#             j -= 1
#             print(f' After j-1 {j}')
#             nums1[j+1] = key
#     return nums1


# print(func([9, 8, 6, 5, 3, 2, 1]))


# def func(nums1):
#     nums1 = list(nums1)
#     for i in range(len(nums1)):
#         key = nums1[i]
#         print(f"\nIteration {i+1}: key = {key}, array = {nums1}")

#         j = i - 1
#         while j >= 0 and nums1[j] > key:
#             print(
#                 f"  nums[{j}]={nums1[j]} > key={key} → shifting {nums1[j]} to position {j+1}")
#             nums1[j+1] = nums1[j]
#             j -= 1

#         nums1[j+1] = key
#         print(f"  Insert key={key} at position {j+1} → {nums1}")
#     return nums1


# print("Final sorted array:", func([9, 8, 6, 5, 3, 2, 1]))


# nums = [9, 8, 6, 5, 3, 2, 1]
# for _ in range(len(nums)-1):
#     for i in range(len(nums)-1):
#         if nums[i] > nums[i+1]:
#             nums[i], nums[i+1] = nums[i+1], nums[i]
# print(nums)


num = [9, 8, 6, 5, 3, 2, 1]

for i in range(len(num)):
    key = num[i]
    j = i-1
    while j >= 0 and num[j] > key:
        num[j+1] = num[j]
        j -= 1
        num[j+1] = key
print(f' Its nums{num}')
