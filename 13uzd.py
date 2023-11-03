"""
Doti divi saraksti.
Izmantojot funkciju map(), izdrukāt abu sarakstu vienādo( sakrīt elementi un to index) elementu summu.
"""

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]


matching_sums = list(map(lambda x, y: x + y, list1, list2))


print("List 1:", list1)
print("List 2:", list2)
print("Sums of matching elements:", matching_sums)
