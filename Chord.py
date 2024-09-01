import hashlib
import requests
import threading

class CHORD_NODE:
    def __init__(self, id, ip, port, files, m, seed_peer_url=None):
        self.node_id = id
        self.node_ip = ip
        self.node_port = port
        self.node_files = files
        self.m = m
        self.node_seed_peer_url = seed_peer_url
        self.node_successor = None
        self.node_predecessor = None
    
    def _get_url(self, ip, port, path):
        return f"http://{ip}:{port}/{path}"
    
    def store_file(self, filename):
        self.node_files.append(filename)
    
    def has_file(self, filename):
        return filename in self.node_files
    
    def update_successor_and_predecessor(self):
        if self.node_successor:
            try:
                response = requests.post(self._get_url(self.node_successor.node_ip, self.node_successor.node_port, 'set_p'),
                                        json={'predecessor': self.node_id})
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Error updating successor: {e}")
        
        if self.node_predecessor:
            try:
                response = requests.post(self._get_url(self.node_predecessor.node_ip, self.node_predecessor.node_port, 'set_s'),
                                        json={'successor': self.node_id})
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Error updating predecessor: {e}")
    
    def set_successor(self, successor):
        self.node_successor = successor
        self.update_successor_and_predecessor()
    
    def set_predecessor(self, predecessor):
        self.node_predecessor = predecessor
        self.update_successor_and_predecessor()

class CHORD_NETWORK:
    def __init__(self, m):
        self.m = m
        self.nodes = []
    
    def _hash(self, key):
        return int(hashlib.sha1(key.encode()).hexdigest(), 16) % (2 ** self.m)
    
    def join(self, new_node):
        if not self.nodes:
            self.nodes.append(new_node)
            new_node.node_successor = new_node
            new_node.node_predecessor = new_node
        else:
            self.nodes.append(new_node)
            self.nodes.sort(key=lambda node: node.node_id)
            new_node.node_successor = self.find_successor(new_node.node_id)
            new_node.node_predecessor = self.nodes[(self.nodes.index(new_node) - 1) % len(self.nodes)]
            
            new_node.update_successor_and_predecessor()
    
    def find_successor(self, id):
        for node in self.nodes:
            if node.node_id >= id:
                return node
        return self.nodes[0]
        
    def get_all_files(self):
        files_full = []
        for node in self.nodes:
            try:
                response = requests.get(f"http://{node.node_ip}:{node.node_port}/files")
                response.raise_for_status()
                node_files = response.json()
                files_full.append({'FILESS': node_files, 'NODEE': node.node_id})
            except requests.RequestException as e:
                print(f"Error fetching files from node {node.node_id}: {str(e)}")
        return files_full