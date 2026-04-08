def grade_email(action):
    if "spam" in action.lower():
        return 1.0
    return 0.0

def grade_schedule(action):
    if "calendar" in action.lower():
        return 1.0
    return 0.0

def grade_support(action):
    if "apologize" in action.lower():
        return 1.0
    return 0.0