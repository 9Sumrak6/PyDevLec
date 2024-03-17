#!/usr/bin/env python3
import asyncio
import cowsay


clients = {}

free_cows = set(cowsay.list_cows())
taken_cows = set()

async def chat(reader, writer):
    global free_cows, taken_cows, clients

    nick = ''

    me = "{}:{}".format(*writer.get_extra_info('peername'))
    print(me)

    clients[me] = asyncio.Queue()
    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(clients[me].get())

    while not reader.at_eof():
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)

        for q in done:
            if q is send:
                print(q.result().decode().strip())
                send = asyncio.create_task(reader.readline())
            elif q is receive:
                receive = asyncio.create_task(clients[me].get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()
    send.cancel()
    receive.cancel()
    print(me, "DONE")
    del clients[me]
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())