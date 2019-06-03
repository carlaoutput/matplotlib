# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 23:04:53 2018
@author: Carla Pastor  
Project: Heat Distribution. 

"""
import numpy as np
import matplotlib.pyplot as lb
from matplotlib.colors import ListedColormap

if __name__ == "__main__":  
    inp=int(input("Enter the starting temperature: "))
   
    oldTemp=np.zeros((inp+1, inp+1))

    for index in range(0,inp+1):
        oldTemp[index, 0]=inp
    temp=np.copy(oldTemp) #np.copy returns an array copy of the given object.
    
    #counter to count 3000 iterations and stop if program iterates more than 3000..
	#In the interest of time, I will stop at 3000 iterations if we don’t see convergence by then.
    c=0
    # while (True):
    while c!=3000:
        flag=False # go ahead and check. EXACTLY 
        for i in range(1, inp):
            for j in range(1, inp):
                temp[i,j]=0.25*(oldTemp[i-1,j] + oldTemp[i+1,j] + oldTemp[i,j-1] + oldTemp[i,j+1]) #included in the hw specifications
                
                if np.array_equal(temp, oldTemp):  # True if two arrays have the same shape and elements, False otherwise.
                    flag=True
                    break
                
            if flag==True:
                break
        oldTemp=np.copy(temp)
        if flag==True:
            break
        #increment counter
        c=c+1
    #ref : https://stackoverflow.com/questions/44443993/matplotlib-colors-listedcolormap-in-python
    cmap = ListedColormap(['darkblue','blue','aqua','lawngreen','yellow','orange','red','darkred']) # invertidos. The colors are already included :/ 
                           #['#7D2C1B', '#DB5033', '#F4A718', '#FCEE14','#CBFE0D', '#0DFEDD', '#08C6E4', '#0A4751'] # my bad
    colors=[]
    split=inp/8.0 #divide the temperatures equally    
    
    for i in range(8):
        colors.append(split)
        split+=split
 
    #Get the current Axes instance on the current figure matching the given keyword args, or create one.
    lb.gca().invert_yaxis() 
    lb.imshow(oldTemp, cmap=cmap, origin='lower') #default: None. https://matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html
    lb.show()
#end
# Other references: 
# https://www.programcreek.com/python/example/102329/matplotlib.pyplot.pcolormesh
# https://stackoverflow.com/questions/2051744/reverse-y-axis-in-pyplot
