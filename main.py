import pygame, math, time, random, copy
##############################################################################
#                                   CLASSES                                  #
##############################################################################
class Trap():
    x1 = x2 = x3 = x4 = y1 = y2 = y3 = y4 = xSpeed1 = xSpeed2 = xSpeed3 = xSpeed4 = ySpeed1 = ySpeed2 = ySpeed3 = ySpeed4 = 0
class Square():
    x = y = newX = newY = w = h = speedX = speedY = 0
class Button():
    x = y = w = h = text = 0
class Player():
    name = score = 0
    
##############################################################################
#                                  FUNCTIONS                                 #
##############################################################################
#DO NOT EDIT THIS FUNCTION!
def checkHit(trap_x1, trap_y1, trap_x2, trap_y2):
    #check if the line has hit any of the rectangle's sides
    #uses the Line/Line function below

    left = checkLineHit(trap_x1, trap_y1, trap_x2, trap_y2, player.x, player.y, player.x, player.y + player.h)
    right = checkLineHit(trap_x1, trap_y1, trap_x2, trap_y2, player.x + player.w, player.y, player.x + player.w, player.y + player.h)
    top = checkLineHit(trap_x1, trap_y1, trap_x2, trap_y2, player.x, player.y, player.x + player.w, player.y)
    bottom = checkLineHit(trap_x1, trap_y1, trap_x2, trap_y2, player.x, player.y + player.h, player.x + player.w, player.y + player.h)

    # if ANY of the above are true, the line has hit the rectangle
    if left or right or top or bottom:
        return True
    else:
        return False


def checkLineHit(trap_x1, trap_y1, trap_x2, trap_y2, player_x1, player_y1, player_x2, player_y2):

    #calculate the direction of the lines
    a1 = ((player_x2 - player_x1) * (trap_y1 - player_y1) - (player_y2 - player_y1)  * (trap_x1 - player_x1))
    a2 = ((player_y2 - player_y1) * (trap_x2 - trap_x1) - (player_x2 - player_x1) * (trap_y2 - trap_y1))
    b1 = ((trap_x2 - trap_x1) * (trap_y1 - player_y1) - (trap_y2 - trap_y1) * (trap_x1 - player_x1))
    b2 = ((player_y2 - player_y1) * (trap_x2 - trap_x1) - (player_x2 - player_x1) * (trap_y2 - trap_y1))

    #avoid dividing by zero
    if a1 == 0 or a2 == 0 or b1 == 0 or b2 == 0:
        return False
   
    uA = float(a1) / float(a2)
    uB = float(b1) / float(b2)
    #if uA and uB are between 0-1, lines are colliding
    if uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1:
        return True
    else:
        return False

##############################################################################
#                      ONE TIME SETUP (GLOBAL VARIABLES)                     #
##############################################################################
pygame.init()
screen = pygame.display.set_mode([800,800])
pygame.display.set_caption("My First Game!")

#Set up global variables
width = screen.get_width()
height = screen.get_height()
fps = 60
timer = 0
gameState = "Menu"

font50 = pygame.font.SysFont("Arial", 200, bold=True, italic=False)
font40 = pygame.font.SysFont("Arial", 100, bold=True, italic=False)
font20 = pygame.font.SysFont("Times New Roman", 20, bold=True, italic=True)
font30 = pygame.font.SysFont("Castellar", 100, bold=False, italic=False)
font10 = pygame.font.SysFont("Arial", 50, bold=False, italic=False)
font5 = pygame.font.SysFont("Arial", 30, bold=False, italic=False)

startButton = Button()
startButton.w = 300
startButton.h = 100
startButton.x = screen.get_width()/2 - startButton.w/2
startButton.y = screen.get_height() - 370
startButton.text = "Play"

instructButton = Button()
instructButton.w = 300
instructButton.h = 50
instructButton.x = screen.get_width()/2 - startButton.w/2
instructButton.y = screen.get_height() - 250
instructButton.text = "HOW TO PLAY"

