
# def is_palindrome(s):
#     s = s.lower()
#     return s == s[::-1]

# test_string = "Malayalan"
# if is_palindrome(test_string):
#     print(test_string, "is a palindrome")
# else:
#     print(f'"{test_string}" is not a palindorme')


def isPalindrome(s):
    return s == s[::-1]

s= "Ankit"
ans = isPalindrome(s)
if ans:
    print("yes")
else:
    print("no")
