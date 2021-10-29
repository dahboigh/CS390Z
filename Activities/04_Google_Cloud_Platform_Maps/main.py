import requests
import os
from urllib.parse import urlencode

# definitions/parameters
STATIC_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/staticmap'
LOCATION_TO_MAP = 'Metropolitan State University of Denver'
ZOOM = '15'
SIZE = '800x600'
IMAGE_FILE_NAME = 'msudenver.png'

# requirements: API_KEY environment variable
if __name__ == "__main__":

    # encode URL
    params = {
        'center': LOCATION_TO_MAP,
        'zoom': ZOOM,
        'size': SIZE,
        'key': os.getenv('Google_API_Key')
    }
    url = STATIC_MAPS_API_URL + '?' + urlencode(params)

    # make the API call and save the result as a png image
    result = requests.get(url)
    if result.status_code == 200:
        with open(IMAGE_FILE_NAME, 'wb') as image:
            image.write(result.content)
        print('Map image saved in ' + IMAGE_FILE_NAME)
    else:
        print(result)

        for i in result:
            print(i)
