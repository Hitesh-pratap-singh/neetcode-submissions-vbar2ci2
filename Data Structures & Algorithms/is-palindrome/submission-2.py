class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s2 = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # print(s2)
        left = 0;
        right = len(s)-1
        print('lenght -> ', len(s))
        while left <= right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() == s[right].lower():
                left +=1
                right -= 1
            else:
                return False

        return True;