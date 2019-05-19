# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:56:24 2019

@author: amegessier
"""

# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from tkinter import*
from random import*

tr=0#tour de chaque joueur
grille=[["A1","A2","A3","A4","A5","A6"],["B1","B2","B3","B4","B5","B6"],["C1","C2","C3","C4","C5","C6"],["D1","D2","D3","D4","D5","D6"],["E1","E2","E3","E4","E5","E6"],["F1","F2","F3","F4","F5","F6"],["G1","G2","G3","G4","G5","G6"]]
#création de la grille
i=1
s=0

fen=Tk()

def tour():
    global tr
    global i
    n=i%2
    if n==0:
        tr=0
    else :
        tr=1
    if tr==0:
        print("C'est le tour du joueur Rouge")
    if tr==1:
        print("C'est le tour du joueur Jaune")
    i=i+1
        
def gagnerhori():
    global tr
    global gagne
    for c in range (5,-1,-1):
       for ca in range (0,4):
           if (tr==1):
               if (grille[ca][c]=="R") and (grille[ca+1][c]=="R") and (grille[ca+2][c]=="R") and (grille[ca+3][c]=="R"):
                   gagne=1
           if (tr==0):
               if (grille[ca][c]=="J") and (grille[ca+1][c]=="J") and (grille[ca+2][c]=="J") and (grille[ca+3][c]=="J"):
                   gagne=2
    print("")
    print(gagne)
    return gagne
                   
def gagnerverti():
    global tr
    global gagne
    for d in range (6,-1,-1):
        for da in range (0,3):
            if (tr==1):
                if (grille[d][da]=="R") and (grille[d][da+1]=="R") and (grille[d][da+2]=="R") and (grille[d][da+3]=="R"):
                   gagne=1
            if (tr==0):
                if (grille[d][da]=="J") and (grille[d][da+1]=="J") and (grille[d][da+2]=="J") and (grille[d][da+3]=="J"):
                   gagne=2
    return gagne

def gagnerdiagauche():
    global tr
    global gagne
    for e in range (3,7):
        for f in range (0,3):
            if (tr==1):
                if (grille[e][f]=="R") and (grille[e-1][f+1]=="R") and (grille[e-2][f+2]=="R") and (grille[e-3][f+3]=="R"):
                    gagne=1
            if (tr==0):
                if (grille[e][f]=="J") and (grille[e-1][f+1]=="J") and (grille[e-2][f+2]=="J") and (grille[e-3][f+3]=="J"):
                    gagne=2
    print("")
    return gagne
                    
def gagnerdiadroite():
    global tr
    global gagne
    for g in range (3,7):
        for h in range (0,3):
            if (tr==1):
                if (grille[g-3][h]=="R") and (grille[g-2][h+1]=="R") and (grille[g-1][h+2]=="R") and (grille[g][h+3]=="R"):
                    gagne=1
            if (tr==0):
                if (grille[g-3][h]=="J") and (grille[g-2][h+1]=="J") and (grille[g-1][h+2]=="J") and (grille[g][h+3]=="J"):
                    gagne=2
    print("")
    return gagne


                    
def jouer():
    global gagne
    global s
    s=s+1
    gagne=-1
    tour()
    gagnerhori()
    gagnerverti()
    gagnerdiagauche()
    gagnerdiadroite()
    if (gagne==1):
        print("Le joueur Rouge a gagné en",s,"tours. Bravo!")
        can.create_text(315,270,text="Le joueur Rouge a gagné en "+str(s)+" tours.\n                         Bravo!",font=("Arial",25,"bold"),fill="red")
        bouA.config(state=DISABLED)
        bouB.config(state=DISABLED)
        bouC.config(state=DISABLED)
        bouD.config(state=DISABLED)
        bouE.config(state=DISABLED)
        bouF.config(state=DISABLED)
        bouG.config(state=DISABLED)
    if (gagne==2):
        print("Le joueur Jaune a gagné en",s,"tours. Bravo!")
        can.create_text(315,270,text="Le joueur Jaune a gagné en "+str(s)+" tours.\n                         Bravo!",font=("Arial",25,"bold"),fill="yellow")
        bouA.config(state=DISABLED)        
        bouB.config(state=DISABLED)
        bouC.config(state=DISABLED)
        bouD.config(state=DISABLED)
        bouE.config(state=DISABLED)
        bouF.config(state=DISABLED)
        bouG.config(state=DISABLED)        
        
def clic1():
    global tr
    for a in range (5,-1,-1):
        if (grille[0][a]!="R") and (grille[0][a]!="J"):
            if (tr==0):
                cercle=can.create_oval(x-30,y-30,x+30,y+30,outline="red",fill="red")
                can.move(cercle,40+90*0,40+90*a)
                grille[0][a]="R"
                jouer()
                return 
            else:
                cercle=can.create_oval(x-30,y-30,x+30,y+30,outline="yellow",fill="yellow")
                can.move(cercle,40+90*0,40+90*a)
                grille[0][a]="J"
                jouer()
                return 

def clic2():
    global tr
    for a in range (5,-1,-1):
        if (grille[1][a]!="R") and (grille[1][a]!="J"):
            if (tr==0):
                cercle=can.create_oval(x-30,y-30,x+30,y+30,outline="red",fill="red")
                can.move(cercle,40+90*1,40+90*a)
                grille[1][a]="R"
                jouer()
                return 
            else:
                cercle=can.create_oval(x-30,y-30,x+30,y+30,outline="yellow",fill="yellow")
                can.move(cercle,40+90*1,40+90*a)
                grille[1][a]="J"
                jouer()
                return 
        
def clic3():
    global tr
    for a in range (5,-1,-1):
        if (grille[2][a]!="R") and (grille[2][a]!="J"):
            if (tr==0):
                cercle=can.create_oval(x-30,y-30,x+30,y+30,outline="red",fill="red")
                can.move(cercle,40+90*2,40+90*a)
                grille[2][a]="R"
                jouer()
                return 
            else:
                cercle=can.create_oval(x-30,y-30,x+30,y+30,outline="yellow",fill="yellow")
                can.move(cercle,40+90*2,40+90*a)
                grille[2][a]="J"
                jouer()
                return 
           
def clic4():
    global tr
    for a in range (5,-1,-1):
        if (grille[3][a]!="R") and (grille[3][a]!="J"):
            if (tr==0):
                cercle=can.create_oval(x-30,y-30,x+30,y+30,outline="red",fill="red")
                can.move(cercle,40+90*3,40+90*a)
                grille[3][a]="R"
                jouer()
                return 
            else:
                cercle=can.create_oval(x-30,y-30,x+30,y+30,outline="yellow",fill="yellow")
                can.move(cercle,40+90*3,40+90*a)
                grille[3][a]="J"
                jouer()
                return 
        
def clic5():
    global tr
    for a in range (5,-1,-1):
        if (grille[4][a]!="R") and (grille[4][a]!="J"):
            if (tr==0):
                cercle=can.create_oval(x-30,y-30,x+30,y+30,outline="red",fill="red")
                can.move(cercle,40+90*4,40+90*a)
                grille[4][a]="R"
                jouer()
                return 
            else:
                cercle=can.create_oval(x-30,y-30,x+30,y+30,outline="yellow",fill="yellow")
                can.move(cercle,40+90*4,40+90*a)
                grille[4][a]="J"
                jouer()
                return 
        
def clic6():
    global tr
    for a in range (5,-1,-1):
        if (grille[5][a]!="R") and (grille[5][a]!="J"):
            if (tr==0):
                cercle=can.create_oval(x-30,y-30,x+30,y+30,outline="red",fill="red")
                can.move(cercle,40+90*5,40+90*a)
                grille[5][a]="R"
                jouer()
                return 
            else:
                cercle=can.create_oval(x-30,y-30,x+30,y+30,outline="yellow",fill="yellow")
                can.move(cercle,40+90*5,40+90*a)
                grille[5][a]="J"
                jouer()
                return 
        
def clic7():
    global tr    
    for a in range (5,-1,-1):
        if (grille[6][a]!="R") and (grille[6][a]!="J"):
            if (tr==0):
                cercle=can.create_oval(x-30,y-30,x+30,y+30,outline="red",fill="red")
                can.move(cercle,40+90*6,40+90*a)
                grille[6][a]="R"
                jouer()
                return 
            else:
                cercle=can.create_oval(x-30,y-30,x+30,y+30,outline="yellow",fill="yellow")
                can.move(cercle,40+90*6,40+90*a)
                grille[6][a]="J"
                jouer()
                return 
        
bouA=Button(fen,text="Placer un jeton",command=clic1)
bouA.grid(row=1,column=0)

bouB=Button(fen,text="Placer un jeton",command=clic2)
bouB.grid(row=1,column=1)

bouC=Button(fen,text="Placer un jeton",command=clic3)
bouC.grid(row=1,column=2)

bouD=Button(fen,text="Placer un jeton",command=clic4)
bouD.grid(row=1,column=3)

bouE=Button(fen,text="Placer un jeton",command=clic5)
bouE.grid(row=1,column=4)

bouF=Button(fen,text="Placer un jeton",command=clic6)
bouF.grid(row=1,column=5)

bouG=Button(fen,text="Placer un jeton",command=clic7)
bouG.grid(row=1,column=6)

can=Canvas(fen,bg="white",width=630,height=540)
can.grid(row=7,column=0,columnspan=7)

position_ligne_v=90
position_ligne_h=90

for x in range(0,7):
    ligne_v=can.create_line(position_ligne_v + 90*x, 0, position_ligne_v + 90*x, 540,fill="blue")
for y in range(0,6):
    ligne_h=can.create_line(0, position_ligne_h + 90*y, 630, position_ligne_h + 90*y,fill="blue")


                
fen.mainloop()




#def jeton(event):
#    for b in range (5,-1,-1):
#        if tr==0: 
#            if event.x<=75 and (grille[0][b]!="R" or grille[0][b]!="J"):
#                return grille[0][b]=="R"
#            elif event.x<=150 and (grille[1][b]!="R" or grille[1][b]!="J"):
#                return grille[1][b]=="R"
#            elif event.x<=225 and (grille[2][b]!="R" or grille[2][b]!="J"):
#                return grille[2][b]=="R"
#            elif event.x<=300 and (grille[3][b]!="R" or grille[3][b]!="J"):
#                return grille[3][b]=="R"
#            elif event.x<=375 and (grille[4][b]!="R" or grille[4][b]!="J"):
#                return grille[4][b]=="R"
#            elif event.x<=450 and (grille[5][b]!="R" or grille[5][b]!="J"):
#                return grille[5][b]=="R"
#            elif event.x<=525 and (grille[6][b]!="R" or grille[6][b]!="J"):
#                return grille[6][b]=="R"
#        if tr==1: 
#            if event.x<=75 and (grille[0][b]!="R" or grille[0][b]!="J"):
#                return grille[0][b]=="J"
#            elif event.x<=150 and (grille[1][b]!="R" or grille[1][b]!="J"):
#                return grille[1][b]=="J"
#            elif event.x<=225 and (grille[2][b]!="R" or grille[2][b]!="J"):
#                return grille[2][b]=="J"
#            elif event.x<=300 and (grille[3][b]!="R" or grille[3][b]!="J"):
#                return grille[3][b]=="J"
#            elif event.x<=375 and (grille[4][b]!="R" or grille[4][b]!="J"):
#                return grille[4][b]=="J"
#            elif event.x<=450 and (grille[5][b]!="R" or grille[5][b]!="J"):
#                return grille[5][b]=="J"
#            elif event.x<=525 and (grille[6][b]!="R" or grille[6][b]!="J"):
#                return grille[6][b]=="J"







    
    