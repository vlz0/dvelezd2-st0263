import requests, json
from Chord import *

class PClientHTTP:
    def __init__(self, server_url):
        self.server_url = server_url
        
    def _make_request(self, method, endpoint, data=None):
        try:
            if method == 'GET':
                response = requests.get(f'{self.server_url}/{endpoint}')
            elif method == 'POST':
                response = requests.post(f'{self.server_url}/{endpoint}', json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error in {method} request to /{endpoint}: {str(e)}")
            return None
    
    def file_list(self):
        return self._make_request('GET', 'files')
    
    def file_upload(self, filename):
        return self._make_request('POST', 'upload', {'filename': filename})
    
    def file_download(self, filename):
        return self._make_request('GET', f'download/{filename}')
    
    def join_network(self):
        with open('config.json') as config_file:
            config = json.load(config_file)
        
        chord_network = CHORD_NETWORK(m=16)
        chord_id = chord_network._hash(f"{config['IP']}:{config['PORT']}")
        chord_node = CHORD_NODE(
            id=chord_id,
            ip=config['IP'],
            port=config['PORT'],
            files=config['FILES'],
            seed_peer_url=config['SEED_PEER_URL'],
            m=16
        )
        
        if config['SEED_PEER_URL']:
            response = requests.post(f"{config['SEED_PEER_URL']}/join", json={'node_ip': config['IP'], 'node_port': config['PORT']})
            response.raise_for_status()
        
        chord_network.join(chord_node)

def main():
    cliente_http = PClientHTTP('http://127.0.0.1:5000')
    cliente_http.join_network()
    
    print("Listing files:")
    print(cliente_http.file_list())
    
    print("\nUploading file 'example.txt':")
    print(cliente_http.file_upload('example.txt'))
    
    print("\nDownloading file 'example.txt':")
    print(cliente_http.file_download('example.txt'))
    
    print("\nListing files again:")
    print(cliente_http.file_list())

if __name__ == '__main__':
    main()