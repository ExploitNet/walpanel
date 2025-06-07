import os
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.oprations import admin
from app.version import __version__


class _MessageSetings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), "..", "..", ".env"),
        case_sensitive=True,
        extra="ignore",
    )

    START_MAIN_ADMIN: dict = {
        "en": (
            "Welcome!\n"
            "━━━━━━━━━━━━━━━━━\n"
            f"🛡️ version: {__version__}\n"
            "👨‍💻 devlop by: @primez_dev\n"
            "🏢 Sponsor: @Magic_Mizban"
        ),
        "fa": (
            "خوش آمدید!\n"
            "━━━━━━━━━━━━━━━━━\n"
            f"🛡️ version: {__version__}\n"
            "👨‍💻 devlop by: @primez_dev\n"
            "🏢 Sponsor: @Magic_Mizban"
        ),
    }
    START_DEALER: dict = {
        "en": ("👋 Hi, you can use the buttons"),
        "fa": ("👋 درود، میتونی از دکمه های زیر استفادی کنی"),
    }
    START_MESSAGE: dict = {
        "en": ("👋 Welcome, if you want to use this bot you need to register"),
        "fa": ("👋 خوش آمدید، اگر می‌خواهید از سرویس ما استفاده کنید باید ثبت نام کنید"),
    }

    DEALERS_STATUS: dict = {
        "en": (
            "<pre>👤 Username: {username}</pre>\n"
            "⌛ Days remaining: {days_remaining} D\n"
            "📊 Traffic: {traffic} GB\n"
            "💻 Panel in use: {panel}\n"
            "ℹ️ Status: {status}\n"
            "➖➖➖➖➖➖➖➖➖➖\n"
        ),
        "fa": (
            "<pre>👤 نام کاربری: {username}</pre>\n"
            "⌛ روزهای باقی‌مانده: {days_remaining} روز\n"
            "📊 ترافیک: {traffic} گیگابایت\n"
            "💻 پنل درحال استفاده: {panel}\n"
            "ℹ️ وضعیت: {status}\n"
            "➖➖➖➖➖➖➖➖➖➖\n"
        ),
    }
    PANELS_STATUS: dict = {
        "en": (
            "<pre>🌐 Panel name: {name}</pre>\n"
            "⚙️ <b>CPU Usage:</b> {cpu_usage}%\n"
            "💾 <b>Memory Usage:</b> {ram_usage}%\n"
            "🛡️ <b>Xray Status:</b> {xray_status}\n"
            "📝 <b>Xray Version:</b> {xray_version}\n"
            "⏱️ <b>Uptime:</b> {uptime} hours\n"
            "➖➖➖➖➖➖➖➖➖➖\n"
        ),
        "fa": (
            "<pre>🌐 نام پنل: {name}</pre>\n"
            "⚙️ <b>استفاده پردازنده:</b> %{cpu_usage}\n"
            "💾 <b>استفاده رم:</b> %{ram_usage}\n"
            "🛡️ <b>وضعیت ایکسری:</b> {xray_status}\n"
            "📝 <b>نسخه ایکسری:</b> {xray_version}\n"
            "⏱️ <b>مدت روشن بودن:</b> {uptime} ساعت\n"
            "➖➖➖➖➖➖➖➖➖➖\n"
        ),
    }
    LOG_MESSAGE: dict = {
        "en": ("📝 Last 10 log entries:"),
        "fa": ("📝 10 لاگ اخر:"),
    }
    BACKING_UP: dict = {
        "en": ("Backing up database..."),
        "fa": ("پشتیبان گیری از دیتابیس..."),
    }
    HELP_TEXT: dict = {
        "en": (
            "<b>📄 Current help text:</b>\n\n"
            "- {help_text}"
            "━━━━━━━━━━━━━━━━━\n"
            "Please send the new help text:"
        ),
        "fa": (
            "<b>📄 متن راهنمای فعلی:</b>\n\n"
            "- {help_text}\n"
            "━━━━━━━━━━━━━━━━━\n"
            "لطفا متن راهنمای جدید رو بفرستید:"
        ),
    }
    CANCEL_OPERATION: dict = {
        "en": ("🔸 Operation canceled."),
        "fa": ("🔸 عملیات لغو شد."),
    }
    HELP_TEXT_CHANGED: dict = {
        "en": ("✅ Help text changed successfully."),
        "fa": ("✅ متن راهنمای تغییر کرد."),
    }
    ERROR: dict = {
        "en": ("Error: {e}"),
        "fa": ("خطا: {e}"),
    }
    REGISTRATION_TEXT: dict = {
        "en": (
            "<b>⚪ Current registration text:</b>\n\n"
            "- {registration_text}\n"
            "━━━━━━━━━━━━━━━━━\n"
            "Please send the new registration text:"
        ),
        "fa": (
            "<b>⚪ متن ثبت‌نام فعلی:</b>\n\n"
            "- {registration_text}\n"
            "━━━━━━━━━━━━━━━━━\n"
            "لطفا متن ثبت‌نام جدید را بفرستید:"
        ),
    }
    REGISTRATION_TEXT_CHANGED: dict = {
        "en": ("✅ Registration text changed successfully."),
        "fa": ("✅ متن ثبت‌نام تغییر کرد."),
    }
    NOTIF_STATUS: dict = {
        "en": (
            "<b>📳 Current notification status:</b>\n\n"
            "- Start the bot = {start_status}\n"
            "- Create a new client = {create_status}\n"
            "- Delete a client = {delete_status}\n"
        ),
        "fa": (
            "<b>📳 وضعیت اعلان های فعلی:</b>\n\n"
            "- استارت ربات = {start_status}\n"
            "- ساخت یک کاربر توسط نماینده = {create_status}\n"
            "- حذف یک کاربر توسط نماینده = {delete_status}\n"
        ),
    }
    START_NOTIF: dict = {
        "en": (
            "<b>📳 Oh, someone starred the bot:</b>\n\n"
            "<b>👤 Full name:</b> {name}\n"
            "<b>🆔 Username:</b> @{user_id}\n"
            "<b>🪪 Chat ID:</b> {chat_id}\n"
            "<a href='tg://openmessage?user_id={chat_id}'>💬<b> Open chat</b></a>"
        ),
        "fa": (
            "<b>📳 اوه، ربات استارت شد توسط:</b>\n\n"
            "<b>👤 نـام:</b> {name}\n"
            "<b>🆔 نام کاربری:</b> @{user_id}\n"
            "<b>🪪 چت ایدی:</b> {chat_id}\n"
            "<a href='tg://openmessage?user_id={chat_id}'>💬<b> بازکردن چـــت </b></a>"
        ),
    }
    PLAN_IS_NOT_EXIST: dict = {
        "en": ("⚠️ Plan not found!"),
        "fa": ("⚠️ پلن یافت نشد!"),
    }
    SHOW_PLANS: dict = {
        "en": (
            "🆔 ID: {id}\n"
            "📊 Traffic: {traffic} G\n"
            "⌛ Deadline: {deadline} days\n"
            "💸 Price: {price} $\n"
            "━━━━━━━━━━━━━━━━━\n"
        ),
        "fa": (
            "🆔 ایدی پلن: {id}\n"
            "📊 ترافیک: {traffic} گیگ\n"
            "⌛ تاریخ انقضا: {deadline} روز\n"
            "💸 قیمت: {price} تومان\n"
            "━━━━━━━━━━━━━━━━━\n"
        ),
    }
    WAITING_FOR_PLAN_TRAFFIC: dict = {
        "en": ("1- plase enter a traffic(GB) for this plan:"),
        "fa": ("1- لطفا ترافیک(گیگ) برای این پلن را وارد کنید:"),
    }
    WAITING_FOR_PLAN_DEADLINE: dict = {
        "en": ("2- plase enter a deadline(days) for this plan:"),
        "fa": ("2- لطفا تاریخ انقضا(روز) برای این پلن را وارد کنید:"),
    }
    WAITING_FOR_PLAN_PRICE: dict = {
        "en": ("3- plase enter a price($) for this plan:"),
        "fa": ("3- لطفا قیمت(تومان) برای این پلن را وارد کنید:"),
    }
    WAITING_FOR_PLAN_ID: dict = {
        "en": ("0- plase enter a plan id:"),
        "fa": ("0- لطفا ایدی پلن را وارد کنید:"),
    }
    PLAN_NOT_EXIST: dict = {
        "en": ("⚠️ Plan not found!"),
        "fa": ("⚠️ پلن یافت نشد!"),
    }
    PLAN_ADDED: dict = {
        "en": ("✅ Plan added successfully!\n"),
        "fa": ("✅ پلن با موفقیت اضافه شد!\n"),
    }
    INVALID_VALUE: dict = {
        "en": ("⚠️ Invalid value!"),
        "fa": ("⚠️ ورودی نا معتبر است!"),
    }
    PLAN_UPDATED: dict = {
        "en": ("✅ Plan updated successfully!\n"),
        "fa": ("✅ پلن با موفقیت بروز رسانی شد!\n"),
    }
    CONFIRM_PLAN_DELETE: dict = {
        "en": ("⚠️ Are you sure you want to delete this plan?"),
        "fa": ("⚠️ از حذف این پلن اطمینان دارید؟"),
    }
    PLAN_DELETED: dict = {
        "en": ("✅ Plan deleted successfully!\n"),
        "fa": ("✅ پلن با موفقیت حذف شد!\n"),
    }
    WAITING_FOR_CONFIRM_SIGNUP_ADMIN: dict = {
        "en": (
            "ℹ️ Your registration request has been sent to the administrator Please wait..."
        ),
        "fa": ("ℹ️ درخواست شما برای مدیر ارسال شد لطفا صبر کنید..."),
    }
    YOUR_REGISTERITION_REQUEST_REJECTED: dict = {
        "en": ("⚠️ Your request has been rejected."),
        "fa": ("⚠️ درخواست شما رد شد."),
    }
    A_NEW_SIGNUP_REQUEST: dict = {
        "en": (
            "📳 New registration request by:\n\n"
            "👤 Full name: {name}\n"
            "<b>🆔 Username:</b> @{user_id}\n"
            "<b>🪪 Chat ID:</b> {chat_id}\n"
            "<a href='tg://openmessage?user_id={chat_id}'>💬<b> Open chat</b></a>"
        ),
        "fa": (
            "📳 درخواست ایجاد حساب جدید از:\n\n"
            "<b>👤 نـام:</b> {name}\n"
            "<b>🆔 نام کاربری:</b> @{user_id}\n"
            "<b>🪪 چت ایدی:</b> {chat_id}\n"
            "<a href='tg://openmessage?user_id={chat_id}'>💬<b> بازکردن چـــت </b></a>"
        ),
    }
    WAITING_FOR_CONFIRM_SIGNUP_SUCCESS: dict = {
        "en": ("✅ Your request has been accepted\nYour plan has been added"),
        "fa": ("✅ درخواست شما پذیرش شد\nپلن شما با موفقیت اضافه شد"),
    }
    REJECT_REGISTERATION_RULES: dict = {
        "en": (
            "⚠️ Rejection of registration rules by:\n\n"
            "👤 Full name: {name}\n"
            "<b>🆔 Username:</b> @{user_id}\n"
            "<b>🪪 Chat ID:</b> {chat_id}\n"
            "<a href='tg://openmessage?user_id={chat_id}'>💬<b> Open chat</b></a>"
        ),
        "fa": (
            "📳 یک رد قوانین ثبت نام جدید توسط:\n\n"
            "<b>👤 نـام:</b> {name}\n"
            "<b>🆔 نام کاربری:</b> @{user_id}\n"
            "<b>🪪 چت ایدی:</b> {chat_id}\n"
            "<a href='tg://openmessage?user_id={chat_id}'>💬<b> بازکردن چـــت </b></a>"
        ),
    }
    CHOOSE_A_USERNAME_FOR_THE_REQUESTER: dict = {
        "en": ("1- Registration request approved. Please enter a Username:"),
        "fa": ("1- درخواست ثبت‌نام تایید شد. لطفاً یک یوزرنیم وارد کنید:"),
    }
    CHOOSE_A_PASSWORD_FOR_THE_REQUESTER: dict = {
        "en": ("2- Please enter a Password:"),
        "fa": ("2- لطفا یک پسورد وارد کنید:"),
    }
    CHOOSE_A_PANEL_FOR_THE_REQUESTER: dict = {
        "en": ("3- Please enter a panel 🆔 for this dealer:"),
        "fa": ("3- لطفا یک پنل 🆔 برای این نماینده وارد کنید:"),
    }
    PANEL_NOT_EXIST: dict = {
        "en": ("⚠️ Panel not found!"),
        "fa": ("⚠️ پنل یافت نشد!"),
    }
    CHOOSE_A_INBOUND_FOR_THE_REQUESTER: dict = {
        "en": ("4- Please enter a inbound id for this dealer:"),
        "fa": ("4- لطفا یک اینباند ایدی برای این نماینده وارد کنید:"),
    }
    REGISTERITION_REQUEST_APPROVED: dict = {
        "en": (
            "✅ Registration request approved and panel access sent to dealer/admin"
        ),
        "fa": ("✅ درخواست ثبت نام تایید شد و دسترسی پنل به نماینده ارسال شد"),
    }
    YOUR_REGISTERITION_REQUEST_HAS_BEEN_CONFIRMED: dict = {
        "en": (
            "<b>🎉 Your registration has been confirmed.</b>\n\n"
            "Username: {username}\n"
            "Password: {password}\n"
        ),
        "fa": (
            "<b>🎉 درخواست ثبت نام شما تایید شد.</b>\n\n"
            "یوزرنیم: {username}\n"
            "پسورد: {password}\n"
        ),
    }
    LOGIN_STEP1: dict = {
        "en": ("1- Please enter your username:"),
        "fa": ("1- لطفا یوزرنیم خودتون رو وارد کنید:"),
    }
    LOGIN_STEP2: dict = {
        "en": ("2- Please enter your password:"),
        "fa": ("2- لطفا پسورد خودتون رو وارد کنید:"),
    }
    LOGIN_STEP3: dict = {
        "en": ("3- Please solve this captcha:\n{question} = ?"),
        "fa": ("3- لطفا این کپچا رو حل کنید:\n{question} = ?"),
    }
    CAPTCHA_WRONG: dict = {
        "en": ("❌ Wrong answer! Please try again:"),
        "fa": ("❌ پاسخ اشتباه! لطفا دوباره تلاش کنید:"),
    }
    LOGIN_SUCCESS: dict = {
        "en": ("✅ Login successful! Welcome back."),
        "fa": ("✅ ورود موفقیت آمیز! خوش آمدید."),
    }
    LOGIN_FAILED: dict = {
        "en": ("❌ Login failed! Invalid username or password."),
        "fa": ("❌ ورود ناموفق! نام کاربری یا رمز عبور اشتباه است."),
    }
    MY_ACCOUNT: dict = {
        "en": (
            "👤 Username: {username}\n"
            "🔐 Password: {password}\n"
            "📊 Traffic: {traffic}\n"
            "⌛ Expiry time: {expiry_time}D"
        ),
        "fa": (
            ".\n"
            "👤 نام کاربری: {username}\n"
            "🔐 رمزعبور: {password}\n"
            "📊 ترافیک: {traffic} گیگ\n"
            "⌛ انقضا: {expiry_time}روز"
        ),
    }
    SHOW_PLANS_FOR_DEALER: dict = {
        "en": ("🛍️ Available  plans:"),
        "fa": ("🛍️ پلن های موجود برای شارژ اشتراک شما:"),
    }
    SELECTED_PLAN: dict = {
        "en": (
            "<b> Selected plan:</b>\n\n"
            "📊 Traffic: {traffic} GB\n"
            "⌛ Expiry time: {expiry_time}D\n"
            "💸 Price: {price} $"
        ),
        "fa": (
            "<b>پلن انتخابی شما برای خرید:</b>\n\n"
            "📊 ترافیک: {traffic} گیگ\n"
            "⌛ تاریخ انقضا: {expiry_time}روز\n"
            "💸 قیمت: {price} تومان"
        ),
    }

    CANCEL: dict = {"en": "❌ Cancel", "fa": "❌ انصراف"}

    SEND_PAYMENT_METHODS: dict = {
        "en": "Please click the confirm button to proceed with card payment.",
        "fa": "لطفا برای ادامه خرید یکی از روش های موجود را انتخاب کنید.",
    }
    PRE_PAY_WITH_GATEWAY: dict = {
        "en": (
            "💳 Payment via ExToPay\n\n"
            "📊 Order Details:\n"
            "💰 Amount: {price} Toman|$\n"
            "⚠️ Note:\n"
            "• Your transaction will be automatically confirmed after payment\n"
            "• If not automatically confirmed, please contact support\n\n"
            "Click the button below to pay 👇"
        ),
        "fa": (
            "💳 پرداخت از طریق درگاه ExToPay\n\n"
            "📊 جزئیات سفارش:\n"
            "💰 مبلغ: {price} تومان\n"
            "⚠️ توجه:\n"
            "• پس از پرداخت، تراکنش شما به صورت خودکار تایید خواهد شد\n"
            "• در صورت عدم تایید خودکار، لطفا با پشتیبانی تماس بگیرید\n\n"
            "برای پرداخت روی دکمه زیر کلیک کنید 👇"
        ),
    }

    PAYMENT_SUCCESS: dict = {
        "en": (
            "✅ Payment Successful\n\n"
            "📊 Order Details:\n\n"
            "🆔 Oeder ID: <code>{order_id}</code>\n"
            "🎉 Your traffic and subscription time have been successfully added"
        ),
        "fa": (
            "✅ پرداخت با موفقیت انجام شد\n\n"
            "📊 جزئیات سفارش:\n\n"
            "🆔 کد پیگیری: <code>{order_id}</code>\n"
            "🎉 ترافیک و زمان اشتراک شما با موفقیت اضافه شد"
        ),
    }

    GEATWAY_ERROR: dict = {
        "en": ("Gateway payment failed. Please try again later."),
        "fa": ("پرداخت از طریق درگاه ناموفق بود. لطفا بعدا دوباره تلاش کنید."),
    }
    PAYMENT_FAILED: dict = {
        "en": (
            "❌ Payment Failed\n\n"
            "🆔 Tracking code:\n<code>{order_id}</code>\n"
            "⚠️ If the amount was deducted from your account, it will be refunded within 24 hours"
        ),
        "fa": (
            "❌ پرداخت ناموفق\n\n"
            "🆔 کد پیگیری:\n<code>{order_id}</code>\n"
            "⚠️ در صورت کسر وجه از حساب شما، طی 24 ساعت آینده به حساب شما بازگردانده خواهد شد"
        ),
    }
    ADMIN_PAYMENT_SUCCESS_NOTIF: dict = {
        "en": (
            "🟢 New Successful Payment!\n\n"
            "📊 Payment Details:\n"
            "💰 Plan price: {amount} Toman|$\n"
            "🆔 Plan id: {plan_id}\n"
            "🆔 Order ID:\n<code>{order_id}</code>\n"
            "🆔 Chat id: {chat_id}\n"
            "🕒 Timestamp: {timestamp}\n"
        ),
        "fa": (
            "🟢 پرداخت موفق جدید!\n\n"
            "📊 جزئیات پرداخت:\n"
            "💰 قیمت پلن: {amount} تومان\n"
            "🆔 ایدی پلن: {plan_id}\n"
            "🆔 ایدی سفارش:\n<code>{order_id}</code>\n"
            "🆔 چت ایدی نماینده: {chat_id}\n"
            "🕒 زمان: {timestamp}\n"
        ),
    }

    ADMIN_PAYMENT_FAILED_NOTIF: dict = {
        "en": (
            "🔴 New Failed Payment!\n\n"
            "📊 Payment Details:\n"
            "💰 Plan price: {amount} Toman|$\n"
            "🆔 Plan id: {plan_id}\n"
            "🆔 Order ID:\n<code>{order_id}</code>\n"
            "🆔 Chat id: {chat_id}\n"
            "🕒 Timestamp: {timestamp}\n"
        ),
        "fa": (
            "🔴 پرداخت ناموفق جدید!\n\n"
            "📊 جزئیات پرداخت:\n"
            "💰 قیمت پلن: {amount} تومان\n"
            "🆔 ایدی پلن: {plan_id}\n"
            "🆔 ایدی سفارش:\n<code>{order_id}</code>\n"
            "🆔 چت ایدی نماینده: {chat_id}\n"
            "🕒 تاریخ: {timestamp}\n"
        ),
    }

    SEND_CARD_PAYMENT_PHOTO: dict = {
        "en": "ℹ️ Please send a photo of your card payment receipt\n\n💸Amount: {price}\n💳Card number: {card_num}",
        "fa": "ℹ️ لطفا عکس رسید پرداخت کارت به کارت را ارسال کنید\n\n💸مبلغ: {price}\n💳شماره کارت: {card_num}",
    }

    PAYMENT_SENT_FOR_APPROVAL: dict = {
        "en": "Your payment has been sent for approval. We will notify you once it's approved.",
        "fa": "پرداخت شما برای تایید ارسال شد. پس از تایید به شما اطلاع داده خواهد شد.",
    }

    PAYMENT_CONFIRMATION_REQUEST: dict = {
        "en": (
            "📳 Payment confirmation request\n\n"
            "👤 From: {username}\n"
            "📊 Traffic: {traffic} GB\n"
            "⌛ Days: {days}\n"
            "💸 Price: {price} $"
        ),
        "fa": (
            "📳 درخواست تایید پرداخت\n\n"
            "👤 از: {username}\n"
            "📊 ترافیک: {traffic} گیگابایت\n"
            "⌛ انقضا: {days} روز\n"
            "💸 قیمت: {price} تومان"
        ),
    }

    APPROVE_PAYMENT: dict = {"en": "✅ Approve", "fa": "✅ تایید"}

    REJECT_PAYMENT: dict = {"en": "❌ Reject", "fa": "❌ رد"}

    PAYMENT_APPROVED: dict = {
        "en": "✅ Your payment has been approved! Your plan has been activated.",
        "fa": "✅ پرداخت شما تایید شد! پلن شما فعال شد.",
    }

    PAYMENT_REJECTED: dict = {
        "en": "❌ Your payment has been rejected. Please contact support if you believe this is a mistake.",
        "fa": "❌ پرداخت شما رد شد. اگر فکر می‌کنید اشتباهی رخ داده، لطفا با پشتیبانی تماس بگیرید.",
    }

    PAYMENT_APPROVED_BY_ADMIN: dict = {
        "en": "✅ Payment approved by admin",
        "fa": "✅ پرداخت توسط ادمین تایید شد",
    }

    PAYMENT_REJECTED_BY_ADMIN: dict = {
        "en": "❌ Payment rejected by admin",
        "fa": "❌ پرداخت توسط ادمین رد شد",
    }

    PAYMENT_CANCELLED: dict = {
        "en": "Payment process has been cancelled!",
        "fa": "فرآیند پرداخت لغو شد!",
    }

    PAYMENT_DISABLED: dict = {
        "en": "Card payment is currently disabled. Please try again later.",
        "fa": "پرداخت در حال حاضر غیرفعال است. لطفا بعداً تلاش کنید.",
    }
    LOGOUT: dict = {
        "en": "You have been logged out of your panel‼️",
        "fa": "شما از پنل خود خارج شدید‼️",
    }

    CARD_METHOD_SETTINGS: dict = {
        "en": (
            "💳 <b>Card Payment Settings</b>\n\n"
            "🔄 Status: {status}\n"
            "💳 Card Number: {card_num}\n"
        ),
        "fa": (
            "💳 <b>تنظیمات پرداخت کارت به کارت</b>\n\n"
            "ℹ️ وضعیت: {status}\n"
            "💳 شماره کارت: {card_num}\n"
        ),
    }

    INTERMEDIARY_METHOD_SETTINGS: dict = {
        "en": (
            "⛓️‍💥 <b>Intermediary Payment Settings</b>\n\n"
            "🔄 Status: {status}\n"
            "🔑 API Key: {api_key}\n"
        ),
        "fa": (
            "⛓️‍💥 <b>تنظیمات درگاه پرداخت واسط</b>\n\n"
            "ℹ️ وضعیت: {status}\n"
            "🔑 کلید: {api_key}\n"
        ),
    }

    CHANGE_CARD_METHOD_STATUS: dict = {"en": "🔄 Change Status", "fa": "🔄 تغییر وضعیت"}

    CHANGE_CARD_NUMBER: dict = {
        "en": "💳 Change Card Number",
        "fa": "💳 تغییر شماره کارت",
    }

    CHANGE_INTERMEDIARY_METHOD_STATUS: dict = {
        "en": "🔄 Change Status",
        "fa": "🔄 تغییر وضعیت",
    }

    CHANGE_INTERMEDIARY_METHOD_API_KEY: dict = {
        "en": "🔑 Change API Key",
        "fa": "🔑 تغییر API Key",
    }
    HELP_INTERMEDIARY_METHOD: dict = {
        "en": ("ℹ️ Tihs only available for Iranians."),
        "fa": (
            "ℹ️ برای استفاده از این درگاه واسطه، شما نیازه به کلید اختصاصی خودتون دارید، برای دریافت کلید و اطلاعات بیشتر میتونید به پشتیبانی این درگاه پیام بدید:\n"
            "<b>@wetoma</b>\n\n"
        ),
    }
    ENTER_NEW_CARD_NUMBER: dict = {
        "en": "Please enter the new card number:",
        "fa": "لطفا شماره کارت جدید را وارد کنید:",
    }
    ENTER_NEW_API_KEY: dict = {
        "en": "Please enter the new API key:",
        "fa": "لطفا API key جدید را وارد کنید:",
    }

    CARD_NUMBER_UPDATED: dict = {
        "en": "✅ Card number has been updated successfully!",
        "fa": "✅ شماره کارت با موفقیت بروزرسانی شد!",
    }

    APIKEY_UPDATED: dict = {
        "en": "✅ API key has been updated successfully!",
        "fa": "✅ با موفقیت بروزرسانی شد!",
    }

    DATABASE_MENU: dict = {"en": "Database menu...", "fa": "منوی دیتابیس..."}

    WAITING_FOR_BACKUP_FILE: dict = {
        "en": "Please send your database backup file to restore the database.",
        "fa": "لطفا فایل پشتیبان دیتابیس خود را برای بازگردانی بفرستید.",
    }

    NO_FILE: dict = {
        "en": "⚠️ No file was sent. Please send a database backup file.",
        "fa": "⚠️ هیچ فایلی ارسال نشد. لطفا یک فایل پشتیبان دیتابیس ارسال کنید.",
    }

    INVALID_FILE: dict = {
        "en": "⚠️ Invalid file format. Please send a .db file.",
        "fa": "⚠️ فرمت فایل نامعتبر است. لطفا یک فایل .db ارسال کنید.",
    }

    RESTORING: dict = {
        "en": "🔄 Restoring database from backup...",
        "fa": "🔄 در حال بازگرداندن دیتابیس از پشتیبان...",
    }

    RESTORE_SUCCESS: dict = {
        "en": "✅ Database has been successfully restored from backup!",
        "fa": "✅ دیتابیس با موفقیت از پشتیبان بازگردانده شد!",
    }

    # Button texts
    BUTTON_ADMINS: dict = {"en": "👤 Admins", "fa": "👤 ادمین‌ها"}
    BUTTON_PANELS: dict = {"en": "🌐 Panels", "fa": "🌐 پنل‌ها"}
    BUTTON_SETTINGS: dict = {"en": "⚙️ Settings", "fa": "⚙️ تنظیمات"}
    BUTTON_LOGS: dict = {"en": "📝 Logs", "fa": "📝 لاگ‌ها"}
    BUTTON_SALES_PLAN: dict = {"en": "🛍️ Sales Plan", "fa": "🛍️ پلن فروش"}
    BUTTON_NOTIFICATIONS: dict = {"en": "🔔 Notifications", "fa": "🔔 اعلان‌ها"}
    BUTTON_HELP_TEXT: dict = {"en": "📄 Help text", "fa": "📄 متن راهنما"}
    BUTTON_REGISTRATION_TEXT: dict = {
        "en": "⚪ Registration text",
        "fa": "⚪ متن ثبت‌نام",
    }
    BUTTON_DATABASE: dict = {"en": "📦 Database", "fa": "📦 دیتابیس"}
    BUTTON_LANGUAGE: dict = {"en": "🌎 Language", "fa": "🌎 زبان"}
    BUTTON_BACK: dict = {"en": "🔙 Back", "fa": "🔙 بازگشت"}
    BUTTON_BACK_TO_SETTINGS: dict = {
        "en": "🔙 Back to settings",
        "fa": "🔙 بازگشت به تنظیمات",
    }
    BUTTON_BACKUP: dict = {"en": "📥 Backup", "fa": "📥 پشتیبان‌گیری"}
    BUTTON_RESTORE: dict = {"en": "📤 Restore", "fa": "📤 بازگردانی"}
    BUTTON_ADD_PLAN: dict = {"en": "➕ Add a plan", "fa": "➕ افزودن پلن"}
    BUTTON_DELETE_PLAN: dict = {"en": "❌ Delete a plan", "fa": "❌ حذف پلن"}
    BUTTON_EDIT_PLAN: dict = {"en": "⚙️ Edit a plan", "fa": "⚙️ ویرایش پلن"}
    BUTTON_CARD_METHOD: dict = {"en": "💳 Card method setting", "fa": "💳 تنظیمات کارت"}
    BUTTON_INTERMEDIARY_METHOD: dict = {
        "en": "⛓️ ExToPay method setting",
        "fa": "⛓️ تنظیمات درگاه ExToPay",
    }
    BUTTON_INTERMEDIARY_METHOD_HELP: dict = {
        "en": "📗 ExToPay help",
        "fa": "📗 راهنمای ExToPay",
    }
    BUTTON_ENGLISH: dict = {"en": "🇺🇸 English", "fa": "🇺🇸 انگلیسی"}
    BUTTON_PERSIAN: dict = {"en": "🇮🇷 Persian", "fa": "🇮🇷 فارسی"}
    BUTTON_CANCEL: dict = {"en": "❌ Cancel", "fa": "❌ انصراف"}
    BUTTON_SIGN_UP: dict = {"en": "💎 sign up", "fa": "💎 ثبت‌نام"}
    BUTTON_LOGIN: dict = {"en": "🛡️ Login", "fa": "🛡️ ورود"}
    BUTTON_HELP: dict = {"en": "ℹ️ Help", "fa": "ℹ️ راهنما"}
    BUTTON_MY_ACCOUNT: dict = {"en": "💎 My account", "fa": "💎 حساب من"}
    BUTTON_STORE: dict = {"en": "🛍️ Store", "fa": "🛍️ فروشگاه"}
    BUTTON_LOGOUT: dict = {"en": "❌ Logout", "fa": "❌ خروج"}
    BUTTON_OPEN_PANEL: dict = {"en": "🛜 Open panel", "fa": "🛜 باز کردن پنل"}
    BUTTON_ACCEPT: dict = {"en": "✅ Accept", "fa": "✅ پذیرش"}
    BUTTON_DECLINE: dict = {"en": "❌ Decline", "fa": "❌ رد"}
    BUTTON_YES: dict = {"en": "✅ Yes", "fa": "✅ بله"}
    BUTTON_NO: dict = {"en": "❌ No", "fa": "❌ خیر"}
    BUTTON_CONFIRM: dict = {"en": "✅ Confirm", "fa": "✅ تایید"}
    BUTTON_REJECT: dict = {"en": "❌ Reject", "fa": "❌ رد"}
    PAYMENT_WITH_CARD: dict = {"en": "💳 Card Payment", "fa": "💳 کارت به کارت"}
    PAYMENT_WITH_INTERMEDIARY: dict = {
        "en": "🔗 ExToPay Payment",
        "fa": "🔗 درگاه پرداخت ExToPay",
    }
    BUTTON_PAY: dict = {
        "en": "💳 Pay",
        "fa": "💳 پرداخت",
    }


BOT_MESSAGE = _MessageSetings()
