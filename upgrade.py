import os

acc = os.popen("cat /home/ubuntu/accuracy.txt")


acc1 = acc.read()
print(acc1)
acc3 = float(acc1)


if acc3<85:
    x = os.popen("cat /home/ubuntu/train.py | grep model.add | wc -l")
    x1 = x.read()
    x2 = x1.rstrip()
    x3 = int(x2)
    print(x3)
    if x3==2:
        y = 'model.add(Dense(units=32, activation=\"relu\"))'
    elif x3==3:
        y = 'model.add(Dense(units=16, activation=\"relu\"))'
    elif x3==4:
        y = 'model.add(Dense(units=8, activation=\"relu\"))'
    else:
        print("Can't do more!!")
        exit()
    os.system("sed -i '/softmax/ i {}' /home/ubuntu/train.py".format(y))
    acc = os.popen("cat /home/ubuntu/accuracy.txt")
	
    acc1 = acc.read()
    print(acc1)
    acc3 = float(acc1)
    
else:
    print("ACCURACY ABOVE 85")

