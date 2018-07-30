# test conditional statements
var1 =4
var2 =5
if var1 == var2 :
    print("good its equal")
else:
    print("not equal")

print("While statement")
while var2 > 0 :
    print("value", var2)
    var2 = var2 -1
print("For statement")
for i in range (1,10, 1):
    print("var", i)

print("For statement default range and increment")
for i in range (5):
    print("var", i)

print("while with break statement")
var2 =5
while var2 > 0 :
    print("value", var2)
    var2 = var2 -1
    if var2 == 3:
        break;
print("end of while")
