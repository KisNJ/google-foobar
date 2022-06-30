import math
def pos_to_coords(pos):
    y=int(math.floor(pos/8))
    x=int(pos%8)
    return x,y


def get_possible_moves(x,y):
    #move 1 x-2 y+1
    #move 2 x-2 y-1
    #move 3 x+2 y+1
    #move 4 x+2 y-1
    #move 5 y-2 x+1
    #move 6 y-2 x-1
    #move 7 y+2 x+1
    #move 8 y+2 x-1
    every_possible_move=[(-2,+1),(-2,-1),(+2,+1),(+2,-1),(+1,-2),(-1,-2),(+1,+2),(-1,+2)]
    possible_move_on_this_coord=[]
    for move in every_possible_move:
        if x+move[0]>=0 and x+move[0]<8 and y+move[1]>=0 and y+move[1]<8:
            possible_move_on_this_coord.append(move)

    return possible_move_on_this_coord
def coords_after_move(x,y,move):
    x=x+move[0]
    y=y+move[1]
    return x,y

def valid_cords(x,y):
    if (x>9 or x<0) or (y>9 or y<0):
        return False
    return True
def solution(src, dest):
    if(src==dest):
        return 0
   
    x_src,y_src=pos_to_coords(src)
    x_dest,y_dest=pos_to_coords(dest)
    try_these_coords=[(x_src,y_src)]
    found=False
    steps=1
    while not found:
        temp_cords=[]
        possible_moves=[]
        
        #print(try_these_coords)
        for coord in try_these_coords:
            move=get_possible_moves(coord[0], coord[1])
            if move not in possible_moves:
                possible_moves.append(get_possible_moves(coord[0], coord[1]))
        
        for moves in possible_moves:
            for move in moves:
                for coord in try_these_coords:
                    x_temp,y_temp=coords_after_move(coord[0], coord[1], move)
                    if(valid_cords(x_temp, y_temp)):
                        if (x_temp,y_temp) not in temp_cords:
                            temp_cords.append( (x_temp,y_temp))
                            print(temp_cords)
                        if (x_temp,y_temp)==(x_dest,y_dest):
                            found=True
        try_these_coords=temp_cords
       #print(temp_cords)
        steps +=1
    return steps-1
print(solution(0, 0))
