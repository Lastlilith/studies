"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = float('-inf')

    for i in range(len(nums)):
        for j in range(i, min(i + k, len(nums))):
            max_sum = max(max_sum, sum(nums[i:j + 1]))

    return max_sum
