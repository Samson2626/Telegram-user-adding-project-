
from telethon import TelegramClient
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
import asyncio
from telethon.tl.types import InputPeerUser
from telethon.tl.types import InputPeerChannel
import time
from telethon.errors import ChatAdminRequiredError, RPCError
import json
api_id = "your_id"
api_hash = 'api_hash'
phone_number = 'phone_number'


client = TelegramClient('session_name', api_id, api_hash)

# Dictionary to be written to the file
async def ajson(a):
  file_path = "avgp.json"
  with open(file_path, "w") as file:
    # Convert the dictionary to a JSON string and write it to the file
    json.dump(a, file)


async def main():
    # Create the client and connect/
    client = TelegramClient('session_name', api_id, api_hash)
    
    await client.start(phone_number)
  #  await agrsivtrue(client)
    print("true")
    # Get the group entity
    file_path = "avgp.json"
    aad = {}
    with open(file_path, "r") as file:
      f1 = json.load(file)
    for slss,keyy in f1.items() :
     
     gp= InputPeerChannel(channel_id=int(slss) , access_hash=int(keyy))
     group = await client.get_entity(gp)
    
    # Get all participants
     offset =0
     limit = 100
     all_participants =[]
    
    
     while True:
          try:
                    participants = await client(GetParticipantsRequest(
                        group,
                        ChannelParticipantsSearch(''),
                        offset,
                        limit,
                        hash=0
                    ))
          except Exception as e:
                    print(f"dave111: {e}")
                    time.sleep(5)  # Wait before retrying to avoid rate limits
                    break
          if not participants.users:
            offset =0
            break
        
          all_participants.extend(participants.users)
          
          offset += len(participants.users)
          print(offset)
          
     for user in all_participants:
            print(f"ID: {user.id}, Access Hash: {user.access_hash}")
            aad[user.id]=user.access_hash
    print(len(aad))
    await ajson(aad)
    # Print member IDs and access hashes
    #  for user in all_participants:
    #      print(f"ID: {user.id}, Access Hash: {user.access_hash}")
         
       

    await client.disconnect()

asyncio.run(main())

