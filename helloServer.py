from concurrent import futures
import time
from grpc_reflection.v1alpha import reflection # pip install grpcio-reflection
import grpc

import hello_pb2
import hello_pb2_grpc

class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(request.name)
        return hello_pb2.HelloReply(message=f'Hello, {request.name}!, {request.num}!, {request.has_boolean}!')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    SERVICE_NAMES = (
        hello_pb2.DESCRIPTOR.services_by_name['Greeter'].full_name,
        reflection.SERVICE_NAME,
    )
    print(SERVICE_NAMES)
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port('localhost:50051')
    server.start()
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
    