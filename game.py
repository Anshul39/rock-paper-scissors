"""
Rock Paper Scissors Game
A simple but complete game you can play!
Author: Your Name
"""

import random
import time

class RockPaperScissors:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.moves = ['rock', 'paper', 'scissors']
        self.emoji = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
        
    def get_computer_move(self):
        """Computer chooses randomly"""
        return random.choice(self.moves)
    
    def get_winner(self, player, computer):
        """Determine who wins the round"""
        if player == computer:
            return "tie"
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissors' and computer == 'paper'):
            return "player"
        else:
            return "computer"
    
    def play_round(self, player_move):
        """Play one round of the game"""
        computer_move = self.get_computer_move()
        
        # Show moves
        print(f"\nYou: {self.emoji[player_move]} {player_move.upper()}")
        print(f"Computer: {self.emoji[computer_move]} {computer_move.upper()}")
        
        # Get winner
        winner = self.get_winner(player_move, computer_move)
        
        if winner == "player":
            self.player_score += 1
            print("✅ YOU WIN this round!")
        elif winner == "computer":
            self.computer_score += 1
            print("❌ Computer wins this round!")
        else:
            print("🤝 It's a tie!")
        
        self.rounds_played += 1
        self.show_score()
    
    def show_score(self):
        """Display current score"""
        print(f"\n📊 SCORE: You {self.player_score} - {self.computer_score} Computer")
    
    def play_game(self):
        """Main game loop"""
        print("="*50)
        print("🎮 ROCK PAPER SCISSORS GAME")
        print("="*50)
        print("\nHow to play:")
        print("  • Type 'rock', 'paper', or 'scissors'")
        print("  • Type 'quit' to exit")
        print("  • First to 5 points wins!")
        print("-"*50)
        
        while True:
            # Get player move
            player_move = input("\nYour move (rock/paper/scissors): ").lower().strip()
            
            # Check for quit
            if player_move == 'quit':
                break
            
            # Validate input
            if player_move not in self.moves:
                print("❌ Invalid move! Please type rock, paper, or scissors")
                continue
            
            # Play round
            self.play_round(player_move)
            
            # Check for game winner
            if self.player_score >= 5:
                print("\n" + "🎉"*10)
                print("🎉 CONGRATULATIONS! YOU WON THE GAME! 🎉")
                print("🎉"*10)
                break
            elif self.computer_score >= 5:
                print("\n" + "💻"*10)
                print("💻 COMPUTER WINS! Better luck next time! 💻")
                print("💻"*10)
                break
        
        # Game over
        print("\n" + "="*50)
        print("GAME OVER")
        print(f"Final Score: You {self.player_score} - {self.computer_score} Computer")
        print(f"Rounds Played: {self.rounds_played}")
        print("="*50)

# Simple version - just play!
def simple_game():
    """Even simpler version - just one function"""
    score = 0
    computer_score = 0
    moves = ['rock', 'paper', 'scissors']
    
    print("🎮 ROCK PAPER SCISSORS")
    print("="*30)
    
    while True:
        # Get player move
        player = input("\nEnter move (r/p/s or quit): ").lower()
        
        if player == 'quit':
            break
        
        # Convert shortcuts
        if player == 'r': player = 'rock'
        elif player == 'p': player = 'paper'
        elif player == 's': player = 'scissors'
        
        # Validate
        if player not in moves:
            print("❌ Invalid! Use r, p, or s")
            continue
        
        # Computer move
        computer = random.choice(moves)
        
        # Show moves
        print(f"You: {player}  vs  Computer: {computer}")
        
        # Determine winner
        if player == computer:
            print("Tie!")
        elif (player == 'rock' and computer == 'scissors') or \
             (player == 'paper' and computer == 'rock') or \
             (player == 'scissors' and computer == 'paper'):
            print("✅ You win!")
            score += 1
        else:
            print("❌ Computer wins!")
            computer_score += 1
        
        # Show score
        print(f"Score: You {score} - {computer_score} Computer")
    
    print(f"\nFinal Score: You {score} - {computer_score} Computer")

# Run the game
if __name__ == "__main__":
    print("Choose game mode:")
    print("1. Full Game (with emojis)")
    print("2. Simple Game")
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        game = RockPaperScissors()
        game.play_game()
    else:
        simple_game()