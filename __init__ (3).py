from aiohttp import web
from .route import routes
import os
import io
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
# Define the new hug command handler
@Client.on_message(filters.command('help'))
async def hug_command_handler(client, message):
    try:
        # Get the absolute path to the image file on your VPS
        file_path = '/home/admin/vegabeta/images/aocpro.jpg'
        
        # Check if the file exists
        if os.path.exists(file_path):
            # Load the image file in binary mode
            with open(file_path, 'rb') as image_file:
                image_data = image_file.read()
                
                # Create buttons with links
                google_button = InlineKeyboardButton(text='✦ᴏᴜʀ ɴᴇᴛᴡᴏʀᴋ✦', url='https://telegram.me/Anime_Ocean_Network')
                donate_button = InlineKeyboardButton(text='✦ᴘʀᴏᴍᴏ ᴡɪᴛʜ ᴜs✦', url='https://telegram.me/CuriousToFault')
                
                # Create an inline keyboard and add the buttons
                keyboard = InlineKeyboardMarkup([[google_button], [donate_button]])
                
                # Create an in-memory binary stream and load the image data
                stream = io.BytesIO(image_data)
                
                # Send the image file and the buttons to the user as a reply
                await client.send_photo(chat_id=message.chat.id, photo=stream, reply_markup=keyboard)
        
        else:
            # Raise an exception if the file does not exist
            raise FileNotFoundError(f"File not found at {file_path}")
    
    except Exception as e:
        print("Exception occurred: ", e)
__all__ = ["web_server"]
