'''
2.The user enters a string and a substring. You have to print the number of times that the
substring occurs in the given string. String traversal will take place from left to right, not from
right to left.
NOTE: String letters are case-sensitive. The first line of input contains the original string. The
next line contains the substring.
Example: Input: ABCDCDC pattern: CD
'''
def count_string(string, substring):
    count=0
    for i in range(len(string)):
        if(string[i:].startswith(substring)):
            count=count+1

    return count
s1="ABCDCDC"
s2="CD"
print("The original string is :", s1)
print("The sunstring is:", s2)
print(count_string(s1,s2))
