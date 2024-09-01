from concurrent import futures
import grpc, chord_pb2, chord_pb2_grpc

class ChordService(chord_pb2_grpc.ChordServiceServicer):
    def SendHello(self, request, context):
        return chord_pb2.HelloReply(reply=f'Hello, {request.message}!')

    def AddNumbers(self, request, context):
        result = request.number1 + request.number2
        return chord_pb2.AddReply(result=result)

def serve_grpc():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chord_pb2_grpc.add_ChordServiceServicer_to_server(ChordService(), server)
    
    grpc_port = 50052
    server.add_insecure_port(f'[::]:{grpc_port}')
    server.start()
    print(f'gRPC server running on port {grpc_port}')
    server.wait_for_termination()

if __name__ == '__main__':
    serve_grpc()