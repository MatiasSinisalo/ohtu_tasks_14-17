class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points = self.player1_points + 1
        else:
            self.player2_points = self.player2_points + 1

    def get_score(self):
        score = ""

        game_draw = self.player1_points == self.player2_points
        player_1_advantage_or_win = self.player1_points >= 4
        player_2_advantage_or_win = self.player2_points >= 4

        if game_draw:
           score = self.set_draw_score()
        elif player_1_advantage_or_win or player_2_advantage_or_win:
            score = self.set_advantage_or_win_score()
        else:
            score = self.update_score()

        return score
    def set_draw_score(self):
        score = ""
        if self.player1_points == 0:
            score = "Love-All"
        elif self.player1_points == 1:
            score = "Fifteen-All"
        elif self.player1_points == 2:
            score = "Thirty-All"
        elif self.player1_points == 3:
            score = "Forty-All"
        else:
            score = "Deuce"
        return score
    
    def set_advantage_or_win_score(self):
        score = ""
        minus_result = self.player1_points - self.player2_points
        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score
    

    def generate_normal_score(self, player_points):
        score = ""
        if player_points == 0:
            score = score + "Love"
        elif player_points == 1:
            score = score + "Fifteen"
        elif player_points == 2:
            score = score + "Thirty"
        elif player_points == 3:
            score = score + "Forty"
        return score


    def update_score(self):
        score = ""
       
        score = score + self.generate_normal_score(self.player1_points)

        score = score + "-"
        
        score = score + self.generate_normal_score(self.player2_points)

        return score

    
