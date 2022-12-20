#Question 1
vct = "Python is a case sensitive language"
#a)
print("a)",len(vct))
#b)
txt = vct [::-1]
print("b)",txt)
#c)
st= ("a")
ed = ("language")
start = vct.find(st)
end = vct.find(ed)
d = slice(start,end)
d = vct[d]
print("c)",d)
#d)
a = vct.replace("a case sensitive","object oriented")
print("d)",a)
#e)
b = vct.index("a")
print("e)",b)
#f)
c = vct.replace(" ","")
print("f)",c)
