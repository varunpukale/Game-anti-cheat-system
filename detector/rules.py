def check_speed(event):
    """
    Detects unrealistic movement speed (speed hack)
    """
    speed = event.get("speed", 0)
    
    if speed > 100:
        return True
    
    return False


def check_bot(event):
    """
    Detects bot-like behavior based on action frequency
    """
    actions = event.get("actions_per_sec", 0)
    
    if actions > 20:
        return True
    
    return False
