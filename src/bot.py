import random
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Ваш токен
TOKEN = "8600717212:AAERLmxF7Ir94KrYB1ss6BAAyYnNh2_FXmM"

# Включаем логирование для отладки
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Список случайных фактов
FACTS = [
    "🐘 Слоны — единственные млекопитающие, которые не умеют прыгать.",
    "🍕 Самая большая пицца в мире была приготовлена в Риме в 2012 году, её площадь — 1261 квадратный метр.",
    "💤 Улитки могут спать до трёх лет подряд.",
    "🐪 Верблюды могут выпить до 200 литров воды за 3 минуты.",
    "🦄 У единорогов нет реального прототипа в природе, но они есть в мифологии многих культур.",
    "🌊 Океаны покрывают 71% поверхности Земли, но мы исследовали только 5% из них.",
    "📖 Библиотека Конгресса США — крупнейшая библиотека в мире, в ней более 170 миллионов единиц хранения.",
    "🍎 Яблоки помогают проснуться лучше, чем кофе, из-за природного сахара.",
    "🐬 Дельфины дают друг другу имена в виде уникальных свистов.",
    "🔥 Венера — самая горячая планета Солнечной системы (до 460°C), хотя Меркурий ближе к Солнцу.",
    "😸 Кошки спят примерно 70% своей жизни.",
    "🍌 Банан — это ягода, а не фрукт.",
    "🕷 Пауки не насекомые, а паукообразные.",
    "📝 Знак @ называется 'коммерческое эт' или 'собачка'.",
    "🎨 Мона Лиза не имеет бровей — такова была мода эпохи Возрождения."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    await update.message.reply_text(
        "🤖 *Привет! Я бот со случайными фактами!*\n\n"
        "📋 *Доступные команды:*\n"
        "/start — приветствие\n"
        "/help — список команд\n"
        "/fact — получить случайный факт\n"
        "/about — информация о боте\n"
        "/count — сколько всего фактов в базе\n\n"
        "Просто напиши /fact и получи порцию знаний! 🧠",
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /help"""
    await update.message.reply_text(
        "📋 *Список команд:*\n\n"
        "/start — приветственное сообщение\n"
        "/help — эта справка\n"
        "/fact — случайный интересный факт\n"
        "/about — информация о создателе и проекте\n"
        "/count — количество фактов в базе данных\n\n"
        "✨ *Совет:* используй /fact несколько раз, чтобы узнать много нового!",
        parse_mode="Markdown"
    )

async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправляет случайный факт"""
    random_fact = random.choice(FACTS)
    await update.message.reply_text(f"🧠 *Вот твой случайный факт:*\n\n{random_fact}", parse_mode="Markdown")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Информация о боте и проекте"""
    await update.message.reply_text(
        "🤖 *О боте:*\n\n"
        "Этот бот создан в рамках проектной практики.\n"
        "📅 Год: 2026\n"
        "🎓 Учебное заведение: Проектная практика\n\n"
        "*Технологии:*\n"
        "• Python 3\n"
        "• python-telegram-bot библиотека\n"
        "• Telegram Bot API\n\n"
        "*Функции:*\n"
        "• Отправка случайных фактов\n"
        "• Простота использования\n\n"
        "📂 *Исходный код:* размещён на GitHub\n"
        "👨‍💻 *Автор:* Студент 1 курса",
        parse_mode="Markdown"
    )

async def count(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показывает количество фактов в базе"""
    await update.message.reply_text(f"📚 В моей базе данных *{len(FACTS)}* интересных фактов! Используй /fact, чтобы их узнать.", parse_mode="Markdown")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ответ на любое текстовое сообщение (кроме команд)"""
    await update.message.reply_text(
        "❓ *Неизвестная команда*\n\n"
        "Напиши /help, чтобы увидеть список всех доступных команд.\n"
        "Или просто нажми /fact для случайного факта! ✨",
        parse_mode="Markdown"
    )

async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка неизвестных команд (начинающихся с / но не зарегистрированных)"""
    await update.message.reply_text(
        "❓ Извини, я не знаю такой команды.\n"
        "Напиши /help, чтобы узнать, что я умею."
    )

def main():
    """Главная функция запуска бота"""
    print("=" * 50)
    print("🚀 ЗАПУСК ТЕЛЕГРАМ-БОТА")
    print("=" * 50)
    print(f"📡 Подключение к Telegram API...")
    print(f"🤖 Бот запускается с токеном: {TOKEN[:15]}...")
    
    # Создаём приложение
    app = Application.builder().token(TOKEN).build()
    
    # Регистрируем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("fact", fact))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("count", count))
    
    # На любое текстовое сообщение (не команду) отвечаем подсказкой
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # На любую неизвестную команду (например /чтототам)
    app.add_handler(MessageHandler(filters.COMMAND, unknown_command))
    
    print("✅ Бот успешно настроен!")
    print("💬 Теперь бот работает и ждёт сообщений")
    print("📱 Проверь в Telegram: отправь /start твоему боту")
    print("⏹ Для остановки бота нажми Ctrl+C")
    print("=" * 50)
    
    # Запускаем бота
    app.run_polling()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + "=" * 50)
        print("🛑 Бот остановлен пользователем")
        print("=" * 50)
    except Exception as e:
        print("=" * 50)
        print(f"❌ ПРОИЗОШЛА ОШИБКА: {e}")
        print("=" * 50)
        raise