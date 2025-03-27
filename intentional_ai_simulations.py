
import random

deck = ["Ace", "King", "Queen", "Jack", "Joker"]

class IntentionalCardAI:
    def __init__(self):
        self.belief_score = 0.5
        self.memory = {card: 1.0 for card in deck}
        self.target = "Ace"

    def draw(self):
        randomness = max(0.01, 1.0 - self.belief_score)
        adjusted_memory = {
            card: min(1e6, self.memory[card] + randomness) for card in deck
        }
        total = sum(adjusted_memory.values())
        weights = [adjusted_memory[card] / total for card in deck]
        return random.choices(deck, weights=weights)[0]

    def update_belief(self, drawn_card):
        if drawn_card == self.target:
            self.belief_score = min(1.0, self.belief_score + 0.01)
            self.memory[drawn_card] = min(1e6, self.memory[drawn_card] * 1.1)
        else:
            self.belief_score = max(0.0, self.belief_score - 0.02)
            self.memory[drawn_card] = max(0.01, self.memory[drawn_card] * 0.9)

intentional_ai = IntentionalCardAI()
intentional_aces = 0
random_aces = 0
rounds = 100000

for _ in range(rounds):
    if random.choice(deck) == "Ace":
        random_aces += 1

    card = intentional_ai.draw()
    if card == "Ace":
        intentional_aces += 1
    intentional_ai.update_belief(card)

print("Intentional AI Ace Rate:", intentional_aces / rounds)
print("Random AI Ace Rate:", random_aces / rounds)
