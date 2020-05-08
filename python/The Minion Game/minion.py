def minion_game(string):
        vw='aeiou'.upper()
    
        kv=0
        st=0

        kvs=sum(len(string)-i for i in range(len(string)) if string[i] in vw )
        stc=sum(len(string)-i for i in range(len(string)) if not string[i] in vw )
        if kvs>stc:
            print("Kevin",kvs)
        elif kvs==stc:
            print("Draw")   
        else:
            print("Stuart",stc) 
    
    # your code goes here

if __name__ == '__main__':
              s = input()
              minion_game(s)
