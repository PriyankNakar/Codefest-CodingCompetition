import ast
from asyncio.windows_events import NULL
from sys import flags
def check():
    file1=open('mayurbhajiya_input.txt','r')

    lines=file1.read().splitlines()
    file1.close()
    counter=0
    lines.pop(0)
    for i in lines:
        i=ast.literal_eval(i)
        if counter==0:
            stack_to=i
            counter+=1
        elif counter==1:
            stack_oo=i
            counter+=1
        else:
            stack_res=i
            counter=0
            flag=True
            cop_res=list(stack_res)
            for j in cop_res:
                
                if j == stack_to[0]:
                    stack_to.pop(0)
                    stack_res.pop(0)
                    if stack_to==[]:
                        stack_to.append(NULL)
                elif stack_oo[0]==j:
                    
                    stack_oo.pop(0)
                    stack_res.pop(0)
                    if stack_oo==[]:
                        stack_oo.append(NULL)
                else:
                    f1=open('sol4_out.txt','a')
                    f1.write('Invalid\n')
                    f1.close()
                    flag=False
                    break
                    
            if flag==True:
                f1=open('sol4_out.txt','a')
                f1.write('Valid\n')
                f1.close()
                

check()       

        