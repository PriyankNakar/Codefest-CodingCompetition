from itertools import permutations

def sol():
    file1=open('q2_inp.txt','r')
    lines=file1.readlines()
    for inp in lines:
        l = list(permutations(range(1, int(inp)+1)))
        file2=open('sol2.txt','a')
        file2.write(str(l[::-1]))
        file2.close()
    file1.close()    

sol()