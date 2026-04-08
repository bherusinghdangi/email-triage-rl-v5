def grade(reward, *args, **kwargs):
    # Strictly clamps any input to the allowed 0.1 - 0.9 range
    return float(max(0.15, min(0.85, float(reward))))