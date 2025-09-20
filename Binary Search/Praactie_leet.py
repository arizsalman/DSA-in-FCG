# Leetcode no 744

# def func(letters, target):
#     left, right = 0, len(letters)-1
#     while left <= right:
#         mid = (left + right)//2
#         # if letters[mid] == target:
#         #     return mid
#         if letters[mid] <= target:
#             left = mid+1
#         else:
#             right = mid-1
#     return letters[left % len(letters)]


# print(func(letters=["c", "f", "j"], target="c"))
# print(func(letters=["c", "f", "j"], target="a"))
# print(func(letters=["x", "x", "y", "y"], target="z"))


'''LeetCode no 852'''

# class Solution:
# def func(arr):
#     left, right = 0, len(arr) - 1
#     while left < right:
#         mid = (left + right) // 2
#         if arr[mid] < arr[mid+1]:
#             left = mid + 1
#         else:
#             right = mid
#     return left

# def func(arr):
#     left, right = 0,  len(arr)-1
#     while left <= right:
#         mid = (left + right)//2
#         if arr[mid] < arr[mid+1]:
#             left = mid+1
#         else:
#             right = mid-1
#     return left


# print(func(arr=[0, 1, 0]))
# print(func(arr=[0, 2, 1, 0]))

'''Leetcode 153'''
# nums = [4, 5, 6, 7, 0, 1, 2], Output = 0


def func(nums):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left+right)//2
        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid
    return nums[left]


print(func(nums=[4, 5, 6, 7, 0, 1, 2]))
