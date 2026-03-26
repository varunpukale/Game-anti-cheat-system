from detector.rules import check_speed, check_bot

def detect_cheat(event):
    # Check speed hack
    if check_speed(event):
        return {
            "cheater": True,
            "reason": "Speed hack detected"
        }

    # Check bot behavior
    if check_bot(event):
        return {
            "cheater": True,
            "reason": "Bot behavior detected"
        }

    return {
        "cheater": False
    }
