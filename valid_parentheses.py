"""Given a string s containing just the characters '(', ')', '{', '}', '[' 
and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Intuion: Intiated a dictionary with open brackets as keys and closed brackets as values.
then initiated a stack. Then looped through the string and if the bracket in the string is
in the dictionary keys, then push the value(closed brackets) to the stack.If the bracket in 
the string is not in the dictionary keys(means its a closed bracket) and the stack is empty
or the first pop(closed bracket) from the stack is not equal to the bracket(closed) in the 
string. Return False. 
If the stack is empty at the end of the loop, return True. Else return False.

"""

def is_valid(brackets: str) -> bool:
    """Using stack to check if brackets are valid
    :param brackets: string of brackets
    :return: True if brackets are valid, False otherwise"""
    closed = {'{':'}','[':']','(':')'} # dictionary of closed brackets

    stack = [] # stack to store open brackets

    for bracket in brackets: # iterate through brackets
        if bracket in closed: # if bracket is open bracket
            stack.append(closed[bracket]) # append corresponding closed bracket
        # if bracket is closed bracket and stack is empty or bracket does
        # not match last open bracket
         # also means that there is no open bracket and closed bracket
         # is first in the string or there is no open bracket for the closed bracket
        elif not stack or bracket != stack.pop():
            return False # return False
    return not stack # return True if stack is empty

def open_close(s:str)->bool:
    """check if opening closing brackets are in order"""
    open_brackets = ['{','[','(']
    closed_brackets = ['}',']',')']
    list_s = list(s)
    for i in range(len(list_s)-1):
        if (list_s[i] in open_brackets and list_s[i+1] in closed_brackets):
            return False
    return True

def isValid(s: str) -> bool:
        
    valid_dict = {'{':'}','[':']','(':')'}
    validity = False
    if len(s)%2 != 0:
        return validity
   
    if not open_close(s):
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





s = "{[]}"
f = "()"
print(isValid(s))
print(is_valid(s))
# print(openClose(s))
