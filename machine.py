from debug import debug
from reel import *
from wins import *
from settings import *
from ui import UI
from player import *
import pygame

class Machine:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.machine_balance = 10000.00
        self.reel_index = 0
        self.reel_list = {}
        self.can_toggle = True
        self.spining = False
        self.win_animation_ongoing = False

        # Results
        self.prev_result = {0: None, 1: None, 2: None, 3: None, 4: None}
        self.spin_result = {0: None, 1: None, 2: None, 3: None, 4: None}

        # Initialize player and UI
        self.currPlayer = Player()
        self.ui = UI(self.currPlayer)
        
        # Spawn the reels
        self.spawn_reels()

    def spawn_reels(self):
        if not self.reel_list:
            x_topleft, y_topleft = 10, -300  # Start position

        while self.reel_index < 5:
            if self.reel_index == 0:
                x_topleft += 143 
            elif self.reel_index == 1:
                x_topleft -= 143 
            elif self.reel_index == 2:
                x_topleft -= 143
            elif self.reel_index == 3:
                x_topleft -= 143 
            elif self.reel_index == 4:
                x_topleft -= 143 

            # Create the reel with the adjusted position
            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft))

            # Adjust x_topleft to move the reels horizontally
            x_topleft += 300

            # Keep y_topleft constant to stack the reels vertically
            # Optionally, adjust it slightly if you want a small gap, e.g., y_topleft += 10

            self.reel_index += 1

    def coolsdowns(self):
        # Only let the player spin if all reels are NOT spinning
        for reel in self.reel_list:
            if self.reel_list[reel].reel_is_spinning:
                self.can_toggle = False
                self.spining = True

        if not self.can_toggle and [self.reel_list[reel].reel_is_spinning for reel in self.reel_list].count(False) == 5:
            self.can_toggle = True
            self.spin_result = self.get_result()

            if self.check_win(self.spin_result):
                self.win_data = self.check_win(self.spin_result)
                # Play the win sound
                # self.play_win_sound(self.win_data)
                self.pay_player(self.win_data, self.currPlayer)
                # self.win_animation_ongoing = True
                # self.ui.win_text_angle = random.randint(-4, 4)

    def input(self):
        keys = pygame.key.get_pressed()

        # Checks for space key, ability to toggle spin, and balance to cover bet size
        if keys[pygame.K_SPACE] and self.can_toggle and self.currPlayer.balance >= self.currPlayer.bet_size:
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()
            self.currPlayer.place_bet()
            self.machine_balance += self.currPlayer.bet_size
            self.currPlayer.last_payout = None

    def draw_reels(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].animate(delta_time)

    def toggle_spinning(self):
        if self.can_toggle:
            self.spin_time = pygame.time.get_ticks()
            self.spining = not self.spining
            self.can_toggle = False

            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * 200)
                # self.spin_sound.play()

    def check_win(self, result):
        hits = {}
        horizontal = flip_horizontal(result)
        for row in horizontal:
            for sym in row:
                if row.count(sym) > 2:  # Potential win
                    possible_win = [idx for idx, val in enumerate(row) if sym == val]

                    # Check possible win for a subsequence longer than 2 and add to hits
                    if len(longest_seq(possible_win)) > 2:
                        hits[horizontal.index(row) + 1] = [sym, longest_seq(possible_win)]
        if hits:
            return hits

    def get_result(self):
        for reel in self.reel_list:
            self.spin_result[reel] = self.reel_list[reel].reel_spin_result()
        return self.spin_result

    def pay_player(self, win_data, curr_player):
        multiplier = 0
        spin_payout = 0

        for v in win_data.values():
            multiplier += len(v[1])
        spin_payout = (multiplier * curr_player.bet_size)
        curr_player.balance += spin_payout
        self.machine_balance -= spin_payout            
        curr_player.total_won += spin_payout
        curr_player.last_payout = spin_payout

    def update(self, delta_time):
        self.coolsdowns()
        self.input()
        self.draw_reels(delta_time)
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()
        self.ui.update()

        # Balance/payout debugger
        """
        debug_player_data = self.currPlayer.get_data()
        machine_balance = "{:.2f}".format(self.machine_balance)
        if self.currPlayer.last_payout:
            last_payout = "{:.2f}".format(self.currPlayer.last_payout)
        else:
            last_payout = "N/A"

        debug(f"Player balance: {debug_player_data['balance']} | Machine balance : {machine_balance} | Last payout {last_payout}")
        """
