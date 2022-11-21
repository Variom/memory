# Komaryan et Lucas

from turtle import *
import random,time,math

########## Autre ##########

def mouse_pos(x,y,): # Fonction qui renvoie la postion de la souris.
    c = (x,y)
    move(c,te)
    print(x,y)

def C(x,y): # Fonction qui convertit la resolution 720p (utilise pour la creation du jeu) en la resoltuion de l'utilisateur.
    x = x*(L/1280)
    y = y*(l/720)
    return(x,y)

def move(c,t): # Fonction deplacement d'une tortue, "c" etant un couple de coordonnees (x,y).
    t.up()
    t.goto(c)
    t.down()

########## Dessin ##########

def drawing(L,t): # Fonction qui dessine une forme a partir d'une liste de coordonnees. On se deplace d'abord sur le premier point sans dessiner puis on se deplace sur les autres en dessinant.
    move(C(L[0][0],L[0][1]),t)
    t.color(L[-1])
    t.begin_fill()
    for i in range(1,len(L)-1):
        t.goto(C(L[i][0],L[i][1]))
    t.end_fill()

def rectangle(coord,L,l,color,width,t,filled): # Fonction qui trace un rectangle plein ou vide.
    t.color(color)
    tracer(0)
    move(coord,t)
    t.width(width)
    t.seth(0)
    if filled:
        t.begin_fill()
    for i in range(2):
        t.forward(L)
        t.left(90)
        t.forward(l)
        t.left(90)
    tracer(1)
    if filled:
        t.end_fill()
    
def parallelogram(length,x,y,color,angle,border,t): # Fonction qui dessine un parallélogramme.
    rad = math.radians(angle)
    length2 = length/math.cos(rad)
    c = (x,y)
    move(c,t)
    t.color("white")
    if not border:
        t.color(color)
    t.seth(0)
    t.begin_fill()
    t.left(angle)
    for i in range(2):
        t.forward(length)
        t.left(90-angle)
        t.forward(length2)
        t.left(angle+90)
    t.color(color)
    t.end_fill()

def square(length,x,y,color,t): # Fonction qui dessine un carré.
    c = (x,y)
    move(c,t)
    t.color(color)
    t.seth(0)
    t.begin_fill()
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()

########## Box ##########

def drawBox(index,t): # Fonction qui dessine une case avec la bonne orientation et la bonne couleur en fonction de son indice.
    if BOX[index][2] >= 17 and BOX[index][2] < 25:
        parallelogram(C(45,0)[0],C(BOX[index][0],0)[0],C(0,BOX[index][1])[1],BOX[index][4],26,True,t)
        t.color("white")
        t.write("")# N'a pas de sens mais à cause d'un bug de time.sleep(), le programme ne fonctionne plus si on l'enlève.
    elif BOX[index][2] == 25:
        parallelogram(C(45,0)[0],C(BOX[index][0],0)[0],C(0,BOX[index][1])[1],BOX[index][4],35,True,t)
        t.color("white")
        t.write("")
    else :
        parallelogram(C(50,0)[0],C(BOX[index][0],0)[0],C(0,BOX[index][1])[1],BOX[index][4],-3,True,t)
        t.color("white")
        t.write("")

def allBoxesExceptDone(t): # Fonction qui dessine toutes les cases sauf aux endroits où l'on a déja découvert le minerais.
    global working
    working = True
    for i in range(len(BOX)):
        if BOX[i][3] == 0:
            drawBox(i,t)
    working = False

def list_box(): # Fonction qui crée la liste des coordonées des cases avec en plus la couleur associée, le rang et l'état de la case à partir de coordonnées prédéfinies pour la position des cases et minerais.
    global BOX
    BOX = [[-580,-11],[-520,184],[-461,33],[-359,176],[-305,120],[-193,278],[-174,-132],[-110,170],[-110,0],[218,-10],[270,244],[269,-14],[320,-69],[419,135],[520,244],[540,10],[-58,-138],[-59,167],[-20,20],[51,7],[103,286],[205,92],[-510,-72],[15,135],[422,-175],[-470,-53],[-258,28],[118,73],[321,90],[558,-115]]
    for i in range(len(BOX)):
        BOX[i].append(i+1)
        BOX[i].append(0)
        if i+1 >= 1 and i+1 <= 16:
            BOX[i].append("#989898")
        if i+1 >= 17 and i+1 <= 22:
            BOX[i].append("#B1B1B1")
        if i+1 >= 23 and i+1 <= 25:
            BOX[i].append("#757575")
        if i+1 >= 26 and i+1 <= 30:
            BOX[i].append("#696969")
    random.shuffle(BOX)
    for i in range(D*10):
        if BOX[i][3] == 0:
            BOX[i].append(i+1)
    BOX = BOX[0:D*10]

########## Ore ##########

def drawOre(l,lmatrix,index,t): # Dessine un minerais avec la bonne orientation et position en fonction de son indice.
    global working
    working = True
    tup = C(l[index][0],l[index][1])
    if l[index][2] >= 17 and l[index][2] < 25:
        drawTexturePers(lmatrix[index],tup[0],tup[1],C(45,0)[0],26,t)
    elif l[index][2] == 25:
        drawTexturePers(lmatrix[index],tup[0],tup[1],C(45,0)[0],35,t)
    else:
        drawTexturePers(lmatrix[index],tup[0],tup[1],C(50,0)[0],-3,t)
    working = False

