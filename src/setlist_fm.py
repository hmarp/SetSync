"""
Module for interacting with the Setlist.fm API.
"""

from typing import List
import requests
import config

def get_setlist(artist_name: str, city: str, date: str) -> List[str]:
    """
    Fetches the setlist for a given artist, city, and date from the Setlist.fm API.
    Args:
        artist_name (str): Name of the artist.
        city (str): City where the concert took place.
        date (str): Date of the concert in 'YYYY-MM-DD' format.
    Returns:
        List[str]: A list of song names in the setlist.
    """
    search_url = f'{config.SETLISTFM_API_BASE_URL}/search/setlists?'

    params = {
        "artistName": artist_name,
        "cityName": city,
        "date": date
    }

    try:
        response = requests.get(
            url = search_url,
            params = params,
            headers = {
                'x-api-key': config.SETLISTFM_API_KEY,
                'Accept': 'application/json'
            },
            timeout=5
        )

        response.raise_for_status()

        data = response.json()
        setlists = data.get('setlist', [])

        if not setlists:
            raise ValueError('No setlist found for the given artist, city, and date.')

        setlist = setlists[0]['sets']['set'][0]['song']

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        raise http_err
    except (IndexError, KeyError, TypeError) as setlist_error:
        print(f"Error accessing setlist data: {setlist_error}")
        raise setlist_error
    except Exception as e:
        print(f'Error fetching setlist: {e}')
        raise e

    return setlist
