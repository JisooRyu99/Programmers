def solution(s):
    stack=[]
    for c in s:
        if len(stack)==0:
            stack.append(c)
            continue

        if stack[-1]!=c:
            stack.append(c)
        else: stack.pop()
    if len(stack)==0:
        return 1
    else : return 0