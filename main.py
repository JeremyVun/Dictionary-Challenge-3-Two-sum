"""
Dictionary Challenge 3 - Two Sum

Description:
Given an array of integer nums and an integer target, return indices of two numbers in nums where the two numbers add up to the target.

Example:
Input:
  nums = [2,7,11,15]
  target = 9
Correct Output:
  [0,1]
  # Because nums[0] + nums[1] == 9, we return [0, 1].
"""

from solutions import fast


########
# Write your code in this function
########
def solution(nums, target):
  return fast(nums, target)




########
# This code wil run your solution against a bunch of test cases
########
from tests.runner import run_tests

if __name__ == "__main__":
  run_tests(solution)