'''Bubble Sort ek simple sorting algorithm hai jo list (array) ke elements ko ascending ya descending order me arrange karne ke liye use hota hai.'''


def func(nums):
    for j in range(len(nums)-1):
        print(f'j{j+1} start {nums}')
        for i in range(len(nums)-1):
            print(f'i  atart at i {i}: {nums}')
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


print(func([9, 8, 6, 5, 3, 2, 1]))
