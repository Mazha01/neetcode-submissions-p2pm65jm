class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                st.append(char)
            elif char == ')' and len(st)!=0:
                l = st.pop()
                if l != '(':
                    return False
            elif char == ']' and len(st)!=0:
                l = st.pop()
                if l != '[':
                    return False
            elif char == '}' and len(st)!=0:
                l = st.pop()
                if l != '{':
                  return False  
            elif  char == ')' or char == '}' or char == ']' and len(st)==0:
                return False                
        
        if len(st)!= 0:
            return False


        return True