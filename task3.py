# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11-ZqtayQTpMr96rCdhGC5I-HcdhNln5W
"""

inp_file=open('input3_2.txt',"r") #DFS
out_file=open('output3_2.txt',"w")
list_1= inp_file.readline()
list_1= list_1.split()


num=0
em_dict={}
c=int(list_1[1])
#------------------------------------
while num <c :
  list_2= inp_file.readline()
  list_2= list_2.split()
  new_line= [list_2[1],list_2[0]]
  
  u= list_2[0]
  v= list_2[1]
  u_alt= new_line[0]
  v_alt= new_line[1]
  
  
  if(u not in em_dict) :
    em_dict[u] = [v]
    
  
  else :
    em_dict[u].append(v)
#--------------------------------------  
  if(u_alt in em_dict):
    em_dict[u_alt].append(v_alt)
  
  else :
    em_dict[u_alt] = [v_alt]    
  num=num+1     
#-------------------------------
em_list=[]
def DFS(em_list,em_dict,s)  :  #s=source
  
  if s not in em_list :
    print(s,end=" ", file=out_file)
    
    em_list.append(s)
    
    for c in em_dict[s]  :
      DFS (em_list,em_dict,c)
#--------------------------------------
DFS(em_list,em_dict,"1")
inp_file.close()
out_file.close()