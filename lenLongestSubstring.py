#!/usr/bin/env python3

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring_lengths = []

        for i in range(len(s)):
            found_letters = set()
            tail = s[i:]
            substring_size = 0
            for letter in tail:
                if letter in found_letters:
                    substring_lengths.append(substring_size)
                    break
                else:
                    substring_size += 1
                    found_letters.add(letter)
            substring_lengths.append(substring_size)
        return max(substring_lengths)

class SolutionIntervals(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        letter_positions = dict()
        intervals = []
        for ind, letter in enumerate(s):
            if letter not in letter_positions:
                letter_positions[letter] = []
            letter_positions[letter].append(ind)

        for letter in letter_positions:
            letter_positions[letter].append(len(s))

        print(letter_positions)
        for key, positions in letter_positions.items():
            if len(positions) == 1:
                intervals.append((positions[0], positions[0]))
            else:
                for interval in zip(positions, positions[1:]):
                    intervals.append(interval)
        intervals.sort(key=lambda x: (x[1] - x[0]), reverse=True)
        print(intervals)
        while True:
            biggest_interval = intervals.pop(0)
            included_intervals = []
            for interval in intervals:
                if interval[0] > biggest_interval[0] and \
                   interval[1] < biggest_interval[1]:
                    included_intervals.append(interval)
            if len(included_intervals) == 0:
                return biggest_interval[1] - biggest_interval[0]
        return None


if __name__ == '__main__':
    c = SolutionIntervals()
    print('abcabcd', c.lengthOfLongestSubstring('abcabcd'))
    print('pwwkew', c.lengthOfLongestSubstring('pwwkew'))
    print('cdd', c.lengthOfLongestSubstring('cdd'))
