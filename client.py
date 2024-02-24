import grpc
import message_pb2
import message_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = message_pb2_grpc.Gpt4ServiceStub(channel)
    input_text = "What's the meaning of life?"
    response = stub.GenerateResponse(message_pb2.Request(input_text=input_text))
    print("GPT-4 response:", response.output_text)

if __name__ == '__main__':
    run()
