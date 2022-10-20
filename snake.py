from os import system
import platform
from time import sleep
from random import randint
import keyboard

clear = ""
width = 40
height = 20
gameOver = False
direction = "STOP"
score = 0
snakeXY = [width / 2, height / 2]
fruitXY = [randint(1, width), randint(1, height)]
tail = [[0, 0]]
totalTail = 0
tailX = list(range(100))
tailY = list(range(100))


def draw():

    # draw game screen

    system(clear)

    print("\033[1;37m")

    for y in range(height+2):
        if y == 0 or y == height+1:
            print("#" * (width+2))
        else:
            for x in range(width+2):
                if x == 0:
                    print("#", end="")
                elif x == width+1:
                    print("#")
                else:
                    if y == snakeXY[1] and x == snakeXY[0]:
                        print("\033[1;32mO\033[1;37m", end="")
                    elif y == fruitXY[1] and x == fruitXY[0]:
                        print("\033[1;31m@\033[1;37m", end="")
                    else:
                        show = True
                        for k in range(totalTail):
                            if tailX[k] == x and tailY[k] == y:
                                print("\033[1;32mo\033[1;37m", end="")
                                show = False
                        """
                        for xy in (tail):
                            if y == xy[1] and x == xy[0]:
                                print("\033[1;32mo\033[1;37m", end="")
                                show = False
                        """
                        if show:
                            print(end="-")
    
    print(f"\n\nScore: {score} Tail: {totalTail}")

    print(f"\nDEBUG:\n  Snake: (X: {snakeXY[0]} Y: {snakeXY[1]})")

    # print(f"TailX: {tailX}")
    # print(f"TailX: {tailY}")


def keyInput():
    
    global direction

    if keyboard.is_pressed("w") or keyboard.is_pressed("up") and direction != "DOWN":
        direction = "UP"
    elif keyboard.is_pressed("s") or keyboard.is_pressed("down") and direction != "UP":
        direction = "DOWN"
    elif keyboard.is_pressed("a") or keyboard.is_pressed("left") and direction != "RIGHT":
        direction = "LEFT"
    elif keyboard.is_pressed("d") or keyboard.is_pressed("right") and direction != "LEFT":
        direction = "RIGHT"


def logic(gameMode):
    
    global snakeXY, fruitXY, gameOver, score, totalTail, tailX, tailY

    prevX = tailX[0]
    prevY = tailY[0]
    
    tailX[0] = snakeXY[0]
    tailY[0] = snakeXY[1]

    for i in range(1, totalTail):
        prev2X = tailX[i]
        prev2Y = tailY[i]
        tailX[i] = prevX
        tailY[i] = prevY
        prevX = prev2X
        prevY = prev2Y

    # snake directions
    if direction == "UP":
        snakeXY[1] -= 1
    elif direction =="DOWN":
        snakeXY[1] += 1
    elif direction == "LEFT":
        snakeXY[0] -= 1
    elif direction == "RIGHT":
        snakeXY[0] += 1

    # if the snake hit the wall
    if gameMode == 1:
        if snakeXY[0] < 1 or snakeXY[0] > width or snakeXY[1] < 1 or snakeXY[1] > height:
            gameOver = True
    else:
        if snakeXY[0] < 1:
            snakeXY[0] = width
        elif snakeXY[0] > width:
            snakeXY[0] = 1
        elif snakeXY[1] < 1:
            snakeXY[1] = height
        elif snakeXY[1] > height:
            snakeXY[1] = 1

    for i in range(totalTail):
        if tailX[i] == snakeXY[0] and tailY[i] == snakeXY[1]:
            gameOver = True

    # if snake eat the fruit
    if snakeXY[0] == fruitXY[0] and snakeXY[1] == fruitXY[1]:
        totalTail += 1
        score += 10
        fruit = False
        while not fruit:
            fruitXY = [randint(1, width), randint(1, height)]
            for i in range(totalTail):
                if tailX[i] == fruitXY[0] and tailY[i] == fruitXY[1]:
                    fruitXY = [randint(1, width), randint(1, height)]
                    fruit = True


def main():
    if platform.system() == "Windows":
        clear = "cls"
    else:
        clear = "clear"

    global gameOver

    system(clear)
    print(f" {'-='*20}")
    print(f"|{'SNAKE GAME':^40}|")
    print(f" {'-='*20}")
    print(f"|{'':^40}|")
    print(f"|{' [1] Can crash into the wall':<40}|")
    print(f"|{' [2] Can teleport through the wall':<40}|")
    print(f"|{'':^40}|")
    print(f" {'-='*20}")

    gameMode = int(input("\nSelect game mode: "))
    
    while not gameOver:
        keyInput()
        draw()
        logic(gameMode)
        if direction == "LEFT" or direction == "RIGHT":
            sleep(0.005)
        sleep(0.1)
        if direction == "UP" or direction == "DOWN":
            sleep(0.070)
    print("\nGAME OVER\n")


main()
