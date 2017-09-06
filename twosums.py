#!/usr/bin/env python3

import math

class Solution(object):
    def twoSum(self, nums, target):
        sorted_nums = sorted([(i, v) for i, v in enumerate(nums)], key=lambda n: n[1])
        rest_sorted_nums = sorted_nums
        indices = []
        for j in range(len(sorted_nums)):
            first_number = rest_sorted_nums[:1][0]
            number_to_find = target - first_number[1]
            rest_sorted_nums = rest_sorted_nums[1:]
            index = self.search(number_to_find, rest_sorted_nums)
            if index is not None:
                indices = [first_number[0], index]
                break
            else:
                continue
        return indices

    def search(self, number, numbers_array):
        print(number, numbers_array)
        if len(numbers_array) < 2:
            if number == numbers_array[0][1]:
                return numbers_array[0][0]
            else:
                return None


        mid_ind = int(math.floor(len(numbers_array)/2.0))

        if numbers_array[mid_ind][1] == number:
            return numbers_array[mid_ind][0]

        if numbers_array[mid_ind][1] > number:
            return self.search(number, numbers_array[:mid_ind])
        else:
            return self.search(number, numbers_array[mid_ind:])


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 3], 6))
    print(s.twoSum([3,2,4], 6))
