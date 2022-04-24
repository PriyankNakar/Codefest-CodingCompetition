import ast
from asyncio.windows_events import NULL
def minmax(list_):
        minpos = list_.index(min(list_))
        maxpos = list_.index(max(list_))
        return minpos,maxpos
def sol():
    file1=open('paytm_stock_input.txt','r')
    lines=file1.readlines()
    lines.pop(0)
    print(lines)
    for inp in lines:
        list_=ast.literal_eval(inp)
        minpos,maxpos=minmax(list_)
        if minpos<maxpos:
            profit=list_[maxpos]-list_[minpos]
        else:
            counter=0
            while minpos>maxpos and counter<len(list_):
                nvlist=list(list_)
                nvlist[minpos]=NULL
                nvlist[minpos]=NULL
                minpos,maxpos=minmax(nvlist)
                counter+=1
            profit=list_[maxpos]-list_[minpos]
        hr=9
        min=20
        for i in list_:
            
            min+=10
            if min>=60:
                min=min%60
                hr+=1
            
            if hr>12:
                hr=hr%12
            if i==list_[maxpos]:
                break

        file2=open("sol3.txt","a")
        file2.write(str([str(profit)+","+str(hr)+"."+str(min)]))
        file2.write("\n")

            
sol()