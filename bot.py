from telebot.types import ReplyKeyboardMarkup
def admin_panel():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    markup.row("📥 Kino yuklash", "📌 Buyurtmalar")
    markup.row("📢 Kanallar", "📊 Statistika")
    markup.row("👨‍💻 Adminlar", "💎 Premium")
    markup.row("💰 Balans", "📨 Xabar yuborish")
    markup.row("💵 Daromad", "📣 Reklamalar")
    markup.row("👥 Referallar", "⚙️ Birlamchi")

    return markup
    @bot.message_handler(commands=['admin'])
def admin(message):
    if message.chat.id == ADMIN_ID:
        bot.send_message(message.chat.id, "🛠 Admin panel:", reply_markup=admin_panel())
      @bot.message_handler(func=lambda message: True)
def handle(message):    if message.chat.id == ADMIN_ID:

        if message.text == "📥 Kino yuklash":
            bot.send_message(message.chat.id, "Kino yuklash boshlandi 🎬")

        elif message.text == "📊 Statistika":
            bot.send_message(message.chat.id, "Statistika 📊")

        elif message.text == "📨 Xabar yuborish":
            bot.send_message(message.chat.id, "Xabar yozing:")
            bot.register_next_step_handler(message, send_all)
            def send_all(message):
    users = cursor.execute("SELECT id FROM users").fetchall()

    for user in users:
        try:
            bot.send_message(user[0], message.text)
        except:
            pass

    bot.send_message(message.chat.id, "Yuborildi ✅")