

# Board for testing the Eval function
test_board = [[0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 2, 0, 2, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 1, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 1, 2, 2, 0, 0, 2, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 1, 0, 0], 
              [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Returns the eval value for rows
def row_eval(board, team):
    board_size = 15

    # Dictionary that takes into account [NumOfPieces : [WithZeroOpenedPlaces, WithOneOpenedPlaces, WithTwoOpenedPlaces]]
    board_count = {1:[0,0,0], 2:[0,0,0], 3:[0,0,0], 4:[0,0,0]}

    for y in range(board_size):
        # x = 0      
        # start_ind = 0
        # end_ind = 0        
        for x in range(board_size):
            consec = 0 # Track of Consecutives in a row
            open_ends = 0 # Track of respective opened space with consecutives
            if board[y][x].value == team:
                if x > 0: # Check for the boundary conditions
                    if board[y][x-1].value == 0: # If empty, means an opened space
                        open_ends += 1
                consec += 1

                i = 1           

                # Lets check for the consecutives after the current piece
                while True:
                    if x+i < board_size:
                        if board[y][x+i].value == team: # Increase the consecutives
                            consec += 1
                        elif board[y][x+i].value != team: # Check for opened spaces and stop
                            if board[y][x+i].value == 0:
                                open_ends += 1
                            break
                    elif x+i == board_size: # Stops at the boundary condition
                        break  
                    i += 1

                if 0 < consec < 5 and open_ends > 0: # If not the winning condition in a row
                    board_count[consec][open_ends] += 1 # Update the dictionary
                elif consec == 5: # If winning condition in a row
                    return 1000000
                # print(x)
                # print(board_count)

                # Resetting the consecutive count and the opened spaces count before going backwards
                consec = 1
                open_ends = 0

                if x < board_size-1: # Check for the boundary conditions
                    if board[y][x+1].value == 0: # If empty, means an opened space
                        open_ends += 1

                j = 1

                # Lets check for the consecutives before the current piece
                while True:
                    if x-j >= 0:
                        if board[y][x-j].value == team:  # Increase the consecutives
                            consec += 1
                        elif board[y][x-j].value != team: # Check for opened spaces and stop
                            if board[y][x-j].value == 0:
                                open_ends += 1
                            break
                    elif x-j < 0: # Stops at the boundary condition
                        break  
                    j += 1
                
                if 0 < consec < 5 and open_ends > 0:  # If not the winning condition in a row
                    board_count[consec][open_ends] += 1 # Update the dictionary
            #     print(board_count)

            # print("-------------------------------------------")
    # Lets evaluate on the basis of data about consecutive pieces and opened spaces
    # print(board_count)
    row_eval = 0.0
    for consecs in board_count:
        for i in range(len(board_count[consecs])):
            w = assign_weights(consecs, i) # Acquire the respective weights
            row_eval += board_count[consecs][i] * w # Calculate the weighted sum

    return row_eval

# Returns the eval value for columns
def col_eval(board, team):
    board_size = 15

    # Dictionary that takes into account [NumOfPieces : [WithZeroOpenedPlaces, WithOneOpenedPlaces, WithTwoOpenedPlaces]]
    board_count = {1:[0,0,0], 2:[0,0,0], 3:[0,0,0], 4:[0,0,0]}

    for y in range(board_size):
        # x = 0      
        # start_ind = 0
        # end_ind = 0        
        for x in range(board_size):
            consec = 0 # Track of Consecutives in a row
            open_ends = 0 # Track of respective opened space with consecutives
            if board[x][y].value == team:
                if x > 0: # Check for the boundary conditions
                    if board[x-1][y].value == 0: # If empty, means an opened space
                        open_ends += 1
                consec += 1

                i = 1

                # Lets check for the consecutives after the current piece
                while True:
                    if x+i < board_size:
                        if board[x+i][y].value == team: # Increase the consecutives
                            consec += 1
                        elif board[x+i][y].value != team: # Check for opened spaces and stop
                            if board[x+i][y].value == 0:
                                open_ends += 1
                            break
                    elif x+i == board_size: # Stops at the boundary condition
                        break  
                    i += 1

                if 0 < consec < 5 and open_ends > 0: # If not the winning condition in a row
                    board_count[consec][open_ends] += 1 # Update the dictionary
                elif consec == 5: # If winning condition in a row
                    return 1000000
                # print(x)
                # print(board_count)

                # Resetting the consecutive count and the opened spaces count before going backwards
                consec = 1
                open_ends = 0

                if x < board_size-1: # Check for the boundary conditions
                    if board[x+1][y].value == 0: # If empty, means an opened space
                        open_ends += 1

                j = 1

                # Lets check for the consecutives before the current piece
                while True:
                    if x-j >= 0:
                        if board[x-j][y].value == team:  # Increase the consecutives
                            consec += 1
                        elif board[x-j][y].value != team: # Check for opened spaces and stop
                            if board[x-j][y].value == 0:
                                open_ends += 1
                            break
                    elif x-j < 0: # Stops at the boundary condition
                        break  
                    j += 1

                
                if 0 < consec < 5 and open_ends > 0:  # If not the winning condition in a row
                    board_count[consec][open_ends] += 1 # Update the dictionary
            #     print(board_count)

            # print("-------------------------------------------")
    
    # Lets evaluate on the basis of data about consecutive pieces and opened spaces
   
    # print(board_count)
    col_eval = 0.0
    for consecs in board_count:
        for i in range(len(board_count[consecs])):
            w = assign_weights(consecs, i) # Acquire the respective weights
            col_eval += board_count[consecs][i] * w # Calculate the weighted sum

    return col_eval


def diag_eval(board, team):
    board_size = 15

    # Dictionary that takes into account [NumOfPieces : [WithZeroOpenedPlaces, WithOneOpenedPlaces, WithTwoOpenedPlaces]]
    board_count = {1:[0,0,0], 2:[0,0,0], 3:[0,0,0], 4:[0,0,0]}

    for y in range(board_size):  
        for x in range(board_size):
            consec = 0 # Track of Consecutives in a row
            open_ends = 0 # Track of respective opened space with consecutives
            if board[y][x].value == team:
                if x > 0 and y > 0: # Check for the boundary conditions
                    if board[y-1][x-1].value == 0: # If empty, means an opened space
                        open_ends += 1
                consec += 1

                i = 1           

                # Lets check for the consecutives after the current piece
                while True:
                    if x+i < board_size and y + i < board_size:
                        if board[y+i][x+i].value == team: # Increase the consecutives
                            consec += 1
                        elif board[y+i][x+i].value != team: # Check for opened spaces and stop
                            if board[y+i][x+i].value == 0:
                                open_ends += 1
                            break
                    elif x+i == board_size or y+i == board_size: # Stops at the boundary condition
                        break  
                    i += 1

                if 0 < consec < 5 and open_ends > 0: # If not the winning condition in a row
                    board_count[consec][open_ends] += 1 # Update the dictionary
                elif consec == 5: # If winning condition in a row
                    return 1000000
                # print(x)
                # print(board_count)

                # Resetting the consecutive count and the opened spaces count before going backwards
                consec = 1
                open_ends = 0

                if x < board_size - 1 and y < board_size -1: # Check for the boundary conditions
                    if board[y+1][x+1].value == 0: # If empty, means an opened space
                        open_ends += 1

                j = 1

                # Lets check for the consecutives before the current piece
                while True:
                    if x-j >= 0 and y- j >= 0:
                        if board[y-j][x-j].value == team:  # Increase the consecutives
                            consec += 1
                        elif board[y-j][x-j].value != team: # Check for opened spaces and stop
                            if board[y-j][x-j].value == 0:
                                open_ends += 1
                            break
                    elif x-j < 0 and y-j < 0: # Stops at the boundary condition
                        break  
                    j += 1
                
                if 0 < consec < 5 and open_ends > 0:  # If not the winning condition in a row
                    board_count[consec][open_ends] += 1 # Update the dictionary
                elif consec == 5: # If winning condition in a row
                    return 1000000
                # print(board_count)

    #_--------------------------------------------------------------------------------------------------------------------------
                consec = 1
                open_ends = 0

                if x > 0 and y < board_size - 1: # Check for the boundary conditions
                    if board[y+1][x-1].value == 0: # If empty, means an opened space
                        open_ends += 1
               

                k = 1           

                # Lets check for the consecutives after the current piece
                while True:
                    if x+k < board_size - 1 and y - k > 0:
                        if board[y-k][x+k].value == team: # Increase the consecutives
                            consec += 1
                        elif board[y-k][x+k].value != team: # Check for opened spaces and stop
                            if board[y-k][x+k].value == 0:
                                open_ends += 1
                            break
                    elif x+k == board_size or y-k == 0: # Stops at the boundary condition
                        break  
                    k += 1

                if 0 < consec < 5 and open_ends > 0: # If not the winning condition in a row
                    board_count[consec][open_ends] += 1 # Update the dictionary
                elif consec == 5: # If winning condition in a row
                    return 1000000
                
                # print(board_count)

                # Resetting the consecutive count and the opened spaces count before going backwards
                consec = 1
                open_ends = 0

                if x < board_size - 1 and y > 0: # Check for the boundary conditions
                    if board[y-1][x+1].value == 0: # If empty, means an opened space
                        open_ends += 1

                j = 1

                # Lets check for the consecutives before the current piece
                while True:
                    if x-j >= 0 and y + j <= board_size - 1:
                        if board[y+j][x-j].value == team:  # Increase the consecutives
                            consec += 1
                        elif board[y+j][x-j].value != team: # Check for opened spaces and stop
                            if board[y+j][x-j].value == 0:
                                open_ends += 1
                            break
                    elif x-j < 0 or y+j > board_size: # Stops at the boundary condition
                        break  
                    j += 1
                
                if 0 < consec < 5 and open_ends > 0:  # If not the winning condition in a row
                    board_count[consec][open_ends] += 1 # Update the dictionary
                elif consec == 5: # If winning condition in a row
                    return 1000000
            #     print(board_count, consec)

            # print("-------------------------------------------")
    # Lets evaluate on the basis of data about consecutive pieces and opened spaces
    # print(board_count)
    diag_eval = 0.0
    for consecs in board_count:
        for i in range(len(board_count[consecs])):
            w = assign_weights(consecs, i) # Acquire the respective weights
            diag_eval += board_count[consecs][i] * w # Calculate the weighted sum

    return diag_eval

# Assigns weights to different cases of consecutive pieces and opened nodes in them, 
# l -- The number of consecutive pieces
# o -- The number of associated opened spaces
def assign_weights(l, o):
    w_o = 0 
    if l == 4:
        if o == 2:
            w_o = 26.6
        elif o == 1:
            w_o = 13.3
        elif o == 0:
            w_o = 0
    elif l == 3:
        if o == 2:
            w_o = 20
        elif o == 1:
            w_o = 10
        elif o == 0:
            w_o = 0
    elif l == 2:
        if o == 2:
            w_o = 13.3
        elif o == 1:
            w_o = 6.6
        elif o == 0:
            w_o = 0
    elif l == 1:
        if o == 2:
            w_o = 6.6
        elif o == 1:
            w_o = 3.3
        elif o == 0:
            w_o = 0
    return w_o


def evaluate(board, team_1, team_2):
    row_eval_1 = row_eval(board, team_1)
    col_eval_1 = col_eval(board, team_1)
    diag_eval_1 = diag_eval(board, team_1)
    
    offensive = row_eval_1 + col_eval_1 + diag_eval_1

    row_eval_2 = row_eval(board, team_2)
    col_eval_2 = col_eval(board, team_2)
    diag_eval_2 = diag_eval(board, team_2)
    
    defensive = row_eval_2 + col_eval_2 + diag_eval_2

    return (offensive-defensive)

