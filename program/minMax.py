def minMax(frame,player):
    scores = rescore(frame)
    if player == "x":
        topScore = float("-inf")
        coor = []
        #X checks for the top value, saves the coordinate and inserts the "x"
        for i in range(0, 3):
            for j in range(0,3):
                if scores[i][j] > topScore:
                    topScore = scores[i][j]
                    coor = [i,j] 
        frame[coor[0]][coor[1]] = "x" 
        player = "o"
    else:
        move = input("put code")
        frame = filler(move,frame,player)
        player = "x"
        
    return frame

def rescore(frame):
    scores = [[3,2,3],[2,0,2],[3,2,3]]

    #corner danger
    if frame[0][0] == "o" and frame[0][2] == "o":
        scores[0][1] = 3
    if frame[0][0] == "o" and frame[2][0] == "o":
        scores[1][0] = 3
    if frame[2][0] == "o" and frame[2][2] == "o":
        scores[2][1] = 3
    if frame[0][2] == "o" and frame[2][2] == "o":
        scores[1][2] = 3
        
    #used values
    for j in range(0, 3):
        for i in range(0,3):
            if "o" == frame[i][j] or "x" == frame[i][j]:
                scores[i][j] = 0
                
    #vertical moves
    for j in range(0,3):            
        for i in range(0,3):
            if "o" == frame[i][j]:
                for v in range(0,3):
                    scores[v][j] -= 1
                break
        continue
    #horizontal moves    
    for i in range(0,3):            
        for j in range(0,3):
            if "o" == frame[i][j]:
                for v in range(0,3):
                    scores[i][v] -= 1
                break
        continue

    #diagonals
    if frame[0][0] == "o":
        scores[2][2] -= 1
    elif frame[0][2] == "o":
        scores[2][0] -= 1
    elif frame[2][0] == "o":
        scores[0][2] -= 1
    elif frame[2][2] == "o":
        scores[0][0] -= 1

   # for val in scores:
   #     print(val)
   # print("------------")
    return scores

def filler(code,frame,player): #Just for human player
    fill = {"TL":1, "TM":2, "TR":3,"ML":4,"MM":5,"MR":6,"BL":7,"BM":8,"BR":9}
    if fill[code] == 1:
        frame[0][0] = player
        return frame
    if fill[code] == 2:
        frame[0][1] = player
        return frame
    if fill[code] == 3:
        frame[0][2] = player
        return frame
    if fill[code] == 4:
        frame[1][0] = player
        return frame
    if fill[code] == 5:
        frame[1][1] = player
        return frame
    if fill[code] == 6:
        frame[1][2] = player
        return frame
    if fill[code] == 7:
        frame[2][0] = player
        return frame
    if fill[code] == 8:
        frame[2][1] = player
        return frame
    if fill[code] == 9:
        frame[2][2] = player
        return frame
    
def checkWin(frame):    
    #Rows
    for i in range(0,3):
        if ["x"]*3 == frame[i]:
            return print ("x wins")
        elif ["o"]*3 == frame[i]:
            return print ("o wins")
        else:
            pass
    #Columns        
    for i in range(0,3):
        if "x" == frame[0][i] and "x" == frame[1][i] and "x" == frame[2][i]:
            return print("x wins")
        elif "o" == frame[0][i] and "o" == frame[1][i] and "o" == frame[2][i]:
            return print ("o wins")
        else:
            pass
    # Inclines    
    if "x" == frame[0][0] and "x" == frame[1][1] and "x" == frame[2][2]:
        return "x wins"
    elif "o" == frame[0][0] and "o" == frame[1][1] and "o" == frame[2][2]:
        return print ("o wins")

    if "x" == frame[0][2] and "x" == frame[1][1] and "x" == frame[2][0]:
        return "x wins"
    elif "o" == frame[0][2] and "o" == frame[1][1] and "o" == frame[2][0]:
        return print ("o wins")
    pass

def main():
    frame = [["-"]*3 for i in range(0,3)]
    frame[1][1] = "x" #x will always start in the middle
    for val in frame:
            print(val)
            
    for i in range(1,9):
        if i%2 == 0:
            print("------------")
            print("Turn of X")
            player = "x"
        else:
            print("------------")
            print("Turn of O")
            player = "o"
        frame = minMax(frame,player)
        for val in frame:
            print(val)
            
        condition = checkWin(frame)
        if condition == "x wins":
            return print("The winner is x")
main()
