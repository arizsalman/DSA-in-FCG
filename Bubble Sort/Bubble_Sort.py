'''Bubble Sort ek simple sorting algorithm hai jo list (array) ke elements ko ascending ya descending order me arrange karne ke liye use hota hai.'''

# INNER & OUTER LOOP
"""Ek analogy 🧩

Socho inner loop ek worker hai jo ek line me boxes ko compare karke swap karta hai.
Outer loop manager hai jo worker ko kehta hai:

"Phir se line ke shuru se jao aur dobara karo."

"Phir se jao."

"Phir se jao."

Jab tak saare boxes sorted na ho jayein.
Manager khud box ko touch nahi karta — sirf worker ko kaam repeat karwata hai."""

""" Importance Point 
Tumhari baat:
last 9, se phele 1 he → outer loop ne pehla round me 9 ko end me fix kar diya, ab baki [8,6,5,3,2,1] me again repeat karega.
agar last me value  bajte tu update kar outer ab sahe he tu repeat karo bus 
"""


def func(nums):
    for j in range(len(nums)-1):  # outer loop
        print(f'j{j+1} start {nums}')
        for i in range(len(nums)-1):  # inner loop
            print(f'i  atart at i {i}: {nums}')
            # Kyon lag raha hai "sirf inner loop kaam kar raha hai"?
            # Kyonke kaam karne wali line sirf inner loop me hai:
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums


print(func([9, 8, 6, 5, 3, 2, 1]))
