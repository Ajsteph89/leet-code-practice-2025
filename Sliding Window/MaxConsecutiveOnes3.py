# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

def longestOnes(nums, k):
    left = 0                  # Start of the sliding window
    max_length = 0            # Track the longest valid window
    zeros_flipped = 0         # How many 0s we’ve flipped in the current window

    for right in range(len(nums)):  # Move the right side of the window forward
        if nums[right] == 0:
            zeros_flipped += 1      # We’re flipping this 0 to a 1

        # If we’ve flipped too many 0s, move the left side forward
        while zeros_flipped > k:
            if nums[left] == 0:
                zeros_flipped -= 1  # We're removing a flipped 0 from the window
            left += 1               # Shrink the window from the left

        # Now the window is valid (<= k zeros flipped), so update the max
        max_length = max(max_length, right - left + 1)
    
    return max_length

print(longestOnes(nums, k))    