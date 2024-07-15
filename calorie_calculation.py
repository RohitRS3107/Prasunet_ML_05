calorie_map = {
    'freshapples': 95,
    'freshbanana': 105,
    'freshoranges': 62,
    'rottenapples': 95,
    'rottenbanana': 105,
    'rottenoranges': 62
}

def get_calories(predicted_class):
    return calorie_map[predicted_class]