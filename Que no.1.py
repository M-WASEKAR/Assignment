''''''
# 1. Check if the given string is a palindrome or not irrespective of case
# Eg: Naan – True, naan – True, roti – False
# ''''''
string =input("Enter the string :").lower()
def pallindram(s1):
    s2 = s1[::-1]
    if s1 ==s2 :
        return True
    return False

print(pallindram(string))