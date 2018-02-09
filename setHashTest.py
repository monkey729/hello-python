#set里的元素都是可哈希的,一旦要存入不可哈希会报错
#可变对象不可hash   不可变对象可hash
#set只接受一个可迭代参数
str2 =set([1,"hello",3])
str1 =set([1,"hello",3])
for i in str2:
	print ("%s的哈希值=%s"%(i,hash(i)))
str1.add("123")
print (str1)
