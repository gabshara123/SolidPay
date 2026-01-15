from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8302155323:AAEiIh4ADCIkl5XwCCj69RKvQzlQovpq2oY"

# Commandes du bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💼 Bienvenue sur SolGrow !\n\n"
        "Dépose tes SOL, regarde ton rendement USDT croître chaque jour et retire facilement quand tu veux.\n"
        "Toutes les transactions sont on-chain et vérifiables.\n\n"
        "📌 Dépôt minimum : 2 SOL\n"
        "📌 Retrait minimum : 30 USDT"
    )

async def deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📥 Déposer des SOL\n\n"
        "Envoie tes SOL sur ton adresse unique (simulation pour le moment).\n"
        "Dépôt minimum : 2 SOL"
    )

async def account(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💼 Mon compte (simulation)\n\n"
        "SOL déposés : 5.0\n"
        "USDT générés : 12.3\n"
        "USDT disponibles : 7.5\n"
        "Dernier retrait : Aucun"
    )

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💸 Retrait USDT\n\n"
        "⚠️ Solde minimum pour retrait : 30 USDT\n"
        "Clique sur le bouton pour simuler le retrait (test)."
    )

async def howitworks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 Comment ça marche\n\n"
        "1️⃣ Dépose tes SOL\n"
        "2️⃣ Ton solde USDT croît chaque jour (simulation)\n"
        "3️⃣ Tu peux retirer tes USDT quand tu veux\n"
        "4️⃣ Toutes les transactions seront visibles on-chain"
    )

# Création du bot
app = ApplicationBuilder().token(TOKEN).build()

# Ajout des handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("deposit", deposit))
app.add_handler(CommandHandler("account", account))
app.add_handler(CommandHandler("withdraw", withdraw))
app.add_handler(CommandHandler("howitworks", howitworks))

print("Bot démarré...")
app.run_polling()
