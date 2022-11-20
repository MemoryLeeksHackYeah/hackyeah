import requests

class RemoteHub:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_hub_data(ip):
        res = requests.get('http://' + ip).json()
        return res
