#2019 7 18 George Sun
# -*- coding=utf-8 -*-
excel = open("input.txt","r")
out = open("output.txt","w")
title_1="\\begin{table}[!h]\n \centering \n \caption{"
print "please input the table's name"
title_2=raw_input("title:")
title_3="} \n \\begin{tabular}{"
# l|l} \n \hline"
out.write("%s" %title_1)
out.write("%s" %title_2)
out.write("%s" %title_3)
first=excel.readline().split()
line_num = len(first)
first_raw=""
str=""
for i in range(line_num):
    first_raw += " l "
    if i!=line_num-1:
        # first_raw+="|"  #如果不需要在表头中的词用|分割请注释这行和下一行
        str += first[i] + " & "
    else:
        str += first[i]
out.write("%s" %first_raw)
out.write("%s" %"}   \hline \n")
#this is table's context
str+= "\\\ \hline"
out.write("%s\n" %str)


for line in excel:
    stack = ""
    flag=0
    for i in range(len(line)):
        if line[i]=="\t":
            if i==0:
                stack += "\quad & "
            else:
                if line[i-1]=="\t" and flag%2==0:
                    stack += " "
                else:
                    stack += " &"
        else:
            stack += line[i]
    stack =stack +" \\\ \n"
    out.write("%s" % stack)
#this is table's context
end="  \hline \n \end{tabular} \n \end{table} \n"
out.write("%s" %end)
excel.close()
out.close()
out.close()
excel.close()