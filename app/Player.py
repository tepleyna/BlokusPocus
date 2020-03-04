class Player:
    def __init__(self, display_name, id, color):
        self._display_name = display_name
        self._id = id
        self._color = color

    def getDisplayName(self):
        return self._display_name

    def getId(self):
        return self._id

    def getColor(self):
        return self._color

    @staticmethod
    def playerFactory(number_players, player_names = []):
        if (number_players < 1 or number_players > 4):
            # # TODO: throw an error/warning  ~~~
            pass
        COLORS = ["red","green","blue", "yellow"]
        number_players = number_players
        player_names = player_names if (len(player_names) > 0) else pf.COLORS[0:number_players]

        if (number_players != len(player_names)):
            #TODO:  add color names??
            # throw error/warning?  (probably)
            pass
        players = [Player(player_names[i],i+1,COLORS[i]) for i in range(number_players)]
        # # IDEA: give them hands of pieces? or snhould that be handled by main?
        # perhaps put it here because a player isn't "done" until
        # they have hands
        return players
