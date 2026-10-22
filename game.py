def calculate_stats(weight, sleep):
    agility=max(0,100 - abs((weight - 85)*2))
    mana= (sleep/8)*100
    hp= 100
    stats={"agility": agility, "mana": mana, "hp": hp}
    return stats
