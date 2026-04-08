def grade(reward, *args, **kwargs):
    # This ensures no score ever touches 0.0 or 1.0 or goes outside 0.1-0.9
    return float(max(0.2, min(0.8, float(reward))))