scoreButton = Button()
scoreButton.w = 300
scoreButton.h = 100
scoreButton.x = screen.get_width()/2 - startButton.w/2
scoreButton.y = screen.get_height() - 190
scoreButton.text = "SCOREBOARD"

exitButton = Button()
exitButton.w = 100
exitButton.h = 50
exitButton.x = width * 0.01
exitButton.y = height * 0.01
exitButton.text = "EXIT"

#Creating hexagon in centre:
x1 = width * 0.46
x2 = width * 0.54
x3 = width * 0.58
x4 = width * 0.54
x5 = width * 0.46
x6 = width * 0.42
y1 = height * 0.44
y2 = height * 0.44
y3 = height * 0.5
y4 = height * 0.56
y5 = height * 0.56
y6 = height * 0.5

#User controlling square:
radius = 100
player = Square()
player.x = ((width / 2) - 10) + radius
player.y = ((height / 2) - 10) 
player.newX = (width / 2) - 10
player.newY = (height / 2) - 10
player.w = 20
player.h = 20 
player.speed = 3
degrees = 0
player.holdingLeft = False
player.holdingRight = False

#Creating 3 Hexagons:
hexagon = []
hexagon2 = []
hexagon3 = []
for i in range(6):
    trap = Trap()
    if i == 0:
        trap.x1 = width * -0.1
        trap.x2 = width * -0.2
        trap.x3 = width * 1.2
        trap.x4 = width * 1.1
        trap.y1 = height * -0.1
        trap.y2 = height * -0.25
        trap.y3 = height * -0.25
        trap.y4 = height * -0.1
        trap.xSpeed1 = (trap.x1 - x1) / 400
        trap.xSpeed2 = (trap.x2 - x1) / 400
        trap.xSpeed3 = (trap.x3 - x2) / 400
        trap.xSpeed4 = (trap.x4 - x2) / 400
        trap.ySpeed1 = (trap.y1 - y1) / 400
        trap.ySpeed2 = (trap.y2 - y1) / 400
        trap.ySpeed3 = (trap.y3 - y2) / 400
        trap.ySpeed4 = (trap.y4 - y2) / 400
        hexagon.append(trap)
        
    elif i == 1:
        trap.x1 = width * -0.1
        trap.x2 = width * -0.2
        trap.x3 = width * -0.7
        trap.x4 = width * -0.5
        trap.y1 = height * -0.1
        trap.y2 = height * -0.25
        trap.y3 = height * 0.5
        trap.y4 = height * 0.5
        trap.xSpeed1 = (trap.x1 - x1) / 400
        trap.xSpeed2 = (trap.x2 - x1) / 400
        trap.xSpeed3 = (trap.x3 - x6) / 400
        trap.xSpeed4 = (trap.x4 - x6) / 400
        trap.ySpeed1 = (trap.y1 - y1) / 400
        trap.ySpeed2 = (trap.y2 - y1) / 400
        trap.ySpeed3 = (trap.y3 - y6) / 400
        trap.ySpeed4 = (trap.y4 - y6) / 400
        hexagon.append(trap)
        
    elif i == 2:
        trap.x1 = width * -0.5
        trap.x2 = width * -0.7
        trap.x3 = width * -0.2
        trap.x4 = width * -0.1
        trap.y1 = height * 0.5
        trap.y2 = height * 0.5
        trap.y3 = height * 1.25
        trap.y4 = height * 1.1
        trap.xSpeed1 = (trap.x1 - x6) / 400
        trap.xSpeed2 = (trap.x2 - x6) / 400
        trap.xSpeed3 = (trap.x3 - x5) / 400
        trap.xSpeed4 = (trap.x4 - x5) / 400
        trap.ySpeed1 = (trap.y1 - y6) / 400
        trap.ySpeed2 = (trap.y2 - y6) / 400
        trap.ySpeed3 = (trap.y3 - y5) / 400
        trap.ySpeed4 = (trap.y4 - y5) / 400
        hexagon.append(trap)
     
    elif i == 3:
        trap.x1 = width * -0.1
        trap.x2 = width * -0.2
        trap.x3 = width * 1.2
        trap.x4 = width * 1.1
        trap.y1 = height * 1.1
        trap.y2 = height * 1.25
        trap.y3 = height * 1.25
        trap.y4 = height * 1.1
        trap.xSpeed1 = (trap.x1 - x5) / 400
        trap.xSpeed2 = (trap.x2 - x5) / 400
        trap.xSpeed3 = (trap.x3 - x4) / 400
        trap.xSpeed4 = (trap.x4 - x4) / 400
        trap.ySpeed1 = (trap.y1 - y5) / 400
        trap.ySpeed2 = (trap.y2 - y5) / 400
        trap.ySpeed3 = (trap.y3 - y4) / 400
        trap.ySpeed4 = (trap.y4 - y4) / 400
        hexagon.append(trap)
     
    elif i == 4:
        trap.x1 = width * 1.1
        trap.x2 = width * 1.2
        trap.x3 = width * 1.7
        trap.x4 = width * 1.5
        trap.y1 = height * 1.1
        trap.y2 = height * 1.25
        trap.y3 = height * 0.5
        trap.y4 = height * 0.5
        trap.xSpeed1 = (trap.x1 - x4) / 400
        trap.xSpeed2 = (trap.x2 - x4) / 400
        trap.xSpeed3 = (trap.x3 - x3) / 400
        trap.xSpeed4 = (trap.x4 - x3) / 400
        trap.ySpeed1 = (trap.y1 - y4) / 400
        trap.ySpeed2 = (trap.y2 - y4) / 400
        trap.ySpeed3 = (trap.y3 - y3) / 400
        trap.ySpeed4 = (trap.y4 - y3) / 400
        hexagon.append(trap)
    
    elif i == 5:
        trap.x1 = width * 1.5
        trap.x2 = width * 1.7
        trap.x3 = width * 1.2
        trap.x4 = width * 1.1
        trap.y1 = height * 0.5
        trap.y2 = height * 0.5
        trap.y3 = height * -0.25
        trap.y4 = height * -0.1
        trap.xSpeed1 = (trap.x1 - x3) / 400
        trap.xSpeed2 = (trap.x2 - x3) / 400
        trap.xSpeed3 = (trap.x3 - x2) / 400
        trap.xSpeed4 = (trap.x4 - x2) / 400
        trap.ySpeed1 = (trap.y1 - y3) / 400
        trap.ySpeed2 = (trap.y2 - y3) / 400
        trap.ySpeed3 = (trap.y3 - y2) / 400
        trap.ySpeed4 = (trap.y4 - y2) / 400
        hexagon.append(trap)
        
