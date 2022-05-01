from cmath import inf
import io

import math
def read_file(file_name):
    file_opened=open(file_name,'r')
    lines=file_opened.read().splitlines()
    
    file_opened.close()
    for i in range(len(lines)):
        lines[i] = eval(lines[i])
    return lines

    
def file_write(file_name,file_content):
    file_opened=open(file_name,'a')
    file_opened.write(file_content)



def fun(sp,arr,sum):

    for i in arr:
        val=i
        newarray=list(arr)
        newarray.pop(newarray.index(i))
        sum+=abs(sp-val)
        sum= abs(sum-fun(val,newarray,sum))
    li.append(sum)
    return sum
    
        
    
li=[]
lines=read_file('ts1_input.txt')
for line in lines:
    print(type(line))








