import random

# Define the ranks and suits of the cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['hearts', 'diamonds', 'clubs', 'spades']

# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]

def calculate_outs(player_hand, community_cards):
    # Combine player's hand and community cards
    all_cards = player_hand + community_cards

    # Convert card ranks to numeric values (2-14)
    numeric_cards = [ranks.index(card[0]) + 2 for card in all_cards]

    # Check for different poker hands
    if is_royal_flush(all_cards):
        return "Royal Flush"
    elif is_straight_flush(all_cards):
        return "Straight Flush"
    elif is_four_of_a_kind(numeric_cards):
        return "Four of a Kind"
    elif is_full_house(numeric_cards):
        return "Full House"
    elif is_flush(all_cards):
        return "Flush"
    elif is_straight(numeric_cards):
        return "Straight"
    elif is_three_of_a_kind(numeric_cards):
        return "Three of a Kind"
    elif is_two_pair(numeric_cards):
        return "Two Pair"
    elif is_pair(numeric_cards):
        return "Pair"
    else:
        return "High Card"

def is_royal_flush(cards):
    suits = [card[1] for card in cards]
    if len(set(suits)) == 1:
        ranks = [card[0] for card in cards]
        if set(ranks) == set(['10', 'J', 'Q', 'K', 'A']):
            return True
    return False

def is_straight_flush(cards):
    if is_flush(cards) and is_straight([ranks.index(card[0]) + 2 for card in cards]):
        return True
    return False

def is_four_of_a_kind(cards):
    for rank in set(cards):
        if cards.count(rank) == 4:
            return True
    return False

def is_full_house(cards):
    rank_counts = {}
    for rank in cards:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    if 3 in rank_counts.values() and 2 in rank_counts.values():
        return True
    return False

def is_flush(cards):
    suits = [card[1] for card in cards]
    if len(set(suits)) == 1:
        return True
    return False

def is_straight(cards):
    cards = sorted(set(cards))
    if len(cards) == 5 and cards[-1] - cards[0] == 4:
        return True
    if set(cards) == set([2, 3, 4, 5, 14]):  # Ace-low straight
        return True
    return False

def is_three_of_a_kind(cards):
    for rank in set(cards):
        if cards.count(rank) == 3:
            return True
    return False

def is_two_pair(cards):
    pair_count = 0
    for rank in set(cards):
        if cards.count(rank) == 2:
            pair_count += 1
    if pair_count == 2:
        return True
    return False

def is_pair(cards):
    for rank in set(cards):
        if cards.count(rank) == 2:
            return True
    return False

# Simulate the flipping of cards and calculate the outs at each step
def simulate_poker():
    # Shuffle the deck
    random.shuffle(deck)

    # Deal two cards to the player
    player_hand = [deck.pop(), deck.pop()]

    # Initialize the community cards
    community_cards = []

    # Simulate the flipping of cards for five turns
    for turn in range(5):
        # Flip the next card and add it to the community cards
        community_cards.append(deck.pop())

        # Calculate the outs at the current step
        outs = calculate_outs(player_hand, community_cards)

        # Print the current turn, player's hand, community cards, and outs
        print(f"Turn {turn + 1}:")
        print(f"Player's hand: {player_hand}")
        print(f"Community cards: {community_cards}")
        # print(f"Outs: {outs}")
        print()

# Run the simulation
simulate_poker()
