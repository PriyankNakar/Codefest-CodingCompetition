import ast


def check():
    file1=open('Traffic_Lane_Input.txt','r')

    lines=file1.read().splitlines()
    file1.close()
    counter=1
    sum_dic=dict()
    
    lines.pop(0)
    for i in lines:
        list_=list(set(ast.literal_eval(i)))
        sum_dic[counter]=sum(list_)
        
        counter+=1

    s=sorted(sum_dic.values())
    li=[]
    for j in s:
        
        for keys,values in sum_dic.items():
            if  j==values:
                li.append(keys)
                li.append(values)

    file2=open("sol1.txt",'a')
    file2.write(str(li))
    file2.close()
        
check()