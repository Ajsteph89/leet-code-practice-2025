# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"

# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

s = "IceCreAm"

def reverseVowels(s):
    vowels = set("aeiouAEIOU")
    string_list =  list(s)
    found = [x for x in string_list if x in vowels]

    for i in range(len(string_list)):
        if string_list[i] in vowels:
            string_list[i] = found.pop()
    
    return ''.join(string_list)


print(reverseVowels(s))    

