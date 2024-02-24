import grpc
import message_pb2
import message_pb2_grpc
from openai import GPT, Example

class Gpt4Service(message_pb2_grpc.Gpt4ServiceServicer):
    def __init__(self):
        self.gpt = GPT(engine="davinci")

    def GenerateResponse(self, request, context):
        input_text = request.input_text
        response_text = self.gpt.submit_request(input_text).choices[0].text.strip()
        return message_pb2.Response(output_text=response_text)

def serve():
    server = grpc.server(grpc.insecure_server())
    message_pb2_grpc.add_Gpt4ServiceServicer_to_server(Gpt4Service(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
