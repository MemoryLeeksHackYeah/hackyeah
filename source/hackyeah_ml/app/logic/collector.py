from app.models import RemoteHub
from app.logic.remote_hub import RemoteHub as RemoteHubLogic
from app.logic.simulator import Simulator

class Collector:
    def __init__(self, company_id):
        self.company_id = company_id
        self.remote_hubs = RemoteHub.objects.filter(disposal_service_company_ID=self.company_id)
        self.remote_hubs_data = {}
        self.update_remote_hubs_data()
        
    def update_remote_hubs_data(self):
        for remote_hub in self.remote_hubs:
            self.remote_hubs_data[remote_hub.id] = RemoteHubLogic.get_hub_data(remote_hub.ip_address)
            for data in Simulator.generate():
                self.remote_hubs_data[data['id']] = data
            
    def __str__(self):
        ret = '{\n'
        for k, v in self.remote_hubs_data.items():
            ret += f'\t{k}: {v},'
        return ret + '\n}'
        