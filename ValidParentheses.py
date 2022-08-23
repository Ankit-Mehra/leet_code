def openClose(s:str)->bool:
    closed_brackets = ['}',']',')']
    open_brackets = ['{','[','(']
    list_s = list(s)
    for i in range(len(list_s)-1):
        if (list_s[i] in open_brackets and list_s[i+1] in closed_brackets):
            return False
        else:
            True


def isValid(s: str) -> bool:
        
        valid_dict = {'{':'}','[':']','(':')'}
        validity = False
        if len(s)%2 != 0:
            return validity
        
        if not openClose(s):
            return validity
        i =0
        list_s = list(s)
        while i < len(list_s):
            j = i+1
            while j < len(list_s):
            # for j in range(i+1,len(list_s)):
                if list_s[j] == valid_dict.get(list_s[i]):
                    list_s.pop(j)
                    list_s.pop(i)
                    j-=1
                    i-=1
                j+=1
                
                        
            if len(list_s) == 0:
                validity = True
                break
            i+=1
                
        return validity       
s = "{[}]"
print(isValid(s))
# print(openClose(s))