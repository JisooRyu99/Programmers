from itertools import permutations
def cal(result,sign):
    for i in range(len(result)):
        if result[i]==sign:
            if sign =='-':
                a = int(result[i-1])-int(result[i+1])
            elif sign == '+':
                a = int(result[i-1])+int(result[i+1])
            elif sign == '*':
                a = int(result[i-1])*int(result[i+1])
            if a!=0:
                result[i-1] = str(a)
            else: result[i-1] =0
            result[i],result[i+1]=0,0
    return result

def solution(ex):
    answer=[]
    tmp=''
    result=[]
    for n in ex:
        if n.isdigit()==True:
            tmp+=n
        else:
            result.append(tmp)
            result.append(n)
            tmp=''
    result.append(tmp) 
    
    
    signs = (list(permutations(['+', '-','*'],3)))
    for i in range(len(signs)):
        for j in range(3):
            cal(result,signs[i][j])
            temp=[]
            for k in result:
                if k!=0:
                    temp.append(k)
            
            answer.append(abs(eval("".join(temp))))

    
    return max(answer)
    
