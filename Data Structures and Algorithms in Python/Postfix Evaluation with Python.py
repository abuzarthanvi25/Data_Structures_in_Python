# Q.1 (c)
def postfix_evaluation(k):  
    k = k.split()
    n=len(k)
    stack =[]
    for i in range(n):

        if k[i].isdigit():
          #append function is equivalent to push
            stack.append(int(k[i]))

        elif k[i]=="+":

            a=stack.pop()
            b=stack.pop()
            stack.append(int(a)+int(b))

        elif k[i]=="*":

            a=stack.pop()
            b=stack.pop()
            stack.append(int(a)*int(b))

        elif k[i]=="/":

            a=stack.pop()
            b=stack.pop()
            stack.append(int(b)/int(a))

        elif k[i]=="-":

            a=stack.pop()
            b=stack.pop()
            stack.append(int(b)-int(a))            
    return stack.pop()
#space separtor is required , for solving 2 or more digits .
k = " 2 4 8 + 10 / * "
evaluation = postfix_evaluation(k)
print(evaluation)
