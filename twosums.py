#!/usr/bin/env python3

class Solution(object):
    def twoSum(self, nums, target):
        sorted_nums = sorted([(i, v) for i, v in enumerate(nums)], key=lambda n: n[1])
        rest_sorted_nums = sorted_nums
        indices = []
        for j in range(len(sorted_nums)):
            first_number = rest_sorted_nums[:1]
            number_to_find = target - first_number
            rest_sorted_nums = rest_sorted_nums[1:]
            index = self.search(number_to_find, rest_sorted_nums)
            if index is not None:
                indices = [first_number[0], index]
                break
            else:
                continue
        return indices

    def search(self, number, 
            
