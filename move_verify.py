
# in this function is verified that the movement of the files be legal, that only can move to aviable positions
def verify_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column, file_one, file_two, player_move_one, player_move_two):
    if (pos_select_row+1, pos_select_column+1) in ((1,1), (1,4), (1,7), (4,1), (7,1), (7,4), (7,7), (4,7)):
        if (pos_move_to_row+1, pos_move_to_column+1) in ((pos_select_row+1, pos_select_column+4), (pos_select_row+1, pos_select_column-2), (pos_select_row+4, pos_select_column+1), (pos_select_row-2, pos_select_column+1)):
            if file_one.turn+1 > file_two.turn:
                player_move_one.fun_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column)

            if file_two.turn > file_one.turn:
                player_move_two.fun_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column)

    if (pos_select_row+1, pos_select_column+1) in ((2,2), (2,4), (2,6), (4,2), (6,2), (6,4), (6,6), (4,6)):
        if (pos_move_to_row+1, pos_move_to_column+1) in ((pos_select_row+1, pos_select_column+3), (pos_select_row+1, pos_select_column-1), (pos_select_row+3, pos_select_column+1), (pos_select_row-1, pos_select_column+1)):
            if file_one.turn+1 > file_two.turn:
                player_move_one.fun_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column)

            if file_two.turn > file_one.turn:
                player_move_two.fun_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column)
        
    if (pos_select_row+1, pos_select_column+1) in ((4,1), (4,2), (4,6), (4,7)):
        if (pos_move_to_row+1, pos_move_to_column+1) in ((pos_select_row+1, pos_select_column+2), (pos_select_row+1, pos_select_column)):  
            if file_one.turn+1 > file_one.turn:
                player_move_one.fun_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column)

            if file_two.turn > file_one.turn:
                player_move_two.fun_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column)
                    
    if (pos_select_row+1, pos_select_column+1) in ((1,4), (2,4), (6,4), (7,4)):
        if (pos_move_to_row+1, pos_move_to_column+1) in ((pos_select_row+2, pos_select_column+1), (pos_select_row, pos_select_column+1)):  
            if file_one.turn+1 > file_two.turn:
                player_move_one.fun_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column)

            if file_two.turn > file_one.turn:
                player_move_two.fun_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column)
                    
    if (pos_select_row+1, pos_select_column+1) in ((3,3), (3,4), (3,5), (4,3), (5,3), (5,4), (5,5), (4,5)):
        if (pos_move_to_row+1, pos_move_to_column+1) in ((pos_select_row+1, pos_select_column+2), (pos_select_row+1, pos_select_column), (pos_select_row+2, pos_select_column+1), (pos_select_row, pos_select_column+1)):
            if file_one.turn+1 > file_two.turn:
                player_move_one.fun_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column)

            if file_two.turn > file_one.turn:
                player_move_two.fun_move(pos_select_row, pos_select_column, pos_move_to_row, pos_move_to_column)