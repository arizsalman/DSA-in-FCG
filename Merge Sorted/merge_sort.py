"""Python slicing ka Concept 

Start index (include hota hai) → jo bhi likho, usi index se values milni shuru ho jati hain.

End index (exclude hota hai) → us index tak jaata hai, lekin us element ko include nahi karta.

👉 Ye bad behavior nahi hai, ye intentionally aisa design kiya gaya hai.
    actually ye smart behavior hai jo maths aur programming me consistency laata hai.
"""


def func(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = nums[:mid]  # is ko ese bhekar sakte  he nums[0:mid]0 se mid tak
    # is ko kse he likehe ge . -1 kar ge tu last element include nahe hoga .
    right = nums[mid:]
    # is line me hum ak arry ko do isso me tol rahe he
    left_sort, right_sort = func(left), func(right)

    # or  is me hum 2 haso ko 1 hase me jol raahe he
    sorted_nums = left_sort, right_sort
    return sorted_nums


""" ye hum ne skeleton  bana he ke ye kam kese karta he """


print(func([2, 6, 3, 5, 1, 2, 4, 9]))
