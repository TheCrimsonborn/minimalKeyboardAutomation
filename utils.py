import json
from pynput.keyboard import Key


def load_special_buttons():
    """Load special key mappings from a JSON file."""
    try:
        with open("keys.json", "r") as file:
            data = json.load(file)
            return {key: getattr(Key, value) for key, value in data.items()}
    except AttributeError as e:
        print(f"Invalid key in the Key class: {e}")
        return {}
    except Exception as e:
        print(f"Error loading special keys: {e}")
        return {}
