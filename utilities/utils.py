import time
import requests
from Movie_Listing.settings import CREDY_MOVIE_API_USERNAME, CREDY_MOVIE_API_PASSWORD


def count_frequency(my_list):
    """
    Function Name: count_frequency

    Description: Get top 3 genres

    Params: list of genres

    Return: top 3 genres

    """
    frequency = {}
    for item in my_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    sorted_dict = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    i = 0
    favourite_genres = ''
    for key, value in sorted_dict:
        if i == 3:
            break
        favourite_genres += key + ','
        i += 1
    favourite_genres = favourite_genres[:-1]
    return favourite_genres


def retry_http_request(max_tries, url):
    """
    Function Name: retry_http_request

    Description: Retry External API call

    Params: max_tries, url

    Return: HTTP response object

    """
    for i in range(max_tries):
        try:
            time.sleep(2)
            response = requests.get(url, auth=(CREDY_MOVIE_API_USERNAME, CREDY_MOVIE_API_PASSWORD), timeout=5)
            if response.status_code == 200:
                return response
            elif i == max_tries - 1:
                return response
        except Exception as e:
            continue
