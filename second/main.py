import math

def pos_to_coords(pos):
    x = int(math.floor(pos/8))
    y = int(pos%8)
    return (x, y)


def coords_to_pos(x, y):
    return x + y * 8


def get_possible_moves(x, y):
    all_moves = []
    all_moves.append((x+2, y+1))
    all_moves.append((x+2, y-1))
    all_moves.append((x-2, y+1))
    all_moves.append((x-2, y-1))
    all_moves.append((x+1, y+2))
    all_moves.append((x+1, y-2))
    all_moves.append((x-1, y+2))
    all_moves.append((x-1, y-2))

    valid_moves = []
    for (x, y) in all_moves:
        if(x >= 0 and x < 8 and y >= 0  and y < 8):
            valid_moves.append((x, y))

    return valid_moves


def solution(src, dest):
    if src == dest:
        return 0

    # Get the current and target tile
    src_x, src_y = pos_to_coords(src)
    dst_x, dst_y = pos_to_coords(dest)
    
    # Create a queue with all the positions I need to check
    queue = get_possible_moves(src_x, src_y)
    depth_queue = []

    # the depth, or solution
    depth = 0 

    while True:
        depth += 1

        # We check each move available at this depth
        for move in queue:
            # Let's see if we arrived to destination
            if move[0] == dst_x and move[1] == dst_y:
                return depth

            # we build the next depth queue, which will replace the queue after we tested them all
            # this is necessary to test one level at a time
            depth_queue.extend(get_possible_moves(move[0], move[1]))

        queue = depth_queue
        depth_queue = []

print(solution(8, 63))