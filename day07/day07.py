import functools

def hand_type_joker(hand):
    if "J" not in hand:
        return hand_type(hand)
    
    hand_set = set(hand)

    if len(hand_set) == 1 or len(hand_set) == 2:
        return 0
    if len(hand_set) == 3:
        return 1
    if len(hand_set) == 4:
        return 3
    if len(hand_set) == 5:
        return 5


def hand_type(hand):
    hand_set = set(hand)
    num_of_chars = [hand.count(x) for x in hand_set]

    if len(hand_set) == 1:
        return 0
    if len(hand_set) == 2:
        if 1 in num_of_chars and 4 in num_of_chars:
            return 1
        elif 2 in num_of_chars and 3 in num_of_chars:
            return 2
    if len(hand_set) == 3:
        if 3 in num_of_chars:
            return 3
        else:
            return 4
    if len(hand_set) == 4:
        return 5
    if len(hand_set) == 5:
        return 6

    return -1

type_function = hand_type
cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
def compare_hands(a, b):
    hand_a = a[0]
    hand_b = b[0]
    types = {}

    for hand in [hand_a, hand_b]:
        types[hand] = type_function(hand)

    if types[hand_a] < types[hand_b]:
        return 1
    elif types[hand_a] > types[hand_b]:
        return -1
    elif types[hand_a] == types[hand_b]:
        for idx, card in enumerate(hand_a):
            if cards.index(card) < cards.index(hand_b[idx]):
                return 1
            elif cards.index(card) > cards.index(hand_b[idx]):
                return -1

    
    return 0

def day07():
    with open("input.txt") as file:
        hand_bids = [x.strip().split(" ") for x in file.readlines()]
    hand_bids = sorted(hand_bids, key=functools.cmp_to_key(compare_hands))

    count = 0
    for idx, hand_bid in enumerate(hand_bids):
        count += int(hand_bid[1]) * (idx + 1)

    return count

print(day07())
type_function = hand_type_joker
cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
print(day07())