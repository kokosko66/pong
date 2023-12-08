class Score:
    def __init__(self):
        self.score_player1 = 0
        self.score_player2 = 0

    def increment_player1(self):
        self.score_player1 += 1

    def increment_player2(self):
        self.score_player2 += 1

    def get_score_text(self):
        return f"{self.score_player1} | {self.score_player2}"
