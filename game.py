from datetime import datetime, timedelta

def calculate_stats(weight, sleep, streak):
    agility=max(0,100 - abs((weight - 85)*2))
    mana= (sleep/8)*100
    hp= 100
    luck = streak * 10
    stats={"agility": agility, "mana": mana, "hp": hp, "luck": luck}
    return stats

def calculate_streak(rows):
    if not rows:
        return 0

    dates = set()
    for row in rows:
        dates.add(row[3])

    streak = 0
    today = datetime.now()

    while True:
        check_date = today - timedelta(days=streak)
        if check_date.strftime("%Y-%m-%d") in dates:
            streak = streak + 1
        else:
            break
    return streak
