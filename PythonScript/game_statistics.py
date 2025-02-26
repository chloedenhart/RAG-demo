from typing import Dict, List
from collections import defaultdict

class GameStatistics:
    def __init__(self):
        self.rounds_played = 0
        self.total_claimed = 0
        self.final_pot = 0
        self.game_completed = False
        self.end_condition = None
        self.player_claims = defaultdict(list)  # Maps player_id to list of their claims

    def compute_summary(self) -> Dict:
        """Compute summary statistics for the game"""
        return {
            'rounds_played': self.rounds_played,
            'total_claimed': self.total_claimed,
            'final_pot': self.final_pot,
            'end_condition': self.end_condition,
            'player_claims': dict(self.player_claims)
        }