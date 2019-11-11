#write 'r' before adress url of a file when you give full addres
#if file in same folder no need to write .txt

#file writing
# var=open('file.txt','w')
# file=var.write("hello world")
# print(file)



#file reading
# var = open('file.txt','r')
# file = var.read()
# print(file)


#file append
# var=open('file.txt','a+')
# file = var.write(' but im happy')
# print(file)


#file reading
# var=open('file.txt','r')
# file = var.read()
# print(file)

#closing file
# var=open('file.txt','a+')
# file=var.write('because i love to live happily')
# var.close()


#file read
# var=open('file.txt','r')
# file=var.read()
# print(file)


# readline in a file
# var=open('file.txt','r')
# file = var.readlines()
# print(file)
# for i in file:
#     print(i)


# var=open('file.txt','w')
# for i in range(10):
#     var.write('pakistan\n')
# var.close()


# var=open('file.txt','r')
# file=var.readlines()
# print(file)
# for i in file:
#     print(i)



#storing pattern in file
var=open('pattern','w')
num=int(input('range :'))

for i in range(num):
    for j in range(0,i):
        var.writelines(str(i))
    var.write('\n')
var.close()
var=open('pattern','r')
pattern=var.read()
print(pattern)



    