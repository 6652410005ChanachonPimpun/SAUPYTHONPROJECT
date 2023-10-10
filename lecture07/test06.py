# Slicing dayda in List and Tuple
#        0   1     2       3         4          5
var1 = [10, 20, 'Hello', True, (111, 'wow'), 'สมชาย']

var2 = (10, 20, 'Hello', True, (111, 'wow'), 'สมชาย')

#20, 'Hello', true
print(var1[1:4])
# true, (111, 'wow')
print(var1[3:5])
# 10, 20, 'Hello'
print(var1[:3])
#'Hello', true, (111, 'wow'), 'สมชาย'
print(var1[2:])