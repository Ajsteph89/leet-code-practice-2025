# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.


# Example 1:
# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"

# Example 2:
# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

# Example 3:
# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"

word1 = "abbzzca"
word2 = "babzzcz"

def closeStrings(word1, word2):
    if len(word1) != len(word2):
        return False

    # Count characters in both strings
    count1 = {}
    count2 = {}

    for c in word1:
        count1[c] = count1.get(c, 0) + 1
    for c in word2:
        count2[c] = count2.get(c, 0) + 1

    # Check if the sets of characters match
    if set(count1.keys()) != set(count2.keys()):
        return False

    # Check if the sorted frequency values match
    return sorted(count1.values()) == sorted(count2.values())

print(closeStrings(word1, word2))