from flask import request, jsonify
from utils.id_generator import generate_trueval_id
from airtable import Airtable  # configure this separately

airtable = Airtable(base_key='appShV6ffCc9yxeHF', table_name='TrueVal_1', api_key='YOUR_API_KEY')

def log_valuation():
    data = request.get_json()

    postcode = data.get("postcode", "")
    door_number = data.get("door_number", "")
    unit = data.get("unit", "")
    lat = data.get("lat")
    lon = data.get("lon")

    trueval_id = generate_trueval_id(postcode, door_number, unit, lat, lon)

    record = {
        "fields": {
            "Postcode": postcode,
            "Door Number": door_number,
            "Unit": unit,
            "Latitude": lat,
            "Longitude": lon,
            "TrueVal ID": trueval_id,
        }
    }

    airtable.insert(record["fields"])
    return jsonify({"status": "success", "trueval_id": trueval_id})