hexagon2 = copy.deepcopy(hexagon)
hexagon3 = copy.deepcopy(hexagon2)

originalHexagon = copy.deepcopy(hexagon)
originalHexagon2 = copy.deepcopy(hexagon2)
originalHexagon3 = copy.deepcopy(hexagon3)

sides = 2 #starting the level by spawning 2 sides from each hexagon
hexagon = random.sample(hexagon, sides)
hexagon2 = random.sample(hexagon2, sides)
hexagon3 = random.sample(hexagon3, sides)
speedMultiplier = 1 #changing this later to speed up hexagons
           
instructions = False
scoreboard = False
people = []
user = Player()
user.name = 0
user.score = 0
users = []
##############################################################################
#                                 GAME LOOP                                  #
##############################################################################
while True:
    # ===================== HANDLE EVENTS (DO NOT EDIT) ===================== #
    done = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = True
            break

        # =================== MOUSE DOWN ==================== #
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]
            if gameState == "Menu" and instructions == False and scoreboard == False:
                #clicked on the start button?
                if mouseX >= startButton.x and mouseX <= startButton.x + startButton.w and mouseY >= startButton.y and mouseY <= startButton.y + startButton.h:
                    #reset all variables that might have changed during the game back
                    #to their original values
                    user = Player()
                    hexagon = copy.deepcopy(originalHexagon)
                    hexagon2 = copy.deepcopy(originalHexagon2)
                    hexagon3 = copy.deepcopy(originalHexagon3)
                    sides = 2                    
                    hexagon = random.sample(hexagon, sides)
                    hexagon2 = random.sample(hexagon2, sides)
                    hexagon3 = random.sample(hexagon3, sides)
                    speedMultiplier = 1
                    timer = 0
                    win = False
                    gameState = "In Game"
                if mouseX >= instructButton.x and mouseX <= instructButton.x + instructButton.w and mouseY >= instructButton.y and mouseY <= instructButton.y + instructButton.h:
                    instructions = True
                if mouseX >= scoreButton.x and mouseX <= scoreButton.x + scoreButton.w and mouseY >= scoreButton.y and mouseY <= scoreButton.y + scoreButton.h:
                    scoreboard = True
                if mouseX >= exitButton.x and mouseX <= exitButton.x + exitButton.w and mouseY >= exitButton.y and mouseY <= exitButton.y + exitButton.h:
                    done = True
               

        # ==================== KEY DOWN ====================== #
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.holdingLeft = True
            elif event.key == pygame.K_RIGHT:
                player.holdingRight = True
            elif instructions == True:
                if event.key == pygame.K_ESCAPE:
                    instructions = False                    
            elif scoreboard == True:
                if event.key == pygame.K_ESCAPE:
                    scoreboard = False
            elif gameState == "End Game":
                user.score = ("%0.2f" % timer)
                user.score = float(user.score)
                if user.name == 0: #to record first letter
                    if event.key == pygame.K_a:
                        user.name = "A"
                    elif event.key == pygame.K_b:
                        user.name = "B"
                    elif event.key == pygame.K_c:
                        user.name = "C"
                    elif event.key == pygame.K_d:
                        user.name = "D"
                    elif event.key == pygame.K_e:
                        user.name = "E"
                    elif event.key == pygame.K_f:
                        user.name = "F"
                    elif event.key == pygame.K_g:
                        user.name = "G"
                    elif event.key == pygame.K_h:
                        user.name = "H"
                    elif event.key == pygame.K_i:
                        user.name = "I"
                    elif event.key == pygame.K_j:
                        user.name = "J"
                    elif event.key == pygame.K_k:
                        user.name = "K"
                    elif event.key == pygame.K_l:
                        user.name = "L"
                    elif event.key == pygame.K_m:
                        user.name = "M"
                    elif event.key == pygame.K_n:
                        user.name = "N"
                    elif event.key == pygame.K_o:
                        user.name = "O"
                    elif event.key == pygame.K_p:
                        user.name = "P"
                    elif event.key == pygame.K_q:
                        user.name = "Q"
                    elif event.key == pygame.K_r:
                        user.name = "R"
                    elif event.key == pygame.K_s:
                        user.name = "S"
                    elif event.key == pygame.K_t:
                        user.name = "T"
                    elif event.key == pygame.K_u:
                        user.name = "U"
                    elif event.key == pygame.K_v:
                        user.name = "V"
                    elif event.key == pygame.K_w:
                        user.name = "W"
                    elif event.key == pygame.K_x:
                        user.name = "X"
                    elif event.key == pygame.K_y:
                        user.name = "Y"
                    elif event.key == pygame.K_z:
                        user.name = "Z"
                       
                elif len(user.name) <= 9:
                    if event.key == pygame.K_a:
                        user.name = user.name + "A"
                    elif event.key == pygame.K_b:
                        user.name = user.name+ "B"
                    elif event.key == pygame.K_c:
                        user.name = user.name + "C"
                    elif event.key == pygame.K_d:
                        user.name = user.name + "D"
                    elif event.key == pygame.K_e:
                        user.name = user.name + "E"
                    elif event.key == pygame.K_f:
                        user.name = user.name + "F"
                    elif event.key == pygame.K_g:
                        user.name = user.name + "G"
                    elif event.key == pygame.K_h:
                        user.name = user.name + "H"
                    elif event.key == pygame.K_i:
                        user.name = user.name + "I"
                    elif event.key == pygame.K_j:
                        user.name = user.name + "J"
                    elif event.key == pygame.K_k:
                        user.name = user.name + "K"
                    elif event.key == pygame.K_l:
                        user.name = user.name + "L"
                    elif event.key == pygame.K_m:
                        user.name = user.name + "M"
                    elif event.key == pygame.K_n:
                        user.name = user.name + "N"
                    elif event.key == pygame.K_o:
                        user.name = user.name + "O"
                    elif event.key == pygame.K_p:
                        user.name = user.name + "P"
                    elif event.key == pygame.K_q:
                        user.name = user.name + "Q"
                    elif event.key == pygame.K_r:
                        user.name = user.name + "R"
                    elif event.key == pygame.K_s:
                        user.name = user.name + "S"
                    elif event.key == pygame.K_t:
                        user.name = user.name + "T"
                    elif event.key == pygame.K_u:
                        user.name = user.name + "U"
                    elif event.key == pygame.K_v:
                        user.name = user.name+ "V"
                    elif event.key == pygame.K_w:
                        user.name = user.name + "W"
                    elif event.key == pygame.K_x:
                        user.name = user.name + "X"
                    elif event.key == pygame.K_y:
                        user.name = user.name + "Y"
                    elif event.key == pygame.K_z:
                        user.name = user.name + "Z"
                if event.key == pygame.K_BACKSPACE:
                    user.name = user.name[:-1]
                if event.key == pygame.K_ESCAPE and user.name != 0:
                    users.append(user) 
                    gameState = "Menu"
                    
                    
        # ==================== KEY UP ======================== #
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.holdingLeft = False
            elif event.key == pygame.K_RIGHT:
                player.holdingRight = False
                
    if done == True:
        break

    # ============================== MOVE STUFF ============================= #   

    if gameState == "In Game":
        timer += 1/fps
        #changing position of player's square
        if player.holdingRight == True:
            degrees = degrees + player.speed
            if degrees == 360:
                degrees = 0

            theta = math.radians(degrees)
            player.x =  player.newX + radius*math.cos(theta)
            player.y = player.newY + radius*math.sin(theta)
        
        if player.holdingLeft == True:
            degrees = degrees - player.speed
            if degrees == 360:
                degrees = 0

            theta = math.radians(degrees)
            player.x = player.newX + radius*math.cos(theta)
            player.y =  player.newY + radius*math.sin(theta)

            
        if timer >= 35:
            speedMultiplier = speedMultiplier + 0.001
            
        for trap in hexagon:
            trap.x1 = trap.x1 - (trap.xSpeed1 * speedMultiplier)
            trap.x2 = trap.x2 - (trap.xSpeed2 * speedMultiplier)
            trap.x3 = trap.x3 - (trap.xSpeed3 * speedMultiplier)
            trap.x4 = trap.x4 - (trap.xSpeed4 * speedMultiplier)

            trap.y1 = trap.y1 - (trap.ySpeed1 * speedMultiplier)
            trap.y2 = trap.y2 - (trap.ySpeed2 * speedMultiplier)
            trap.y3 = trap.y3 - (trap.ySpeed3 * speedMultiplier)
            trap.y4 = trap.y4 - (trap.ySpeed4 * speedMultiplier)
            
        if timer >= 2.3:
            for trap in hexagon2:
                trap.x1 = trap.x1 - (trap.xSpeed1 * speedMultiplier) 
                trap.x2 = trap.x2 - (trap.xSpeed2 * speedMultiplier)
                trap.x3 = trap.x3 - (trap.xSpeed3 * speedMultiplier)
                trap.x4 = trap.x4 - (trap.xSpeed4 * speedMultiplier)

                trap.y1 = trap.y1 - (trap.ySpeed1 * speedMultiplier)
                trap.y2 = trap.y2 - (trap.ySpeed2 * speedMultiplier)
                trap.y3 = trap.y3 - (trap.ySpeed3 * speedMultiplier)
                trap.y4 = trap.y4 - (trap.ySpeed4 * speedMultiplier) 
        if timer >= 4.6:
            for trap in hexagon3:
                trap.x1 = trap.x1 - (trap.xSpeed1 * speedMultiplier)
                trap.x2 = trap.x2 - (trap.xSpeed2 * speedMultiplier)
                trap.x3 = trap.x3 - (trap.xSpeed3 * speedMultiplier)
                trap.x4 = trap.x4 - (trap.xSpeed4 * speedMultiplier)

                trap.y1 = trap.y1 - (trap.ySpeed1 * speedMultiplier)
                trap.y2 = trap.y2 - (trap.ySpeed2 * speedMultiplier)
                trap.y3 = trap.y3 - (trap.ySpeed3 * speedMultiplier)
                trap.y4 = trap.y4 - (trap.ySpeed4 * speedMultiplier)

        if timer >= 60:
            win = True
            #the user wins if they survive for 1 minute, however the game keeps going until there is collision 

    # ============================== COLLISION ============================== #
    if gameState == "In Game":
        #Adding more sides/walls to make the level harder       
        if timer >= 10:
            sides = 3
        if timer >= 20:
            sides = 4
        if timer >= 30:
            sides =  5
        #Checking to see if one trapezoid collides with the center hexagon, then setting it back to its original positon          
        for trap in hexagon[:1]:
            if trap.x1 >= x1 and trap.y1 >= y1:
                for trap in hexagon:
                    hexagon = copy.deepcopy(originalHexagon)
                    hexagon = random.sample(hexagon, sides)
        for trap in hexagon2[:1]:
            if trap.x1 >= x1 and trap.y1 >= y1:
                for trap in hexagon2:
                    hexagon2 = copy.deepcopy(originalHexagon2)
                    hexagon2 = random.sample(hexagon2, sides)
        for trap in hexagon3[:1]:
            if trap.x1 >= x1 and trap.y1 >= y1:
                for trap in hexagon3:
                    hexagon3 = copy.deepcopy(originalHexagon3)
                    hexagon3 = random.sample(hexagon3, sides)

        #Checking if collision between player and hexagon is true
        for trap in hexagon:
            hit = checkHit(trap.x1, trap.y1, trap.x4, trap.y4)
            if hit:
                gameState = "End Game"
                player.score = int(timer) 
        for trap in hexagon2:
            hit = checkHit(trap.x1, trap.y1, trap.x4, trap.y4)
            if hit:
                gameState = "End Game"
                player.score = int(timer) 
        for trap in hexagon3:
            hit = checkHit(trap.x1, trap.y1, trap.x4, trap.y4)
            if hit:
                gameState = "End Game"
                player.score = int(timer) 

    # ============================== DRAW STUFF ============================= #
    if gameState == "Menu":
        mouseHoverX = pygame.mouse.get_pos()[0]
        mouseHoverY = pygame.mouse.get_pos()[1]            
        screen.fill ((0,0,0))
        users.sort(key = lambda user: user.score, reverse = True)

        
        #Title
        text = font40.render('SUPER', True, (0,0,255))
        screen.blit(text, [screen.get_width()/2 - 140, screen.get_height()/4])
        text = font40.render('HEXAGON', True, (0,0,255))
        screen.blit(text, [screen.get_width()/2 - 205, screen.get_height()/3 + 10])
        
        #Play button
        text = font30.render(startButton.text, True, (255,255,255))
        if mouseHoverX >= startButton.x and mouseHoverX <= startButton.x + startButton.w and mouseHoverY >= startButton.y and mouseHoverY <= startButton.y + startButton.h:
            text = font30.render(startButton.text, True, (255,251,159))     
        screen.blit(text, [startButton.x + 12, startButton.y - 5])
        
        #How to play button
        text = font10.render(instructButton.text, True, (255,255,255))
        if mouseHoverX >= instructButton.x and mouseHoverX <= instructButton.x + instructButton.w and mouseHoverY >= instructButton.y and mouseHoverY <= instructButton.y + instructButton.h:
            text = font10.render(instructButton.text, True, (255,251,159))     
        screen.blit(text, [instructButton.x + 10, instructButton.y - 5])
        
        #Score button
        text = font10.render(scoreButton.text, True, (255,255,255))
        if mouseHoverX >= scoreButton.x and mouseHoverX <= scoreButton.x + scoreButton.w and mouseHoverY >= scoreButton.y and mouseHoverY <= scoreButton.y + scoreButton.h:
            text = font10.render(scoreButton.text, True, (255,251,159))     
        screen.blit(text, [scoreButton.x + 6, scoreButton.y - 5])
        
        #Exit button
        text = font10.render(exitButton.text, True, (255,255,255))
        if mouseHoverX >= exitButton.x and mouseHoverX <= exitButton.x + exitButton.w and mouseHoverY >= exitButton.y and mouseHoverY <= exitButton.y + exitButton.h:
            text = font10.render(exitButton.text, True, (255,251,159))     
        screen.blit(text, [exitButton.x + 6, exitButton.y - 5])

       
        if instructions == True:
            screen.fill ((0,0,0))
            text = font10.render('Goal:', True, (255,255,255))
            screen.blit(text, [width * 0.01, height * 0.01])
            text = font5.render('Your job is to prevent yourself from colliding with the hexagons', True, (255,255,255))
            screen.blit(text, [width * 0.05, height * 0.1])
            text = font5.render('coming your way. You are in control of the red square found in', True, (255,255,255))
            screen.blit(text, [width * 0.05, height * 0.15])
            text = font5.render('the middle. Using the left and right arrow keys, you can move', True, (255,255,255)) 
            screen.blit(text, [width * 0.05, height * 0.2])
            text = font5.render('the square either clockwise or counterclockwise, to position', True, (255,255,255)) 
            screen.blit(text, [width * 0.05, height * 0.25])
            text = font5.render('yourself correctly. Every hexagon will have an opening for you', True, (255,255,255))
            screen.blit(text, [width * 0.05, height * 0.3])
            text = font5.render('to seep through, however, more will be coming your way, becoming', True, (255,255,255))
            screen.blit(text, [width * 0.05, height * 0.35])
            text = font5.render('faster and more difficult to deal with. See if you can survive', True, (255,255,255)) 
            screen.blit(text, [width * 0.05, height * 0.4])
            text = font5.render('for the full minute.', True, (255,255,255))
            screen.blit(text, [width * 0.05, height * 0.45])
            text = font5.render('Hit "ESC" to return to menu', True, (255,255,255))
            screen.blit(text, [width * 0.6, height * 0.95])

        if scoreboard == True:
            screen.fill ((0,0,0))
            text = font40.render('TOP THREE', True, (0,0,255))
            screen.blit(text, [width * 0.2, height * 0.1])
            text = font40.render('SCORES', True, (0,0,255))
            screen.blit(text, [width * 0.28, height * 0.23])
            text = font5.render('Hit "ESC" to return to menu', True, (255,255,255))
            screen.blit(text, [width * 0.6, height * 0.95])
            
            text = font10.render('Name', True, (255,0,0))
            screen.blit(text, [width * 0.2, height * 0.4])
            text = font10.render('Time(s)', True, (255,0,0))
            screen.blit(text, [width * 0.65, height * 0.4])

            #sorting names based on scores from greatest to least: 
            users.sort(key = lambda user: user.score, reverse = True)
            #first place
            text = font10.render('1.', True, (250,234,1))
            screen.blit(text, [width * 0.1, height * 0.5])
            for user in users[0:1]:
                first1 = font10.render(user.name, True, (250,234,1))            
                screen.blit(first1, [width * 0.2, height * 0.5])
                first2 = font10.render(str(user.score), True, (250,234,1))            
                screen.blit(first2, [width * 0.67, height * 0.5])
            #second place
            text = font10.render('2.', True, (204,204,204))
            screen.blit(text, [width * 0.1, height * 0.6])
            for user in users[1:2]:
                second1 = font10.render(user.name, True, (204,204,204))            
                screen.blit(second1, [width * 0.2, height * 0.6])
                second2 = font10.render(str(user.score), True, (204,204,204))            
                screen.blit(second2, [width * 0.67, height * 0.6])
            #third place
            text = font10.render('3.', True, (255,155,0))
            screen.blit(text, [width * 0.1, height * 0.7])
            for user in users[2:3]:
                third1 = font10.render(user.name, True, (255,155,0))            
                screen.blit(third1, [width * 0.2, height * 0.7])
                third2 = font10.render(str(user.score), True, (255,155,0))            
                screen.blit(third2, [width * 0.67, height * 0.7])


    elif gameState == "In Game":
        screen.fill ((0,0,0))
        for trap in hexagon:
            pygame.draw.polygon(screen, (0, 0, 255), [[trap.x1, trap.y1], [trap.x2, trap.y2], [trap.x3, trap.y3], [trap.x4, trap.y4]])
        for trap in hexagon2:
            pygame.draw.polygon(screen, (0, 0, 255), [[trap.x1, trap.y1], [trap.x2, trap.y2], [trap.x3, trap.y3], [trap.x4, trap.y4]])
        for trap in hexagon3:
            pygame.draw.polygon(screen, (0, 0, 255), [[trap.x1, trap.y1], [trap.x2, trap.y2], [trap.x3, trap.y3], [trap.x4, trap.y4]])
        pygame.draw.rect(screen, (255, 0, 0), [player.x, player.y, player.w, player.h])
        pygame.draw.polygon(screen, (0, 0, 255), [[x1, y1], [x2, y2], [x3, y3], [x4, y4], [x5, y5], [x6, y6]])
   
    elif gameState == "End Game":
        screen.fill ((0,0,0))
        if win == True:
            gameOver = font40.render(' YOU WIN!!', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        else:
            gameOver = font40.render('YOU LOSE!', True, (255,0,0))

        score = font10.render(str("%0.2f" % timer), True, (0,0,255))
        screen.blit(gameOver, [width * 0.2 , height * 0.1])
        text = font10.render('TIME SURVIVED(s):', True, (0,0,255))
        screen.blit(text, [width * 0.25 , height * 0.3])
        screen.blit(score, [width * 0.42 , height * 0.35])

        text = font10.render('ENTER YOUR NAME:', True, (0,255,0))
        screen.blit(text, [width * 0.05, height * 0.5])
        text = font5.render('(MAX 10 CHARACTERS)', True, (0,255,0))
        screen.blit(text, [width * 0.05, height * 0.56])
        
        if user.name != 0:
            text = font5.render(user.name, True, (255,255,255))
        screen.blit(text, [width * 0.6, height * 0.525])

        text = font5.render('Hit "ESC" to return to menu and save username', True, (255,255,255))
        screen.blit(text, [width * 0.33, height * 0.95])        
     
    # ====================== PYGAME STUFF (DO NOT EDIT) ===================== #
    pygame.display.flip()
    pygame.time.delay(10)

