import random

latlon_limits = {
    'lat': {
        'min': 49.996529,
        'max': 50.105795
    },
    'lon': {
        'min': 19.843499,
        'max': 20.044056
    }
}

class Simulator:
    @staticmethod
    def generate():
        response = []
        hubs_count = random.randint(10, 50)
        total_scales = 2
        
        for hub_id in range(1, hubs_count):
            scales_count = random.randint(2, 5)
            response_part = {
                'id': hub_id,
                'lat': random.random() * (latlon_limits['lat']['max'] - latlon_limits['lat']['min']) + latlon_limits['lat']['min'],
                'long': random.random() * (latlon_limits['lon']['max'] - latlon_limits['lon']['min']) + latlon_limits['lon']['min'],
                'weights': []
            }
            waste_types = random.sample(['mix', 'plastic', 'bio', 'paper', 'glass'], k=scales_count)
            for scale_id in range(scales_count):
                response_part['weights'].append({
                    'id': total_scales + scale_id,
                    'weight': random.random() * 1500,
                    'type': waste_types[scale_id]
                })
            response.append(response_part)
            total_scales += scales_count
        return response
        