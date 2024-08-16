"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Examples:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""
class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        negative=False
        if x.startswith('-'):
            x=x[1:]
            negative=True
        x=x[::-1]
        x=int(x)
        if negative:
            return x*(-1) if x<2**31 else 0
        else:
            return x if x<2**31 else 0