import requests

class DeveloperAPI:
    def __init__(self):
        """
        This function contains the link to the API website
        args: self.url (str)
        """
        self.url= f'https://backend-omega-seven.vercel.app/api/getjoke'
    def get(self):
        """
        This function requests the response from the API website, converts it into a json dictionary, and returns it as a string
        args: self.url (str)
        return: response (str)
        """
        r=requests.get(self.url)
        response=r.json()
        return str(response)