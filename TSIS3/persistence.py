import json

def load_settings():
    try:
        with open("settings.json") as f:
            return json.load(f)
    except:
        return {"sound": True, "color": "blue", "difficulty": "normal"}

def save_settings(data):
    with open("settings.json", "w") as f:
        json.dump(data, f, indent=4)

def load_leaderboard():
    try:
        with open("leaderboard.json") as f:
            return json.load(f)
    except:
        return []

def save_score(entry):
    data = load_leaderboard()
    data.append(entry)

    # сортировка топ 10
    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    with open("leaderboard.json", "w") as f:
        json.dump(data, f, indent=4)