def ores(nb): # Fonction qui crée deux listes de matrices.
    global ingot,funct
    funct = [[bluer,1],[bluer,100],[bluer,-100],[reder,100],[reder,-100],[greener,100],[greener,-100],[bluer,-370,reder,130],[bluer,-110,greener,-30,reder,-110],[bluer,-140,greener,-120,reder,-20],[reder,-140,greener,-120,bluer,-20],[reder,70,greener,-130,bluer,-130],[reder,-10,greener,40,bluer,-160],[greener,-170,reder,80],["random"]]
    ingot = [] # Liste de matrice de lingot.   
    output = [] # Liste de matrice de minerais.
    random.shuffle(funct) # On mélange funct.
    funct = funct[0:nb]*2 # On la coupe au nombre de minerais qu'on veut puis on la multiplie par deux pour avoir des paires.
    random.shuffle(funct) # On re-mélange funct.

    ## Création de la couleur aléatoire ##
    rainbow = []
    for z in range(16):
        colour = ["random"]
        while colour == ["random"]:
            colour = random.choice(funct)
        rainbow.append(colour)

    ## Remplissage des listes ingot et output ##  
    for i in range(len(funct)):
        # Modèles en noir et blanc des matrices.
        ore_ingot = [['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', (251, 251, 249), (160,160,160), 'rien', 'rien', 'rien', 'rien', (160,160,160), (160,160,160), 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (251, 251, 249), (255, 255, 255), (251, 251, 249), (210,210,210), (210,210,210), (160,160,160), 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (251, 251, 249), (160,160,160), 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', (210,210,210), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (251, 251, 249), (160,160,160), (160,160,160), (160,160,160), 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', (251, 251, 249), (210,210,210), 'rien', 'rien', 'rien', 'rien', 'rien', (255, 255, 255), (251, 251, 249), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', (255, 255, 255), (251, 251, 249), (210,210,210), (165,165,165), (160,160,160), 'rien', 'rien', (210,210,210), (160,160,160), 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', (255, 255, 255), (251, 251, 251), 'rien', 'rien', 'rien', (255, 255, 255), (251, 251, 249), 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (251, 251, 249), (160,160,160), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', (210,210,210), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (251, 251, 249), (210,210,210), 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien']]
        gotgot = [['rien', 'rien', 'rien', (68, 68, 68), (53, 53, 53), (53, 53, 53), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', (68, 68, 68), (130, 130, 130), (127, 127, 127), (114, 114, 114), (53, 53, 53), (53, 53, 53), (53, 53, 53), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', (68, 68, 68), (130, 130, 130), (130, 130, 130), (127, 127, 127), (114, 114, 114), (114, 114, 114), (114, 114, 114), (114, 114, 114), (53, 53, 53), (53, 53, 53), (53, 53, 53), 'rien', 'rien', 'rien', 'rien'], [(68, 68, 68), (130, 130, 130), (130, 130, 130), (168, 168, 168), (127, 127, 127), (150, 150, 150), (150, 150, 150), (150, 150, 150), (114, 114, 114), (114, 114, 114), (114, 114, 114), (104, 104, 104), (53, 53, 53), (53, 53, 53), (53, 53, 53), 'rien'], [(68, 68, 68), (216, 216, 216), (216, 216, 216), (168, 168, 168), (127, 127, 127), (150, 150, 150), (150, 150, 150), (150, 150, 150), (150, 150, 150), (150, 150, 150), (114, 114, 114), (114, 114, 114), (114, 114, 114), (114, 114, 114), (114, 114, 114), (53, 53, 53)], [(68, 68, 68), (255, 255, 255), (216, 216, 216), (150, 150, 150), (216, 216, 216), (104, 104, 104), (104, 104, 104), (104, 104, 104), (150, 150, 150), (150, 150, 150), (150, 150, 150), (150, 150, 150), (150, 150, 150), (114, 114, 114), (114, 114, 114), (53, 53, 53)], [(68, 68, 68), (255, 255, 255), (150, 150, 150), (216, 216, 216), (216, 216, 216), (216, 216, 216), (216, 216, 216), (216, 216, 216), (104, 104, 104), (104, 104, 104), (104, 104, 104), (150, 150, 150), (150, 150, 150), (150, 150, 150), (150, 150, 150), (53, 53, 53)], [(68, 68, 68), (150, 150, 150), (255, 255, 255), (255, 255, 255), (255, 255, 255), (216, 216, 216), (216, 216, 216), (216, 216, 216), (216, 216, 216), (216, 216, 216), (216, 216, 216), (104, 104, 104), (104, 104, 104), (104, 104, 104), (104, 104, 104), (53, 53, 53)], ['rien', (68, 68, 68), (68, 68, 68), (68, 68, 68), (168, 168, 168), (255, 255, 255), (255, 255, 255), (216, 216, 216), (216, 216, 216), (216, 216, 216), (216, 216, 216), (216, 216, 216), (216, 216, 216), (168, 168, 168), (68, 68, 68), 'rien'], ['rien', 'rien', 'rien', 'rien', (68, 68, 68), (68, 68, 68), (68, 68, 68), (168, 168, 168), (255, 255, 255), (216, 216, 216), (216, 216, 216), (216, 216, 216), (168, 168, 168), (68, 68, 68), 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (68, 68, 68), (68, 68, 68), (68, 68, 68), (168, 168, 168), (168, 168, 168), (68, 68, 68), 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (68, 68, 68), (68, 68, 68), 'rien', 'rien', 'rien', 'rien']]
        diams = [['rien', 'rien', 'rien', (48, 48, 48), (48, 48, 48), (48, 48, 48), (48, 48, 48), (48, 48, 48), (48, 48, 48), 'rien', 'rien', 'rien'], ['rien', 'rien', (48, 48, 48), (132, 132, 132), (182, 182, 182), (182, 182, 182), (182, 182, 182), (182, 182, 182), (132, 132, 132), (48, 48, 48), 'rien', 'rien'], ['rien', (48, 48, 48), (195, 195, 195), (109, 109, 109), (182, 182, 182), (182, 182, 182), (182, 182, 182), (182, 182, 182), (109, 109, 109), (132, 132, 132), (48, 48, 48), 'rien'], ['rien', (48, 48, 48), (212, 212, 212), (109, 109, 109), (182, 182, 182), (182, 182, 182), (182, 182, 182), (182, 182, 182), (109, 109, 109), (182, 182, 182), (48, 48, 48), 'rien'], [(48, 48, 48), (255, 255, 255), (212, 212, 212), (212, 212, 212), (132, 132, 132), (132, 132, 132), (132, 132, 132), (132, 132, 132), (182, 182, 182), (182, 182, 182), (132, 132, 132), (48, 48, 48)], [(48, 48, 48), (255, 255, 255), (241, 241, 241), (182, 182, 182), (225, 225, 225), (225, 225, 225), (225, 225, 225), (225, 225, 225), (132, 132, 132), (109, 109, 109), (109, 109, 109), (48, 48, 48)], [(48, 48, 48), (255, 255, 255), (230, 230, 230), (241, 241, 241), (225, 225, 225), (225, 225, 225), (225, 225, 225), (225, 225, 225), (132, 132, 132), (212, 212, 212), (195, 195, 195), (48, 48, 48)], [(48, 48, 48), (255, 255, 255), (230, 230, 230), (255, 255, 255), (225, 225, 225), (225, 225, 225), (225, 225, 225), (225, 225, 225), (132, 132, 132), (212, 212, 212), (48, 48, 48), 'rien'], ['rien', (48, 48, 48), (255, 255, 255), (230, 230, 230), (255, 255, 255), (241, 241, 241), (241, 241, 241), (241, 241, 241), (212, 212, 212), (195, 195, 195), (48, 48, 48),'rien'], ['rien', (48, 48, 48), (255, 255, 255), (241, 241, 241), (230, 230, 230), (230, 230, 230), (255, 255, 255), (212, 212, 212), (212, 212, 212), (48, 48, 48), 'rien', 'rien'], ['rien', 'rien', (48, 48, 48), (255, 255, 255), (230, 230, 230), (230, 230, 230), (230, 230, 230), (241, 241, 241), (195, 195, 195), (48, 48, 48), 'rien', 'rien'], ['rien', 'rien', 'rien', (48, 48, 48), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (48, 48, 48), 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', (48, 48, 48), (48, 48, 48), (48, 48, 48), (48, 48, 48),'rien', 'rien', 'rien', 'rien']]
        ore_emerald = [['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', (165,165,165), (100,100,100), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', (251, 251, 251), (165,165,165), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (165,165,165), (100,100,100), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (251, 251, 251), (148, 148, 148), 'rien', 'rien', 'rien', 'rien', (165,165,165), (100,100,100), 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (165,165,165), (100,100,100), 'rien', (251, 251, 251), (165,165,165), 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', (165,165,165), (100,100,100), 'rien', 'rien', (251, 251, 251), (165,165,165), 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', (251, 251, 251), (165,165,165), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', (165,165,165), (100,100,100), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', (165,165,165), (100,100,100), (251, 251, 251), (165,165,165), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', (251, 251, 251), (165,165,165), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (165,165,165), (100,100,100), 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (242, 242, 242), (165,165,165), 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', (165,165,165), (100,100,100), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', (251, 251, 251), (165,165,165), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien']]

        repeated = False
        
        # Savoir si on a déja utilisé la couleur sur laquelle on est.
        if i+1 < len(funct):
            for k in range(i+1,len(funct)):
                if funct[i] == funct[k]:
                    repeated = True

        # Si on a utlisé la couleur et que la couleur n'est pas random, on applique la couleur à un type de minerais.
        if not repeated and funct[i] != ["random"]:
            for j in range(0,len(funct[i]),2):
                ore_ingot = funct[i][j](ore_ingot,funct[i][j+1])
                gotgot = funct[i][j](gotgot,funct[i][j+1])
            output.append(ore_ingot)
            ingot.append(gotgot)
            
        # Si on a pas utlisé la couleur et que la couleur n'est pas random, on applique la couleur à un autre type de minerais.    
        elif repeated and funct[i] != ["random"]:            
            for j in range(0,len(funct[i]),2):
                ore_emerald = funct[i][j](ore_emerald,funct[i][j+1])  
                diams = funct[i][j](diams,funct[i][j+1])          
            output.append(ore_emerald)
            ingot.append(diams)
        
        # Si on a utlisé la couleur et que la couleur est random, on applique la couleur arc-en-ciel à un type de minerais.
        elif not repeated and funct[i] == ["random"]:
            for z in range(len(ore_ingot)):
                for j in range(0,len(rainbow[z]),2):
                    ore_ingot[z:z+1] = rainbow[z][j](ore_ingot[z:z+1],rainbow[z][j+1])
                    gotgot[z:z+1] = rainbow[z][j](gotgot[z:z+1],rainbow[z][j+1])
            output.append(ore_ingot)
            ingot.append(gotgot)
        
        # Si on a pas utlisé la couleur et que la couleur est random, on applique la couleur arc-en-ciel à un autre type de minerais.
        else:
            for z in range(len(ore_emerald)):
                for j in range(0,len(rainbow[z]),2):
                    ore_emerald[z:z+1] = rainbow[z][j](ore_emerald[z:z+1],rainbow[z][j+1])
                    diams[z:z+1] = rainbow[z][j](diams[z:z+1],rainbow[z][j+1])
            output.append(ore_emerald)
            ingot.append(diams)             
    return output

def coord_ore(): # Fonction qui cree une liste de coordonees necessaires pour faire apparaitre les lingots trouves dans le minecart 1.
    coord_ore = []
    for i in range(D*10):
        if i < D*5:
            coord_ore.append((-500-i*(140/(D*5)),(-190)-i*(45/(D*5))))
        else:
            coord_ore.append((-435-(i-D*5)*(140/(D*5)),(-190)-(i-D*5)*(45/(D*5))))
    return coord_ore

########## Textures ##########
    
def drawTexture(matrix,x,y,size,t): # Fonction qui dessine une texture à partir d'une matrice de couleur.
    global working
    working = True
    squaresize = size//len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != "rien":
                square(squaresize,x+j*squaresize,y+i*squaresize,matrix[i][j],t)
    working = False

def drawTexturePers(matrix,x,y,size,angle,t): # Fonction qui dessine une texture à partir d'une matrice de couleur mais avec un orientation particulière en utilisant un angle différent sur la fonction parallélogram.
    rad = math.radians(angle)
    length = size/len(matrix[0])    
    length2 = length*math.cos(rad)
    shift = length * math.sin(rad)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != "rien":
                parallelogram(round(length),round(x+j*length2),round(y+i*length+j*shift),matrix[i][j],angle,False,t)

def greener(matrix,nb): # Fonction qui rend une matrice plus ou moins verte.
    uniqcolor = [] # Liste qui prend chaque couleur différente présente dans la matrice en un seul exemplaire.
    
    # On prend la couleur si elle n'a pas été déja prise, pour avoir un seul exemplaire de chaque couleur.
    for i in range(len(matrix)): 
        for j in range(len(matrix[0])):
            if matrix[i][j] != "rien" and matrix[i][j] not in uniqcolor:
                uniqcolor.append(matrix[i][j])
    # Pour chaque couleur on applique une modification sur la valeur de vert en RGB. La liste reshade contient la couleur originale puis la couleur modifiée.
    reshade = []        
    for i in uniqcolor:
        reshade.append(i)
        a = i[1] + nb
        if a > 255:
            a = 255
        elif a < 0:
            a = 0
        reshade.append((i[0],a,i[2]))
    # On re-crée la matrice en remplaçant toutes les couleurs originales par leurs couleurs reshades.
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != "rien":
                matrix[i][j] = reshade[reshade.index(matrix[i][j])+1]
    return matrix

def bluer(matrix,nb): # Raisonnement analogue à greener (voir ci-dessus).
    uniqcolor = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != "rien" and matrix[i][j] not in uniqcolor:
                uniqcolor.append(matrix[i][j])

    reshade = []           
    for i in uniqcolor:
        reshade.append(i)
        a = i[2] + nb
        if a > 255:
            a = 255
        elif a < 0:
            a = 0
        reshade.append((i[0],i[1],a))
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != "rien":
                matrix[i][j] = reshade[reshade.index(matrix[i][j])+1]
    return matrix

def reder(matrix,nb): # Raisonnement analogue à greener (voir ci-dessus).
    uniqcolor = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != "rien" and matrix[i][j] not in uniqcolor:
                uniqcolor.append(matrix[i][j])

    reshade = []           
    for i in uniqcolor:
        reshade.append(i)
        a = i[0] + nb
        if a > 255:
            a = 255
        elif a < 0:
            a = 0
        reshade.append((a,i[1],i[2]))
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != "rien":
                matrix[i][j] = reshade[reshade.index(matrix[i][j])+1]
    return matrix

########## Decor ##########

# Pour toutes les fonctions décor, on crée une liste de points sur lesquelles la tortue va se déplacer et créer la forme souhaitée. Le dernier élément de la liste est la couleur.

def ground_front(t):
    L = [(-640,-360),(-640,-163),(0,-206),(-113,-268),(640,-328),(640,-360),"#A8A8A8"]
    drawing(L,t)

def ground_back(t):
    L = [(0,-206),(0,-327),(-248,-327),(-248,-206),"#848484"]
    drawing(L,t)

def left1_wall_front(t):
    L = [(-640,-100),(-585,-104),(-585,-12),(-532,-16),(-532,35),(-360,26),(-360,120),(-255,117),(-255,171),(-59,167),(-59,360),(-640,360),"#989898"]
    drawing(L,t)

def left2_wall_front(t):
    L = [(-415,-116),(-59,-142),(-59,50),(-200,54),(-200,-33),(-256,-30),(-256,-77),(-415,-65),"#989898"]
    drawing(L,t)
    
def middle_wall_front(t):
    L = [(-59,-142),(-59,50),(52,106),(52,55),(93,77),(93,32),(169,71),(169,272),(-59,167),(-59,360),(392,360),(392,95),"#B1B1B1"]
    drawing(L,t)
    
def right_wall_front(t):
    L = [(220,-163),(420,-180),(420,-81),(470,-85),(470,-37),(590,-45),(590,5),(640,2),(640,360),(220,360),(220,198),(366,194),(366,136),(420,134),(420,29),(220,37),"#989898"]
    drawing(L,t)

def left_wall_back1(t):
    L = [(-585,-104),(-415,-116),(-110,-91),(-110,258),(-602,172),"#686868"]
    drawing(L,t)

def left_wall_back2(t):
    L = [(-110,-49),(190,30),(188,318),(-110,251),"#757575"]
    drawing(L,t)

def left_wall_back3(t):
    L = [(-200,54),(-59,50),(52,106),(-70,110),"#8F8F8F"]
    drawing(L,t)

def left_wall_back4(t):
    L = [(93,77),(40,79),(59,40),"#8F8F8F"]
    drawing(L,t)

def left_wall_back5(t):
    L = [(169,71),(60,72),(60,278),(169,271),"#696969"]
    drawing(L,t)
    
def left_wall_back6(t):
    L = [(169,71),(60,72),(56,70),(93,32),"#8C8C8C"]
    drawing(L,t)

def left_wall_back7(t):
    L = [(-255,171),(-255,117),(-159,159),(-159,170),"#828282"]
    drawing(L,t)
    
def left_wall_back8(t):
    L = [(-360,26),(-257,78),(-257,132),(-371,130),"#828282"]
    drawing(L,t)

def left_wall_back9(t):
    L = [(-415,-65),(-299,-15),(-198,-22),(-195,-88),"#7A7A7A"]
    drawing(L,t)

def left_wall_back11(t):
    L = [(-256,-30),(-194,4),(-196,-46),"#737373"]
    drawing(L,t)

def left_wall_back10(t):
    L = [(-532,-16),(-441,30),(-543,43),"#828282"]
    drawing(L,t)

def left_wall_back12(t):
    L = [(-585,-104),(-470,-55),(-470,50),(-585,-12),"#767676"]
    drawing(L,t)

def left_wall_back13(t):
    L = [(-470,-55),(-357,-65),(-413,-116),(-585,-104),"#7A7A7A"]
    drawing(L,t)

def right_wall_back1(t):
    L = [(220,37),(322,90),(420,86),(420,29),"#888888"]
    drawing(L,t)

def right_wall_back2(t):
    L = [(322,90),(322,224),(420,236),(420,86),"#686868"]
    drawing(L,t)

def right_wall_back3(t):
    L = [(420,-180),(510,-112),(510,-21),(420,-75),"#757575"]
    drawing(L,t)

def right_wall_back4(t):
    L = [(420,-180),(640,-197),(640,-120),(510,-112),"#828282"]
    drawing(L,t)

def right_wall_back5(t):
    L = [(510,-112),(510,11),(640,16),(640,-120),"#5E5E5E"]
    drawing(L,td)

def right_wall_back6(t):
    L = [(470,-85),(540,-40),(590,-45),(640,-9),(640,8),(570,17),(467,-36),"#7E7E7E"]
    drawing(L,t)

def lava(t):
    L = [(-640,-99),(-59,-142),(346,79),(640,55),(640,-358),(-640,-358),"#ff7b19"]
    drawing(L,t)

def torche(t): # Fonction qui dessine quelque torches grâce à drawtexture. C'est l'élément qui se répète x fois dans notre décor.
    torche = [['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (103, 82, 49), (55, 42, 23), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (152, 120, 73), (59, 46, 27), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (103, 82, 49), (61, 48, 29), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (151, 119, 72), (60, 47, 28), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (159, 127, 80), (64, 51, 32), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (149, 117, 70), (66, 53, 34), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (147, 115, 68), (60, 47, 28), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (124, 98, 62), (76, 61, 38), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (255, 255, 151), (255, 255, 255), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (255, 216, 0), (255, 143, 0), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien']]
    L = [(-51,86),(-468,-91),(-292,-26),(500,-172),(256,42)]
    for i in range(len(L)):
        drawTexture(torche,C(L[i][0],0)[0],C(0,L[i][1])[1],C(50,0)[0],t)

def minecart_front(x,y,t,color): # Fonction qui dessine le devant du minecart. Le minecart est l'élément qui se répète 2 fois dans notre décor.
    Color = [("#6F9FBC","#6189A0"),("#BC6464","#A05656")]
    L = [(1+x,10+y),(137+x,72+y),(137+x,154+y),(1+x,102+y),Color[color][0]]
    drawing(L,td)
    L = [(1+x,102+y),(-139+x,109+y),(-139+x,19+y),(1+x,10+y),Color[color][1]]
    drawing(L,td)

def minecart_back(x,y,t): # Fonction qui dessine l'arrière du minecart. Le minecart est l'élément qui se répète 2 fois dans notre décor.
    L = [(x,y),(137+x,64+y),(-18+x,77+y),(-140+x,10+y),"#909090"] # mettre toutes le coordonnees centrees en 0.
    drawing(L,td)
    L = [(137+x,72+y),(137+x,154+y),(-1+x,162+y),(-1+x,78+y),"#848484"]
    drawing(L,td)
    L = [(-1+x,162+y),(-139+x,109+y),(-139+x,56+y),(-1+x,78+y),"#9D9D9D"]
    drawing(L,td)
    L = [(21+x,22+y),(41+x,20+y),(55+x,26+y),(57+x,38+y),(89+x,52+y),(107+x,50+y),(119+x,56+y),(122+x,69+y),"#4B4B4B"]
    drawing(L,td)

def decor(): # On utilise toutes les fonctions décor d'un coup.
    global working
    working = True
    lava(td)
    ground_back(td)
    ground_front(td)
    left_wall_back1(td)
    left_wall_back2(td)
    left_wall_back3(td)
    left_wall_back5(td)
    left_wall_back6(td)
    left_wall_back4(td)
    left_wall_back8(td)
    left_wall_back7(td)
    left_wall_back13(td)
    left_wall_back12(td)
    left_wall_back9(td)
    left_wall_back10(td)
    left_wall_back11(td)
    left1_wall_front(td)
    left2_wall_front(td)
    middle_wall_front(td)
    right_wall_back1(td)
    right_wall_back2(td)
    right_wall_back3(td)
    right_wall_back4(td)
    right_wall_back5(td)
    right_wall_back6(td)
    right_wall_front(td)
    torche(td)
    for i in range(2): # On utilise un boucle for pour déssiner les deux minecart.
        c =(-490,-300)
        T = [tc1,tc2]
        minecart_back(c[0]+i*210,c[1]-i*20,T[i])
        minecart_front(c[0]+i*210,c[1]-i*20,T[i],i)
    working = False

########## Interface ##########

def menu(): # Fonction qui affiche le menu.
    L = [("MEMOCRAFT",(0,200),70),("Quelle difficulte voulez-vous choisir ?",(0,150),33),("Tentatives",(0,50),25),("Facile (10)",(0,0),20),("Normal (18)",(0,-50),20),("Difficile (26)",(0,-100),20),("START",(0,-220),60),("Quitter",(0,-300),30)]
    bgcolor("#848484")
    te.color("white")
    for i in range(len(L)):
        move(C(L[i][1][0],L[i][1][1]),te)
        te.write(L[i][0], align="center", font=("Fixedsys",L[i][2], "bold"))
    goldOre = [['rien', 'rien', 'rien', (255, 255, 181), (248, 175, 43), 'rien', 'rien', 'rien', 'rien', (248, 175, 43), (248, 175, 43), 'rien', 'rien', 'rien', 'rien', 'rien'],['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (255, 255, 181), (255, 255, 255), (255, 255, 181), (252, 238, 75), (252, 238, 75), (248, 175, 43), 'rien', 'rien'],['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (255, 255, 181), (248, 175, 43), 'rien', 'rien', 'rien'],['rien', 'rien', 'rien', 'rien', (252, 238, 75), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'],['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (255, 255, 181), (248, 175, 43), (248, 175, 43), (248, 175, 43), 'rien', 'rien', 'rien', 'rien', 'rien'],['rien', (255, 255, 181), (252, 238, 75), 'rien', 'rien', 'rien', 'rien', 'rien', (255, 255, 255), (255, 255, 181), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'],['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'],['rien', 'rien', 'rien', (255, 255, 255), (255, 255, 181), (252, 238, 75), (252, 238, 75), (248, 175, 43), 'rien', 'rien', (252, 238, 75), (248, 175, 43), 'rien', 'rien', 'rien', 'rien'],['rien', 'rien', 'rien', 'rien', 'rien', (255, 255, 255), (255, 255, 181), 'rien', 'rien', 'rien', (255, 255, 255), (255, 255, 181), 'rien', 'rien', 'rien', 'rien'],['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'],['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (255, 255, 181), (248, 175, 43), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'],['rien', 'rien', 'rien', 'rien', (252, 238, 75), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (255, 255, 181), (252, 238, 75), 'rien', 'rien']]
    tup1 = C(-530,-240)
    tup2 = C(210,-200)
    drawTexture(pioche,tup1[0],tup1[1],C(300,0)[0],te)
    drawTexture(goldOre,tup2[0],tup2[1],C(270,0)[0],te)

def endingscreen(): # Fonction qui enlève tous les dessins et qui affiche un message de fin suivant la fin de la partie.
    global working
    working = True
    move((0,0),te)
    move(C(150,-250),te)
    te.color("white")
    if count == D*10:
        te.write("Bravo !", align="center", font=("Fixedsys",75,"italic"))
    elif tent_rest == 0:
        te.write("Perdu :(", align="center", font=("Fixedsys",75,"italic"))
    update()
    time.sleep(3)
    for i in T:
        i.clear()
    menu()
    working = False

def progression_bar(use): # Fonction qui à partir des tentatives restantes dessine les pioches dans le minecart 2, use est le nombre de tentative deja utilisee pour trouver les minerais. On définit aussi la difficulté en fonction su nombre de tentative dans cette fonction.
    global tent_rest,working
    working = True
    #pioche = [['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', (104, 78, 30), (40, 30, 11), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', (73, 54, 21), (137, 103, 39), (40, 30, 11), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', (73, 54, 21), (104, 78, 30), (40, 30, 11), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', (73, 54, 21), (137, 103, 39), (40, 30, 11), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (14, 63, 54), 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', (73, 54, 21), (104, 78, 30), (40, 30, 11), 'rien', 'rien', 'rien', 'rien', (14, 63, 54), (51, 235, 203), (14, 63, 54), 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', (73, 54, 21), (137, 103, 39), (40, 30, 11), 'rien', 'rien', 'rien', (14, 63, 54), (43, 199, 172), (14, 63, 54), 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (73, 54, 21), (104, 78, 30), (40, 30, 11), 'rien', 'rien', (14, 63, 54), (39, 178, 154), (14, 63, 54), 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (73, 54, 21), (137, 103, 39), (40, 30, 11), 'rien', (14, 63, 54), (39, 178, 154), (14, 63, 54), 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (73, 54, 21), (104, 78, 30), (40, 30, 11), (39, 178, 154), (43, 199, 172), (14, 63, 54), 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (73, 54, 21), (43, 199, 172), (39, 178, 154), (14, 63, 54), 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', (14, 63, 54), (14, 63, 54), (14, 63, 54), (14, 63, 54), (39, 178, 154), (39, 178, 154), (137, 103, 39), (40, 30, 11), 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', (14, 63, 54), (51, 235, 203), (43, 199, 172), (39, 178, 154), (39, 178, 154), (43, 199, 172), (14, 63, 54), (73, 54, 21), (104, 78, 30), 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', (14, 63, 54), (14, 63, 54), (14, 63, 54), (14, 63, 54), (14, 63, 54), 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien']]
    coordonnee =[(-290,-215),(-225,-215)]
    tc2.clear()
    minecart_back(-280,-320,tc2)
    tent_tot = (10+(D-1)*8)
    tent_rest = tent_tot - use
    for i in range(tent_rest):
        if i < tent_tot/2:
            drawTexture(pioche,C(coordonnee[0][0]+i*(-131/(tent_tot/2)),0)[0],C(0,coordonnee[0][1]+i*(-45/(tent_tot/2)))[1],C(70,0)[0],tmp)
        else:
            drawTexture(pioche,C(coordonnee[1][0]+(i-(tent_tot/2))*(-150/(tent_tot/2)),0)[0],C(0,coordonnee[1][1]+(i-(tent_tot/2))*(-47/(tent_tot/2)))[1],C(70,0)[0],tmp)
    minecart_front(-280,-320,tc2,1)
    working = False

########## Autre ##########

def getclickedcard(x,y): # Fonction qui a partir des coordonnees du clic et des coordonnees des cases, renvoie l'indice de la case cliquee.
    for i in range(len(BOX)):
        if 17 <= BOX[i][2] <= 25:
            if C(BOX[i][0],69)[0] <= x <= C(BOX[i][0]+45*math.cos(math.radians(26)),69)[0] and C(0,BOX[i][1])[1] <= y <= C(0,BOX[i][1]+45/math.cos(math.radians(26))+45*math.sin(math.radians(26)))[1]:
                return i
        else:
            if C(BOX[i][0],69)[0] <= x <= C(BOX[i][0]+45*math.cos(math.radians(-3)),69)[0] and C(0,BOX[i][1])[1] <= y <= C(0,BOX[i][1]+45/math.cos(math.radians(-3))+45*math.sin(math.radians(-3)))[1]:
                return i

########## Jeu ##########

def game(x,y): # Fonction utilisée avec le screen.onclick et qui utilise l'ensemble des fonctions précédentes. On peut donc intéragir avec le jeu grâce à la souris (niveau 2+).
    global menu_ok,D,use,count,ore,ingot_list
    if not working:
        if menu_ok == 0:
            if x > C(-135,0)[0] and x < C(135,0)[0] and y < C(0,40)[1] and y > C(0,-10)[1]:
                tmp.clear()
                D = 1
                rectangle(C(-135,-15),C(270,0)[0],C(0,50)[1],"white",4,tmp,False)
            if x > C(-135,0)[0] and x < C(135,0)[0] and y < C(0,-10)[1] and y > C(0,-60)[1]:
                tmp.clear()
                D = 2
                rectangle(C(-135,-65),C(270,0)[0],C(0,50)[1],"white",4,tmp,False)
            if x > C(-135,0)[0] and x < C(135,0)[0] and y < C(0,-60)[1] and y > C(0,-110)[1]:
                tmp.clear()
                D = 3
                rectangle(C(-135,-115),C(270,0)[0],C(0,50)[1],"white",4,tmp,False)
            if x > C(-135,0)[0] and x < C(135,0)[0] and y < C(0,-130)[1] and y > C(0,-210)[1] and D != 0:
                te.clear()
                tmp.clear()
                tracer(0)
                decor()
                progression_bar(use)
                list_box()
                allBoxesExceptDone(casing)
                ore = ores(D*5)
                ingot_list = coord_ore()
                a = coord_ore()
                menu_ok = 1
            if x > C(-135,0)[0] and x < C(135,0)[0] and y < C(0,-280)[1] and y > C(0,-320)[1]:
                exit()
                
        elif menu_ok == 1:
        # on recupère la case sur laquelle on clique
            card = getclickedcard(x,y)
            # si on a clique sur une case ET que cette case n'est pas deja retourne
            if card is not None and BOX[card][3] == 0:
            # on ajoute la case a la liste pairs, on met l'etat de la case a 2 et on decouvre ce qu'il y a en dessous 
                pairs.append(card)
                BOX[card][3]=2
                drawOre(BOX,ore,card,inter)
        # on clear tout sauf les cases a l'etat 2
            casing.clear()
        # on decouvre toutes les cases d'etat 1 ou 2 et on dessine les cases sinon
            allBoxesExceptDone(casing)
        # lorsque l'on a clique sur 2 cases
            if len(pairs) == 2:
            #  si les cases n'ont pas la même couleur on met l'etat des cases a 0         ore[pairs[0]][9][6] != ore[pairs[1]][9][6]
                if funct[pairs[0]] != funct[pairs[1]]:
                    for l in range(2):
                        BOX[pairs[l]][3]=0
                    use += 1
                    time.sleep(1)
            # sinon (donc si les cases match) alors on met l'etat des cases a 1 et on les ajoutes a une liste qui compte toutes les bonnes pairs
                else:
                    for i in range(2):
                        BOX[pairs[i]][3] = 1
                        drawOre(BOX,ore,pairs[i],thor)
                        drawTexture(ingot[pairs[i]],C(ingot_list[count][0],0)[0],C(0,ingot_list[count][1])[1],C(60,0)[0],thor)
                        count+=1
                    minecart_front(-490,-300,tc1,0)
                # on clear la liste pairs et on clear les cases intermediaires
                progression_bar(use)
                #time.sleep(1)
                pairs.clear()
                inter.clear()
                allBoxesExceptDone(casing)
            # detection de la fin du jeu, si la liste des pairs bien associees est egale aux nombres de pairs qu'il y a alors on fini le jeu
            if count == D*10 or tent_rest == 0:   
                endingscreen()
                menu_ok = 0
                t = 0
                use = 0
                D = 0
                count = 0

########## Setup ##########

colormode(255)

L = window_width()*2
l = window_height()*4/3

setup(1.0, 1.0)

screen = Screen()

tracer(0)

########## Variables ##########

working = False # Variable qui permet de savoir si la tortue est en train de dessiner, grâce à celle-ci lorqu'on clique très rapidement il n'y a aucun bug.

inter = Turtle() # Tortue intermediaire minerais
casing = Turtle() # Tortue des cases
td = Turtle() # Tortue decor
te = Turtle() # Tortue ecriture
tc1 = Turtle() # Tortue chariot 1
tc2 = Turtle() # Tortue chariot 2
tmp = Turtle() # Tortue temporaire
thor = Turtle() # Tortue des minerais

pioche = [['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', (104, 78, 30), (40, 30, 11), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', (73, 54, 21), (137, 103, 39), (40, 30, 11), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', (73, 54, 21), (104, 78, 30), (40, 30, 11), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', (73, 54, 21), (137, 103, 39), (40, 30, 11), 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (14, 63, 54), 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', (73, 54, 21), (104, 78, 30), (40, 30, 11), 'rien', 'rien', 'rien', 'rien', (14, 63, 54), (51, 235, 203), (14, 63, 54), 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', (73, 54, 21), (137, 103, 39), (40, 30, 11), 'rien', 'rien', 'rien', (14, 63, 54), (43, 199, 172), (14, 63, 54), 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (73, 54, 21), (104, 78, 30), (40, 30, 11), 'rien', 'rien', (14, 63, 54), (39, 178, 154), (14, 63, 54), 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (73, 54, 21), (137, 103, 39), (40, 30, 11), 'rien', (14, 63, 54), (39, 178, 154), (14, 63, 54), 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (73, 54, 21), (104, 78, 30), (40, 30, 11), (39, 178, 154), (43, 199, 172), (14, 63, 54), 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', (73, 54, 21), (43, 199, 172), (39, 178, 154), (14, 63, 54), 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', (14, 63, 54), (14, 63, 54), (14, 63, 54), (14, 63, 54), (39, 178, 154), (39, 178, 154), (137, 103, 39), (40, 30, 11), 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', (14, 63, 54), (51, 235, 203), (43, 199, 172), (39, 178, 154), (39, 178, 154), (43, 199, 172), (14, 63, 54), (73, 54, 21), (104, 78, 30), 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', (14, 63, 54), (14, 63, 54), (14, 63, 54), (14, 63, 54), (14, 63, 54), 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien'], ['rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien', 'rien']]

# Variable qui contient toutes les couleurs des minerais et lingots.
funct = [[bluer,1],[bluer,100],[bluer,-100],[reder,100],[reder,-100],[greener,100],[greener,-100],[bluer,-370,reder,130],[bluer,-110,greener,-30,reder,-110],[bluer,-140,greener,-120,reder,-20],[reder,-140,greener,-120,bluer,-20],[reder,70,greener,-130,bluer,-130],[reder,-10,greener,40,bluer,-160],[greener,-170,reder,80],["random"]]

# Liste qui contient les postions de chaque cases/minerais.
BOX = [[-580,-11],[-520,184],[-461,33],[-359,176],[-305,120],[-193,278],[-174,-132],[-110,170],[-110,0],[218,-10],[270,244],[269,-14],[320,-69],[419,135],[520,244],[540,10],[-58,-138],[-59,167],[-20,20],[51,7],[103,286],[205,92],[-510,-72],[15,135],[422,-175],[-470,-53],[-258,28],[118,73],[321,90],[558,-115]]

# On rend toutes les tortues invisibles
T = [td,te,tc1,tc2,tmp,inter,casing,thor]
for i in range(len(T)):
    T[i].ht()

# On met toutes les variables nécéssaires au fonctionnement du jeu à 0 ou vide.
menu_ok = 0
t = 0
use = 0
D = 0
count = 0
pairs = []

########## Code ##########

menu()

screen.onclick(game)

screen.mainloop()
