import requests
import json


def get_deezer_album_info(deezer_id):
    """This function retrieves album info from Deezer API
    album:str is the album ID from the deezer services and it will be stored on the backend DB"""
    url = f"https://deezerdevs-deezer.p.rapidapi.com/album/{deezer_id}"
    headers = {
        "X-RapidAPI-Key": "a29d80eb60msh011a5a400ddedf5p11052ejsn9c12bf758c97",
        "X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extracting desired fields
        extracted_data = {
            "cover": data.get("cover_medium", ""),
            "contributors": [contributor.get("name", "") for contributor in data.get("contributors", [])],
            "label": data.get("label", ""),
            "tracklist": [track.get("title", "") for track in data.get("tracks", {}).get("data", [])]
        }
        # Return the retrieved data
        return extracted_data
    else:
        print("Failed to retrieve data from the API:", response.status_code)
