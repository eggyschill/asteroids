# Create a new file: managers/highscores.py
import json
import os

class HighScoreManager:
    def __init__(self):
        self.high_scores = []
        self.scores_file = "highscores.json"
        self.load_scores()
        
    def load_scores(self):
        try:
            if os.path.exists(self.scores_file):
                with open(self.scores_file, 'r') as f:
                    self.high_scores = json.load(f)
            else:
                self.high_scores = []
        except:
            self.high_scores = []
            
    def save_scores(self):
        with open(self.scores_file, 'w') as f:
            json.dump(self.high_scores, f)
            
    def check_score(self, score):
        """Returns True if score is a high score"""
        if len(self.high_scores) < 5:
            return True
        return score > min(self.high_scores)
            
    def add_score(self, score):
        """Add a new score and maintain only top 5"""
        self.high_scores.append(score)
        self.high_scores.sort(reverse=True)
        self.high_scores = self.high_scores[:5]  # Keep only top 5
        self.save_scores()
        
    def get_scores(self):
        """Return the list of high scores"""
        return sorted(self.high_scores, reverse=True)