import hashlib

def generate_trueval_id(postcode, door_number, unit='', lat=None, lon=None):
    base = f"{postcode}_{door_number}_{unit}".lower().replace(' ', '').replace(',', '').replace('.', '')
    if lat and lon:
        latlon_hash = hashlib.md5(f"{lat}_{lon}".encode()).hexdigest()[:6]
    else:
        latlon_hash = "unknown"
    return f"trueval_{base}_{latlon_hash}"
