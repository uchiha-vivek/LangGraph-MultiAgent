from flask import Flask, request, jsonify
 
import requests

app = Flask(__name__)
 

# Your ATTOM API Key
ATTOM_API_KEY = "fee7f335168f8b704468d69cc740d721"

# Base URL for ATTOM API
ATTOM_BASE_URL = "https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/basicprofile"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # 1. Get the user's message from frontend
        data = request.get_json()
        user_message = data.get("message", "")
        
        # 2. Parse the address from the user input
        # (Simplified — in real use, you might want NLP or a form for address parts)
        if "," not in user_message:
            return jsonify({"reply": "Please provide the address in '123 Main St, City, State' format."})

        address_parts = user_message.split(",", 1)
        address1 = address_parts[0].strip()
        address2 = address_parts[1].strip()

        # 3. Call the ATTOM API
        headers = {
            "accept": "application/json",
            "apikey": ATTOM_API_KEY
        }

        params = {
            "address1": address1,
            "address2": address2
        }

        attom_response = requests.get(ATTOM_BASE_URL, headers=headers, params=params)

        if attom_response.status_code == 200:
            attom_data = attom_response.json()
            # Extract something meaningful from the response
            try:
                property_info = attom_data['property'][0]
                address = property_info.get('address', {})
                building = property_info.get('building', {})
                summary = f"{address.get('line1')}, {address.get('locality')}, {address.get('state')}:\n" \
                          f"Beds: {building.get('rooms', {}).get('beds')}, " \
                          f"Baths: {building.get('rooms', {}).get('baths')}, " \
                          f"Year Built: {building.get('yearbuilt')}, " \
                          f"Sqft: {building.get('size', {}).get('livingsize')}"
                return jsonify({"reply": summary})
            except (KeyError, IndexError):
                return jsonify({"reply": "Sorry, I couldn't find property details for that address."})
        else:
            return jsonify({
                "reply": f"Error from ATTOM API: {attom_response.status_code} - {attom_response.text}"
            })

    except Exception as e:
        return jsonify({"reply": f"Internal server error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)