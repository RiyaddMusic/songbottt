from config import API_ID, API_HASH, BOT_TOKEN, BOT_NAME
from pyrogram import Client, filters, idle
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

Medusa = Client(
    session_name=BOT_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root='plugins')
)


PMTEXT = ('👋 Salam\n⚡ Mən 🎧 _ 𝐒 𝐎 𝐍 𝐆 _ 𝐁 𝐎 𝐓 Musiqi Yükləmə Botuyam\n🎧 Mənim Vasdəm İlə İsdənilən Musiqini Yükləmək Mümkündür\n📚 Əmrlərlə Tanış Olmaq Üçün ƏMRLƏR Butonuna Toxun')
PMKEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                '📚 ƏMRLIR', callback_data='help_callback'),
            InlineKeyboardButton('ℹ MƏLUMAT', callback_data='about')
        ],
        [
            InlineKeyboardButton(
                '➕《 MƏNİ QRUPA DƏVƏT ET 》 ➕', url='http://t.me/ZionSongbot?startgroup=true')  # Replace the `MedusaMousikibot` with your bot username
        ]
    ]
)
HELPTEXT = ('📚 ƏMRLƏR MENUSU\n🔹️ Aşağdakı Əmrləri İzləyin\n⚡ **ƏMRLƏR*/n• /song - Musiqi Adı Yada YouTube  Linki\n• /lyrics - İsdənilən Musiqinin Sözlərin Yükləyər\n• /info - YouTube dən Musiqi Məlumatı Alın')

ABOUTTEXT = (
    "**Name** : Zionusic🎵\n**Username** : ZionMusicbot\n**Description**"
    " : <a href='https://en.wikipedia.org/wiki/Medusa'>**Medusa**</a> is a Greek"
    " mythology.\n__Generally described as winged human females with living"
    " venomous snakes in place of hair. Those who gazed into her eyes would"
    " turn to stone.\nThe word '**Mousiki**' is the Greek word for"
    " '**Music**'.__\n**Version** : 2.3.1\n**Special Credits:**\n\t•Credit of"
    " lyrics: __genius.com__\n\nProject by Bibee"
)


@Medusa.on_message(
    filters.command(['start', 'help'], ['/', '!'])
    & (filters.private | filters.group)
    & ~ filters.edited
)
async def start_cmd(_, msg: Message):
    ''' Response for /start command (private or groupe) '''

    if msg.chat.type == 'private':
        await msg.reply_sticker(sticker='CAACAgIAAx0CXeethQACBIthRB3WPePSpGljt548kGW3uJ0s3gACkAUAAtJaiAGaVzjS0OoLfh4E')
        await msg.reply(
            text=PMTEXT,
            reply_markup=PMKEYBOARD,
            disable_web_page_preview=True
        )
    else:
        await msg.reply(
            text='Hey! I am Online. PM me if you have any question on how to use me.',
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text='Start me in PM :)',
                            # Replace the `MedusaMousikibot` with your bot username
                            url=f't.me/MedusaMousikibot?start=help'
                        )
                    ]
                ]
            )
        )


@Medusa.on_callback_query()
async def callback_handling(_, query: CallbackQuery):
    ''' Response for Callback queries '''

    q_data = query.data
    q_id = query.id

    if q_data == 'menu_1':
        await Medusa.answer_callback_query(q_id, 'Main Menu!')
        await query.message.edit(
            text=PMTEXT,
            reply_markup=PMKEYBOARD,
            disable_web_page_preview=True
        )

    elif q_data == 'help_callback':
        await Medusa.answer_callback_query(q_id, 'Help Menu!')
        await query.message.edit(text=HELPTEXT,
                                 parse_mode='md',
                                 reply_markup=InlineKeyboardMarkup(
                                     [
                                         [
                                             InlineKeyboardButton(
                                                 text="Back",
                                                 callback_data='menu_1',
                                             )
                                         ]
                                     ]
                                 ),
                                 )

    elif q_data == 'about':
        await Medusa.answer_callback_query(q_id, text='About Menu!')
        await query.message.edit(
            text=ABOUTTEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            'Back', callback_data='menu_1')
                    ]
                ]
            )
        )




Medusa.start()
print('Medusa is starting....')
idle()
print('Medusa is aborting...')
Medusa.stop()
