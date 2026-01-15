from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8302155323:AAEiIh4ADCIkl5XwCCj69RKvQzlQovpq2oY"

# --- MENU PRINCIPAL ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📥 Déposer", callback_data="deposit")],
        [InlineKeyboardButton("💼 Mon compte", callback_data="account")],
        [InlineKeyboardButton("💸 Retirer", callback_data="withdraw")],
        [InlineKeyboardButton("📖 Comment ça marche", callback_data="howitworks")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "💼 Bienvenue sur SolGrow !\n\n"
        "Choisis une action ci-dessous 👇",
        reply_markup=reply_markup
    )

# --- GESTION DES BOUTONS ---
async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # valide le clic pour Telegram

    if query.data == "deposit":
        keyboard = [[InlineKeyboardButton("⬅️ Retour au menu", callback_data="menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(
            "📥 Déposer des SOL\n\n"
            "Envoie tes SOL sur ton adresse unique (simulation).\n"
            "Dépôt minimum : 2 SOL",
            reply_markup=reply_markup
        )

    elif query.data == "account":
        keyboard = [[InlineKeyboardButton("⬅️ Retour au menu", callback_data="menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(
            "💼 Mon compte (simulation)\n\n"
            "SOL déposés : 5.0\n"
            "USDT générés : 12.3\n"
            "USDT disponibles : 7.5\n"
            "Dernier retrait : Aucun",
            reply_markup=reply_markup
        )

    elif query.data == "withdraw":
        keyboard = [[InlineKeyboardButton("⬅️ Retour au menu", callback_data="menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(
            "💸 Retrait USDT\n\n"
            "⚠️ Solde minimum pour retrait : 30 USDT\n"
            "Clique sur le bouton pour simuler le retrait (test).",
            reply_markup=reply_markup
        )

    elif query.data == "howitworks":
        keyboard = [[InlineKeyboardButton("⬅️ Retour au menu", callback_data="menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(
            "📖 Comment ça marche\n\n"
            "1️⃣ Dépose tes SOL\n"
            "2️⃣ Ton solde USDT croît chaque jour (simulation)\n"
            "3️⃣ Tu peux retirer tes USDT quand tu veux\n"
            "4️⃣ Toutes les transactions seront visibles on-chain",
            reply_markup=reply_markup
        )

    elif query.data == "menu":
        # renvoyer le menu principal
        await start(update, context)

# --- CRÉATION DU BOT ---
app = ApplicationBuilder().token(TOKEN).build()

# --- HANDLERS ---
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(menu_handler))

# --- LANCEMENT DU BOT ---
print("Bot démarré...")
app.run_polling()
