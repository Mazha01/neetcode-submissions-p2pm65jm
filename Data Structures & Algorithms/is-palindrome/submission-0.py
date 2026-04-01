class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l_index=0
        # r_index=len(s)-1
        # while l_index <= r_index:
        #     cur_l = ""
        #     cur_r = ""
        #     if s[l_index].isalnum()==False:
        #         l_index+=1
        #     else: 
        #         cur_l =  s[l_index].lower()  

        #     if s[r_index].isalnum()==False:
        #         r_index-=1
        #     else:
        #         cur_r =  s[r_index].lower() 


        #     if  cur_l!=cur_r:
        #         return False

        # for char in s:
        #     cur_l = ''
        #     c = len(s)-1
        #     r_index=len(s)-1
        #     if char.isalnum()==False:
        #         continue
        #     else:    
        #        cur_l = char.lower()
        #        while not s[r_index].isalnum():
        #             r_index-=1
        #     if  cur_l!=s[r_index].lower():
        #             return False

        #     r_index-=1   
        # return True


        l = 0
        r = len(s)-1


        while l < r:    
            while l < r and not s[l].isalnum():
                l+=1

            while l < r and not s[r].isalnum():
                r-=1

            if  s[l].lower()!=s[r].lower():
                return False

            l+=1
            r-=1

        return True    





