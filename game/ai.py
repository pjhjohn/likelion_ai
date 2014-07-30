import random
import result
import const1 as constant

constant.status_missed = -2
constant.status_hit = -1
constant.status_empty = 0

constant.result_invalid = -2
constant.result_alredy = -1
constant.result_missed = 0
constant.result_hit = 1
constant.result_sink = 2
constant.result_win = 3

def guess_helper(location, result):

    board = result.board
    x = location[0]
    y = location[1]

    guess = {'x':None,'y':None}

    if x == None or y == None:
        while board[y][x] < 0:
            x = random.randint(0,9)
            y = random.randint(0,9)

    guess['x'] = x
    guess['y'] = y

    return guess

def guess(result):
    """
    return  
    """
    # user AI here

    x = 0
    y = 0
    board = result.board
    last_result = result.get_last_result()

    if "result" in last_result:
        x = last_result["guess"]["x"]
        y = last_result["guess"]["y"]

    if ("result" in last_result) and (last_result["result"] == constant.result_hit) and (x < 9) and board[y][x+1] > 0:
        x = last_result["guess"]["x"] + 1
        y = last_result["guess"]["y"]
        print "x: %d" %x
    else:
        while board[y][x] < 0:
            x = random.randint(0,9)
            y = random.randint(0,9)
    #----------------

    return (x,y)
