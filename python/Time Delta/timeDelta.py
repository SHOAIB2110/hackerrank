from datetime import datetime
fmt='%a %d %b %Y %H:%M:%S %z'
for _ in range(int(input())):
    t1=datetime.strptime(input(),fmt)
    t2=datetime.strptime(input(),fmt)
    print (int(abs((t1-t2).total_seconds())))
