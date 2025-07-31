import requests
from langchain_core.tools import tool
import os
from dotenv import load_dotenv

load_dotenv()

ATTOM_API_KEY = os.getenv("ATTOM_API_KEY")
BASE_URL = os.getenv("BASE_URL")

@tool
def get_real_estate_info(address: str) -> str:
    """
    Fetches real estate valuation and property data using ATTOM's AVM API.
    Expects full address as a string like "123 Main St, Los Angeles CA".
    """
    try:
        street, city_state = address.split(",", 1)
        city_state = city_state.strip().upper().split()
        city = " ".join(city_state[:-1])
        state = city_state[-1]

        params = {
            "address1": street.strip(),
            "address2": f"{city} {state}"
        }

        headers = {
            "Accept": "application/json",
            "apikey": ATTOM_API_KEY
        }

        response = requests.get(BASE_URL, params=params, headers=headers)
        data = response.json()

        if response.status_code != 200:
            return f"ATTOM API Error {response.status_code}: {data}"

        prop = data.get("property", [{}])[0]

        # Extract AVM data
        avm = prop.get("avm", {}).get("amount", {})
        est_value = avm.get("value")
        confidence = avm.get("scr")

        # Extract building and room info
        building = prop.get("building", {})
        rooms = building.get("rooms", {})
        size = building.get("size", {})
        summary = prop.get("summary", {})

        beds = rooms.get("beds")
        baths = rooms.get("bathstotal")
        sqft = size.get("livingsize")
        year_built = summary.get("yearbuilt")

        return (
            f"🏠 Property Info for {address}:\n"
            f"Estimated Value: ${est_value:,} (Confidence Score: {confidence})\n"
            f"Beds: {beds}, Baths: {baths}, Year Built: {year_built}, Sqft: {sqft} sqft"
        )

    except Exception as e:
        return f"Error fetching data: {str(e)}"
