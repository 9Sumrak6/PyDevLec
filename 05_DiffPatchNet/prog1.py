#!/usr/bin/env python3
import asyncio
import cowsay


clients = {}

free_cows = set(cowsay.list_cows())
taken_cows = set()

async def chat(reader, writer):
    global free_cows, taken_cows, clients

    me = "{}:{}".format(*writer.get_extra_info('peername'))

    while query := await reader.readline():
        query = query.decode().split()
        if len(query) == 0:
            continue
        if query[0] == 'login':
            if len(query) == 1:
                writer.write(f"Enter the nickname\n".encode())
                continue

            if query[1] in free_cows:
                me = query[1]
                writer.write(f"You have registered under a nickname: {query[1]}\n".encode())

                clients[me] = asyncio.Queue()

                taken_cows.add(query[1])
                free_cows = free_cows - taken_cows

                break
            elif query[1] in taken_cows:
                writer.write("This cow is alreday taken.\n".encode())
            else:
                writer.write("Incorrect cow\n".encode())
                continue
        elif query[0] == 'who':
            writer.write(f'Taken cows: {taken_cows}\n'.encode())
        elif query[0] == 'cows':
            writer.write(f'Free cows: {free_cows}\n'.encode())
        elif query[0] == 'quit':
            writer.close()
            return
        else:
            writer.write("You did not log in or the command is incorrect.\n".encode())

        await writer.drain()


async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())