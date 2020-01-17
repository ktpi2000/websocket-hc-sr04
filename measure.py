from websocket_server import WebsocketServer

def new_client(client, server):
    server.send_message_to_all("Otaku Kosen")

server = WebsocketServer(3000, host="192.168.0.9")
server.set_fn_new_client(new_client)
server.run_forever()
