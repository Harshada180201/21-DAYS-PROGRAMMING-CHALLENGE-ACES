
f = open('MyData','r')

f1 = open('ABC','w')

for data in f:
    f1.write(data)


#************************************
#for image

f = open('todo.jfif','rb')

f1 = open('Pic.jfif','wb')

for i in f:
    f1.write(i)