def print_formatted(n):
        width = len("{0:b}".format(n))
        for i in range(1,n+1):
             print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width=width ))#
             
"""st=int(raw_input())

w=len(bin(st)[2:])

for i in range(1,st+1):
    print (str(i).rjust(w,' '),str(oct(i)[1:]).rjust(w,' '),str(hex(i)[2:].upper()).rjust(w,' '),str(bin(i)[2:]).rjust(w,' '),sep=' ')"""
    
   

if __name__ == '__main__':
