class Board:
    """
    battleships : (list) list of battleships
    """
    def __init__( self, battleships ):
        self.battleships = battleships
        self.remaining = 17  # remaining numbers of battleships' tiles
        self.board = [] # status of each tile on the board. 0 = empty, 1 = occupied, -1 = hit, -2 = missed
        
        for x in range(10): 
            self.board.append( [0] * 10 )

        for battleship in battleships:
            for coordinate in battleship.coordinates:
                if self.board[ coordinate['y'] ][ coordinate['x'] ] > 0 :
                    raise ValueError("battleships overlap at (%d,%d)! %(coordinate['x'],coordinate['y'])")
                else:
                    self.board[ coordinate['y'] ][ coordinate['x'] ] = battleship.ship_id # change occupied tile to 1

    def hit( self, player, guess ):
        """
        check if guess hit
        guess : (dic) guess location
        """
        if ( guess['x'] > 9 or guess['x'] < 0 ) or ( guess['y'] > 9 or guess['y'] < 0 ):
            return {"player":player, "guess":{"x":guess['x'],"y":guess['y']}, "result":-2, "sink":None}

        else:
            coordinate = self.board[ guess['y'] ][ guess['x'] ]
            if coordinate < 0:
                return {"player":player, "guess":{"x":guess['x'],"y":guess['y']}, "result":-1, "sink":None}

            elif coordinate == 0:
                self.board[ guess['y'] ][ guess['x'] ] = -2
                return {"player":player, "guess":{"x":guess['x'],"y":guess['y']}, "result":0, "sink":None}

            elif coordinate > 0 :
                hit_ship_id = self.board[ guess['y'] ][ guess['x'] ]

                self.board[ guess['y'] ][ guess['x'] ] = -1
                self.remaining -= 1
                self.battleships[ ( hit_ship_id - 1 ) ].health -= 1
                if self.battleships[ ( hit_ship_id - 1 ) ].health == 0:
                    if self.remaining == 0:
                        return {"player":player, "guess":{"x":guess['x'],"y":guess['y']}, "result":3, "sink":hit_ship_id}
                    else:
                        return {"player":player, "guess":{"x":guess['x'],"y":guess['y']}, "result":2, "sink":hit_ship_id}

                else:
                    return {"player":player, "guess":{"x":guess['x'],"y":guess['y']}, "result":1, "sink":None}
