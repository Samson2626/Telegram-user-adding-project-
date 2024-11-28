
from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest 
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.types import InputPeerUser

from telethon.tl.types import ChannelParticipantsSearch
import time
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import InputPeerChannel
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
async def additreblegroup(gp):
    group = await client.get_entity(gp)
    
    # Get all participants
    offset =0
    limit = 15
    all_participants = []
    x1=0
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
                   
                    x1=1
                    return x1
                    break
          if not participants.users:
            break
          
          all_participants.extend(participants.users)
          
          offset += len(participants.users)
          print(offset)
          return x1
          break

async def main():
    

        
     
        a1={}
        dialogs = await client.get_dialogs()
        for dialog in dialogs:
         cp=0
         if dialog.is_group or dialog.is_channel:
            entity = dialog.entity
            
            if hasattr(entity, 'access_hash'):
                
                gp= InputPeerChannel(channel_id= entity.id, access_hash=entity.access_hash)
                cp=1
            else:
                gp=entity.id
            ad1=await additreblegroup(gp)
            if ad1 == 0:
                if cp==1:
                    print(f"Name: {entity.title}, ID: {entity.id}, Access Hash: {entity.access_hash}")
                    a1[entity.id]=entity.access_hash
                else:
                    a1[entity.id]=90
                    print(f"Name: {entity.title}, ID: {entity.id}, Access Hash: {entity.title}")
            
                    
                
            # Print user ID and access hash
        await ajson(a1)  
    
       
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())


