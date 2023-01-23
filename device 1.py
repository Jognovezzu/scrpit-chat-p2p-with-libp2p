import argparse
from io import StringIO
import sys

import multiaddr
import trio

from libp2p import new_host
from libp2p.network.stream.net_stream_interface import INetStream
from libp2p.peer.peerinfo import info_from_p2p_addr
from libp2p.typing import TProtocol

PROTOCOL_ID = TProtocol("/chat/1.0.0")
MAX_READ_LEN = 2 ** 32 - 1


#Função para ler a msg
async def read_data(stream: INetStream) -> None:
    while True:
        read_bytes = await stream.read(MAX_READ_LEN)
        if read_bytes is not None:
            read_string = read_bytes.decode()
            if read_string != "\n":
                # Green console colour: 	\x1b[32m
                # Reset console colour: 	\x1b[0m
                print("\x1b[32m %s\x1b[0m " % read_string, end="")

#Função para escrever  a msg
async def write_data(stream: INetStream) -> None:
    # trio.trio.wrap_file(sys.stdin) para escrever a msg do console,
    # trocar para trio.wrap_file(StringIO('asdf')) se for para instanciar
    # diretamente.
    async_f = trio.wrap_file(sys.stdin)
    while True:
        line = await async_f.readline()
        await stream.write(line.encode())


async def run(port: int, destination: str):

    localhost_ip = "127.0.0.1"
    host = new_host()
    listen_addr = multiaddr.Multiaddr(f"/ip4/0.0.0.0/tcp/{port}")

    async with host.run(listen_addrs=[listen_addr]), trio.open_nursery() as nursery:

        if destination is None or "": #CASO NÃO TENHA DESTINATARIO
            async def stream_handler(stream: INetStream) -> None:
                nursery.start_soon(read_data, stream)
                nursery.start_soon(write_data, stream)

            
            host.set_stream_handler(PROTOCOL_ID, stream_handler)

            print(
                f"copy and paste the link to send message: "
                f"/ip4/{localhost_ip}/tcp/{port}/p2p/{host.get_id().pretty()} "
            )
            print("Waiting for incoming connection...")

        
        else: #CASO HAJA O DESTINO 
            maddr = multiaddr.Multiaddr(destination)
            info = info_from_p2p_addr(maddr)
            await host.connect(info)
            stream = await host.new_stream(info.peer_id, [PROTOCOL_ID])
            nursery.start_soon(read_data, stream)
            nursery.start_soon(write_data, stream)
            print(f"Connected to peer {info.addrs[0]}")
        
        await trio.sleep_forever()



def main() -> None:
    # Criando instância de host para o dispositivo

    localhost_ip = "127.0.0.1"
    print("port:")
    port = int(input())




    host = new_host()
    print("Destination:")
    destination = input()
    if destination =="":
        destination = None

    trio.run(run,*(port, destination))



if __name__ == "__main__":
    main()