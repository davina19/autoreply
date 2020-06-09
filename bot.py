import time

from telethon import TelegramClient, events

api_id = api_id
api_hash = 'api_hash'

phone = '+62nomor hp'
session_file = 'nama sesi'
password = 'password, kalo gak ada kosongin aja'

message = "isi pesan | 𝘛𝘩𝘪𝘴 𝘮𝘦𝘴𝘴𝘢𝘨𝘦 𝘸𝘢𝘴 𝘳𝘦𝘱𝘭𝘪𝘦𝘥 𝘣𝘺 𝘈𝘶𝘵𝘰 𝘙𝘦𝘱𝘭𝘺 𝘉𝘰𝘵 𝘣𝘺 𝘷𝘪𝘯𝘤𝘰𝘵𝘪𝘯𝘦."

if __name__ == '__main__': 

    client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)


    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
      if event.is_private:
        from_ = await event.client.get_entity(event.from_id)
        if not from_.bot:
          print(time.asctime(), '-', event.message)
          time.sleep(1)
          await event.respond(message)


    print(time.asctime(), '-', 'Auto-replying...')
    client.start()
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')
