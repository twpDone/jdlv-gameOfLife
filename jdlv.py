#!/usr/bin/python2.7

import os
import copy

ENABLECOLOR=True

##### COLORS #####

WHITE="\033[47m"
BLACK="\033[47m\033[30m" # game black color
OBLACK="\033[m" # original black color
RESET="\033[m"

def testcase(row,col,tab):
    return tab[row][col]==1
 


def countNeighbor(row,col,tab,debug=False):
    neighbors=0
    for rowpos in range(row-1,row+2):
        for colpos in range(col-1,col+2):
	    if(rowpos==row and colpos==col):
                pass
            else:
                if(rowpos>=0 and colpos>=0):
                    if(debug):
                        print("Testing "+str(rowpos)+":"+str(colpos))
                    try:
                        if(testcase(rowpos,colpos,tab)):
                            neighbors+=1
                        if(debug):
                            print("neighbors="+str(neighbors))
                    except:
                        if(debug):
                            print("Except found")
    return neighbors

def rule(caseValue,neighbors,tab,debug=False):
    if(debug):
        print(neighbors)
    if(neighbors<2 or neighbors>3):
        if(debug):
            print("neighbors<2 or neighbors>3")
        return 0
    if(neighbors==2):
        if(debug):
            print("neighbors=2")
        return caseValue
    if(neighbors==3):
        if(debug):
            print("neighbors=3")
        return 1
    if(debug):
        print("stay as you are")
    return caseValue

def dispGrid(tab,color=False,debug=False):
    for row in range(0,len(tab)):
        rowLine=""
        for col in range(0,len(tab)):
            if(tab[row][col]==1):
                if(color):
                    rowLine+=BLACK
                    rowLine+="()"
                else:
                    rowLine+="*"
            else:
                if(color):
                    rowLine+=WHITE
                    rowLine+="  "
                else:
                    rowLine+=" "
            if(debug):
                print(tab[row][col])
        if(color):
            rowLine+=RESET
        print(rowLine)

def dispNeighbor(tab,color=False,debug=False):
    for row in range(0,len(tab)):
        rowLine=""
        for col in range(0,len(tab)):
            if(tab[row][col]==1):
                rowLine+=str(countNeighbor(row,col,tab,False))
            else:
                rowLine+=str(countNeighbor(row,col,tab,False))
            if(debug):
                print(tab[row][col])
        print(rowLine)

def playTurn(tab,color=False,debug=False):
    newtab=copy.deepcopy(tab)
    for row in range(0,len(tab)):
        for col in range(0,len(tab)):
            newtab[row][col]=rule(tab[row][col],countNeighbor(row,col,tab),tab,debug=False)
    return newtab

def saveGridOnFile(tab,filename):
    f=open(filename,"w")
    for row in range(0,len(tab)):
        for col in range(0,len(tab)):
            f.write(str(tab[row][col]))
        f.write("\n")
    f.close()

def readGridFromFile(filename):
    tab=[]
    tab.append([])
    f=open(filename,"r")
    print("Fichier "+filename+" ouvert")
    end=False
    while(end==False):
        char=f.read(1)
        if(char=="0"):
            tab[len(tab)-1].append(0)
        if(char=="1"):
            tab[len(tab)-1].append(1)
        if(char=="\n"):
            tab.append([])
        if(char==""):
            end=True
    f.close()
    if(len(tab[len(tab)-1])==0):
        removed=tab.pop()
    print("Fichier "+filename+" Importe")
    print("Grid["+str(len(tab))+"]["+str(len(tab[0]))+"]")
    return tab

def gridGen(dim):
    tab=[]
    for d in range(0,dim):
        tab.append([])
        for d2 in range(0,dim):
            tab[d].append("0")
    return tab

def initGrid():
    tab=gridGen(18)
    tab[0][1]=1
    tab[1][2]=1
    tab[2][0]=1
    tab[2][1]=1
    tab[2][2]=1
    return tab

def initFile():
    tab2=initGrid()
    print(len(tab2))
    saveGridOnFile(tab2,"saveGrid")

def instruction():
    print("Type r to read grid from file")
    print("Type i to create a new demo grid")
    print("Type s to save grid to file")
    print("Type q to Quit")
    print("Press enter to play one turn in the game of life")

instruction()
cont=""
while(cont!="q"):
    cont=raw_input()
    if(cont=="r"):
        try:
            tab=readGridFromFile("saveGrid2")
            dispGrid(tab,color=ENABLECOLOR,debug=False)
        except:
            tab=initGrid()
    elif(cont=="i"):
        tab=initGrid()
        dispGrid(tab,color=ENABLECOLOR,debug=False)
    elif(cont=="s"):
        saveGridOnFile(tab,"saveGrid2")
	print("Grid saved in file : saveGrid2")
        dispGrid(tab,color=ENABLECOLOR,debug=False)
    else:
	try:
            print(" ")
            os.system("clear")
            print(" ")
            tab=playTurn(tab,color=ENABLECOLOR,debug=False)
            dispGrid(tab,color=ENABLECOLOR,debug=False)
        except:
            instruction()

os.system("clear")


