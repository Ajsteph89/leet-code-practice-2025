# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105. 

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

s = "2[abc]3[cd]ef"

def decodeString(s):
    stack = []
    current_num = 0
    current_str = ""

    for c in s:
        if c.isdigit():
            current_num = current_num * 10 + int(c)
        elif c == "[":
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif c == "]":
            last_str, num = stack.pop()
            current_str = last_str + current_str * num
        else:
            current_str += c

    return current_str

print(decodeString(s))    