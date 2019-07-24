file = open("in.txt","r")
out = open ("out.txt","w")
s=""
for line in file:

    for element in line:
        if element =="'" or element == '"':
            element =""
        s=s+element
out.write("%s" %s)
file.close()
out.close()

