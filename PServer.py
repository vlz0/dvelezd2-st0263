from flask import Flask, jsonify, request
import json, threading
from Chord import CHORD_NODE, CHORD_NETWORK

app = Flask(__name__)

with open('config.json') as config_file:
    config = json.load(config_file)

chord_network = CHORD_NETWORK(m=16)
chord_id = chord_network._hash(f"{config['IP']}:{config['PORT']}")
chord_node = CHORD_NODE(chord_id, config['IP'], config['PORT'], config['FILES'], 16, config['SEED_PEER_URL'])
chord_network.join(chord_node)

@app.route('/files', methods=['GET'])
def list_files():
    return jsonify(chord_node.node_files)

@app.route('/upload', methods=['POST'])
def upload_file():
    filename = request.json['filename']
    target_node = chord_network.find_successor(chord_network._hash(filename))
    target_node.store_file(filename)
    return jsonify({'message': f'File {filename} uploaded to node {target_node.node_id}'}), 200

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    target_node = chord_network.find_successor(chord_network._hash(filename))
    if target_node.has_file(filename):
        return jsonify({'message': f'File {filename} found on node {target_node.node_id}'}), 200
    else:
        return jsonify({'error': 'File not found'}), 404

@app.route('/nodes', methods=['GET'])
def nodes_list():
    nodes_info = [{'NODO ID': node.node_id, 'NODO IP': node.node_ip, 'NODO PORT': node.node_port} for node in chord_network.nodes]
    return jsonify({'NODES': nodes_info, 'ALL FILES': chord_network.get_all_files()}), 200

@app.route('/join', methods=['POST'])
def join():
    data = request.json
    join_ip = data['node_ip']
    join_port = data['node_port']
    join_node_id = chord_network._hash(f"{join_ip}:{join_port}")
    join_node = CHORD_NODE(join_node_id, join_ip, join_port, [], 16)
    chord_network.join(join_node)
    return jsonify({'message': f'Node {join_node_id} added successfully'}), 200

@app.route('/set', methods=['POST'])
def set_node():
    data = request.json
    if 'successor' in data:
        chord_node.set_successor(data['successor'])
    if 'predecessor' in data:
        chord_node.set_predecessor(data['predecessor'])
    return jsonify({'message': 'Node updated successfully'}), 200

@app.route('/set_p', methods=['POST'])
def set_p():
    predecessor_id = request.json['predecessor']
    chord_node.node_predecessor = predecessor_id
    return jsonify({'message': 'Predecessor updated'}), 200

@app.route('/set_s', methods=['POST'])
def set_s():
    successor_id = request.json['successor']
    chord_node.node_successor = successor_id
    return jsonify({'message': 'Successor updated'}), 200

if __name__ == '__main__':
    app.run(host=config['IP'], port=config['PORT'], debug=True)