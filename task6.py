# -*- coding: utf-8 -*-
"""task6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WC7yXLzK8Qgfd9YCa5PVqWxkw4XXj39Z
"""

inp_file= open('input6_3.txt',"r")
out_file= open('output6_3.txt',"w")
list_l= []
em_list= []
rows,columns= [int(a) for a in inp_file. readline(). split() ]


row= ["#"]* ( columns+2 ) 
list_l.append(row)
temp1=inp_file.read().split("\n")
#---------------------------------

for l in range(len (temp1)) : 
  new_list=["#"]
  
  for b in temp1[l] :
    new_list.append(b)
  
  new_list.append("#")
  list_l.append (new_list)

list_l.append (row)

for x in range(rows+2) :
  new_list=[]
  
  for y in range(columns+2) :
    
    if list_l[x] [y]=='#' :
      new_list.append(-1 )
    
    else :
      new_list.append(0)
  em_list.append(new_list)
#-------------------
def DFS(x, y) :
  if list_l [x][y]=="D"  :
    
    if [x, y] not in map : 
      map.append([x, y])
  
  temp2=[ [x-1,y], [x+1,y], [x,y+1], [x,y-1] ]
  
  for z in temp2:
    
    if  em_list[z[0]] [z[-1]]==0 :
      em_list[x][y]=1
      DFS(z[0], z[1])

num=0
for a in range(rows+2):
  
  for b in range(columns+2):
    
    if em_list[a][b]==0 and  list_l[a][b]=='.'  :
      map=[] 
      DFS(a, b)
      
      if len(map)> num :
        num=len(map)
#----------------
out_file.write(str(num))
inp_file.close()
out_file.close()