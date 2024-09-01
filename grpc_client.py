import grpc, chord_pb2, chord_pb2_grpc, json

class PClientGRPC:
    def __init__(self, server_url):
        grpc_port = 50052
        self.grpc_channel = grpc.insecure_channel(f'{server_url}:{grpc_port}')
        self.grpc_stub = chord_pb2_grpc.ChordServiceStub(self.grpc_channel)

    def send_hello(self):
        request = chord_pb2.HelloRequest(message="Hello from gRPC client")
        response = self.grpc_stub.SendHello(request)
        print("gRPC Hello Response:", response.reply)

    def add_numbers(self, num1, num2):
        request = chord_pb2.AddRequest(number1=num1, number2=num2)
        response = self.grpc_stub.AddNumbers(request)
        print(f"gRPC Add Numbers Response: {num1} + {num2} = {response.result}")

def main():
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    server_url = config.get("GRPC_PEER_URL", "localhost")
    client = PClientGRPC(server_url)
    client.send_hello()
    client.add_numbers(10, 20)

if __name__ == '__main__':
    main()