class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        st = []
        for char in tokens:
            if char !='+' and  char !='-' and char !='*'  and char !='/':
                st.append(int(char))
            else:
                r = st.pop()  
                l = st.pop()
                if char =='+':
                    res = l + r
                    st.append(res)
                elif char =='/':
                    res = int(l/r)
                    st.append(res)
                elif char =='*':
                    res = l*r
                    st.append(res)
                elif char =='-':
                    res = l-r
                    st.append(res)           


        return st.pop()