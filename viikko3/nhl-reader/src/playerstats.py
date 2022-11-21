class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
    
    def top_scorers_by_nationality(self, nationality):
       
        sortedPlayers = list(filter(lambda p: p.nationality == nationality, self.reader.players))
        sortedPlayers.sort(key=lambda p : p.assists + p.goals, reverse=True)
        return sortedPlayers



