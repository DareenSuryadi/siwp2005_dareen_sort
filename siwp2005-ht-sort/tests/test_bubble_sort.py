import sys
sys.path.append(r'C:\Users\SHAREEN ANGELICA\SI-UKKW-SIWP2005_OOP_2024\siwp2005-ht-sort\src')
import unittest
from sort.bubble_sort import Bubble
class TestBubbleSort(unittest.TestCase):
    def test_bubble(self):
        arr = [0, 50, 7, 34, 66, 85]
        print('this is the unsorted list:')
        print(arr)
        result = Bubble.bubble_sort(arr)
        print('this is the (bubble) sorted list:')
        print(result)

if __name__ == "__main__":
    unittest.main()