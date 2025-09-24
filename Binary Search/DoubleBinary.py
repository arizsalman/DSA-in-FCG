"""Leetcode No 34 """

# nums = [5, 7, 7, 8, 8, 10], target = 8, [3, 4]


# def find(nums,  target):

#     def first(nums, target):
#         left, right = 0, len(nums)-1
#         find = -1
#         while left <= right:
#             mid = (left + right)//2
#             if nums[mid] == target:
#                 find = mid
#                 right = mid-1
#             elif nums[mid] < target:
#                 left = mid+1
#             else:
#                 right = mid-1
#         return find

#     def last(nums, target):
#         left, right = 0, len(nums)-1
#         find = -1
#         while left <= right:
#             mid = (left + right)//2
#             if nums[mid] == target:
#                 find = mid
#                 left = mid+1
#             elif nums[mid] < target:
#                 left = mid+1
#             else:
#                 right = mid-1
#         return find
#     return first(nums, target), last(nums, target)


# print(find(nums=[5, 7, 7, 8, 8, 10], target=8))
# print(find(nums=[5, 7, 7, 8, 8, 10], target=6))


# # arr = [2,3,4,7,11], k = 5
# def func(arr, k):
#     left, right = 0, len(arr)-1
#     while left <= right:
#         mid = (left+right)
#         missing = arr[mid]-(mid+1)
#         if missing < k:
#             left = mid+1
#         else:
#             right = mid-1
#     return left + k


# print(func(arr=[2, 3, 4, 7, 11], k=5))

# [2, 4, 7, 10, 15], x = 6 7


# def funcs(arri, x):
#     left, right = 0, len(arri)-1
#     find = -1
#     while left <= right:
#         mid = (left+right)//2
#         print(f'mid {mid}')
#         if arri[mid] >= x:
#             find = arri[mid]
#             right = mid-1
#             print(f"right {right}")
#         else:
#             left = mid + 1
#             print(f'left {left}')
#     return find


# print(funcs(arri=[2, 4, 7, 10, 15], x=6))
# print(funcs(arri=[2, 4, 7, 10, 15], x=16))


# mountainArr = [1,2,3,4,5,3,1], target = 3
"""Leetcode no 1095"""

""" ye kam tu kar raha but leetcode me us question ke requirement ye nahe the is error de raha he  """


# def func(arr, target):
#     left, right = 0, len(arr)-1
#     find = -1
#     while left <= right:
#         mid = (left + right)//2
#         if arr[mid] == target:
#             return arr[mid]
#         elif arr[mid] < target:
#             left = mid+1
#         else:
#             right = mid-1
#     return find


# # 3
# print(func(arr=[1, 2, 3, 4, 5, 3, 1], target=3))


# leetcode no 658


# arr = [1, 2, 3, 4, 5], k = 4, x = 3


# def func(arr, k, x):
#     left, right = 0, len(arr)-1
#     while left <= right:
#         mid = (left + right)//2
#         if arr[mid] < x:

#             left = mid+1
#         else:
#             right = mid-1
#     return k


# print(func(arr=[1, 2, 3, 4, 5], k=4, x=3))


# arr = [1, 2, 3, 4, 5], k = 4, x = 3
'''Leetcode no 658'''


def func(arr, k, x):
    left, right = 0, len(arr)-1
    while right - left + 1 > k:
        if abs(arr[left]-x) > abs(arr[right]-x):
            left += 1
        else:
            right -= 1
    return arr[left:right+1]


print(func(arr=[1, 2, 3, 4, 5], k=4, x=3))
