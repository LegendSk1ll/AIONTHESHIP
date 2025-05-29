import json

def load_sensor_data(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

def get_status_color(value):
    """
    Funktio palauttaa tilan värikoodauksen arvon perusteella.
    Vihreä = ok, keltainen = varoitus, punainen = virhe
    """
    if value == "Hyvä":
        return "green"
    elif value == "Varoitus":
        return "yellow"
    else:
        return "red"


