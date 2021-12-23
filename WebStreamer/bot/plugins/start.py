# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]



from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command(['start', 'help']))
async def start(_, m: Message):
    await m.reply(f'•Hello {m.from_user.mention(style="md")},
 I can upload your files to direct download link send your file to upload!

• سلام {m.from_user.mention(style="md")}
من میتوانم فایل های شما را به لینک دانلود مستقیم تبدیل کنم فایل خود را ارسال کنید!',
                  reply_markup=InlineKeyboardMarkup(
                      [[
                            InlineKeyboardButton(
                                  f'{emoji.STAR} Source {emoji.STAR}',
                                  url='https://telegram.me/m_mahdihajizadeh')
                        ]]
                  ))
