
from telethon import TelegramClient



   
    

api_id = "your_id"
api_hash = 'api_hash'
phone_number = 'phone_number'

client = TelegramClient('session_name', api_id, api_hash)
# Start the client and add the event handler for new messages
from telethon.tl.functions.messages import GetDialogsRequest
from tqdm import tqdm
import os  
from telethon.tl.functions.channels import GetFullChannelRequest

from telethon.tl.functions.messages import AddChatUserRequest 
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.types import InputPeerUser
#from telethon.errors import PrivacyError, UserPrivacyRestrictedError
from telethon.errors import UserPrivacyRestrictedError, UserAlreadyParticipantError, RPCError
from telethon.tl.types import ChannelParticipantsSearch
import time
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import InputPeerChannel
import json



   
async def agrsivtrue1add(client,user_id, group_id):
        
        print("1")
        try:
          await client(AddChatUserRequest( group_id, user_id, fwd_limit=10  ))
        except UserPrivacyRestrictedError:
         print(f"Failed to add user due to privacy restrictions.")
        except UserAlreadyParticipantError:
         print(f"User  already a member of the ")
        except RPCError as e:
           print(f"An RPC error occurred: {e}")
        except Exception as e:
           print("LLL!" )
async def main():
    
 
        group_id="4204649918"
        await client.start(phone_number)
        file_path = "user.json"
        aad = {}
        with open(file_path, "r") as file:
           f1 = json.load(file)
       
        for slss,keyy in f1.items() :
        
           input_user = InputPeerUser(user_id=int(slss), access_hash=int(keyy))
           await agrsivtrue1add(client,input_user,group_id )
           time.sleep(3) 
          
           
       
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
print("tel1")

