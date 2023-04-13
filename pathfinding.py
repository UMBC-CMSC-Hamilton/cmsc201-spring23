import random

BLOCKED = ' * '
EMPTY = " _ "
FINISH = ' f '
VISITED = ' v '


def build_grid(height, width, prob):
    my_grid = []
    for i in range(height):
        new_row = []
        for j in range(width):
            # floating point number between [0, 1]
            if random.random() < prob:
                new_row.append(BLOCKED)
            else:
                new_row.append(EMPTY)
        my_grid.append(new_row)
    
    finish_x = random.randint(0, width - 1)
    finish_y = random.randint(0, height - 1)
    
    my_grid[finish_y][finish_x] = FINISH
    my_grid[0][0] = EMPTY
    return my_grid


def display_grid(the_grid):
    for row in the_grid:
        print(''.join(row))


def find_the_finish(the_map, current_pos, height, width, visited, step):
    """
        current_pos = (0, 0)
        
        left, down, right, up
    """
    current_y = current_pos[0]
    current_x = current_pos[1]
    # use if rather than elif becuase we want it to try others paths if the first one fails
    
    if current_pos in visited:
        return []
    
    print(current_pos)
    
    if the_map[current_y][current_x] == FINISH:
        return [(current_y, current_x)]
    
    visited.append(current_pos)
    the_map[current_y][current_x] = ' ' + str(step).zfill(2)
    
    # go left
    if current_x + 1 < width and the_map[current_y][current_x + 1] != BLOCKED:
        the_path = find_the_finish(the_map, (current_y, current_x + 1), height, width, visited, step + 1)
        if the_path:
            return [current_pos] + the_path
    # go down
    if current_y + 1 < height and the_map[current_y + 1][current_x] != BLOCKED:
        the_path = find_the_finish(the_map, (current_y + 1, current_x), height, width, visited, step + 1)
        if the_path:
            return [current_pos] + the_path
    # go right
    if 0 <= current_x - 1 and the_map[current_y][current_x - 1] != BLOCKED:
        the_path = find_the_finish(the_map, (current_y, current_x - 1), height, width, visited, step + 1)
        if the_path:
            return [current_pos] + the_path
    # go up
    if 0 <= current_y - 1 < width and the_map[current_y - 1][current_x] != BLOCKED:
        the_path = find_the_finish(the_map, (current_y - 1, current_x), height, width, visited, step + 1)
        if the_path:
            return [current_pos] + the_path
    
    return []


the_grid = build_grid(10, 10, 0.25)
display_grid(the_grid)
print(find_the_finish(the_grid, (0, 0), 10, 10, [], 1))
display_grid(the_grid)
