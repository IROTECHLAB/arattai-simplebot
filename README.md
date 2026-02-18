# 🤖 Arattai Bot - Reverse Engineered Chat Bot

[![Warning](https://img.shields.io/badge/⚠️-REVERSE_ENGINEERED-red)](https://github.com/IROTECHLAB)
[![License](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.6+-blue)](https://python.org)
[![Zoho](https://img.shields.io/badge/Zoho-Arattai-orange)](https://www.zoho.com/arattai/)
[![Contributors](https://img.shields.io/badge/Contributors-Welcome-brightgreen)](https://github.com/IROTECHLAB/arattai-bot/blob/main/CONTRIBUTORS.md)

**Created by [IROTECHLAB](https://github.com/IROTECHLAB)**

---

## ⚠️ IMPORTANT DISCLAIMER

`THIS BOT IS REVERSE ENGINEERED SOFTWARE - FOR EDUCATIONAL PURPOSES ONLY`

**🔴 WARNING:**
- Arattai is a product of **ZOHO CORPORATION**
- Using this bot MAY result in **PERMANENT ACCOUNT BAN**
- We are **NOT RESPONSIBLE** for any misuse or bans
- **DO NOT** use for spamming, harassment, or bulk messaging
- Respect Arattai/Zoho's Terms of Service
- **USE AT YOUR OWN RISK**

---

## 📱 What is Arattai Bot?

A Python bot that responds to commands in Arattai chat (Zoho's social platform). It reads messages with prefix "." and replies automatically.

**Search terms:** Arattai bot, Zoho Arattai bot, Arattai automation, Arattai chat bot, Arattai API, reverse engineered Arattai, Arattai Python bot, IROTECHLAB Arattai, Arattai chat ID finder

---

## 👥 Contributors

**We Welcome Contributors!**

Want to contribute? Check our [CONTRIBUTORS.md](https://github.com/IROTECHLAB/arattai-simplebot/blob/main/CONTRIBUTORS.md) file.

---

## ✨ Features

- ✅ Command-based responses (`.menu`, `.alive`, `.time`, `.ping`)
- ✅ Rate limiting to avoid detection
- ✅ Self-message detection
- ✅ Cookie authentication (no password)
- ✅ Console logging when messages received
- ✅ Silent fail (no error spam, only shows when working)
- ✅ Works 24/7 on PC/Server/VPS
- ✅ Android compatible (with Reqable)

---

## 📋 Requirements

- Python 3.6+
- requests library
- Arattai account (by Zoho)
- Android phone OR PC
- Reqable app (for cookie & chat ID extraction)

---

## 🚀 Quick Installation

```bash
# Clone from IROTECHLAB
git clone https://github.com/IROTECHLAB/arattai-simplebot
cd arattai-simplebot

# Install requirements
pip install requests

# Run the bot
python bot.py
```

---

## 🔑 TWO THINGS YOU NEED

Before running the bot, you need to get two things using Reqable:

1. **🍪 COOKIES** - For authentication (12 cookies)
2. **💬 CHAT ID** - Which chat the bot should monitor (starts with CT_)

---

## 📱 Reqable Guide

**Your Reqable app will show:**

```text
┌─────────────────────────────────────┐
│  Request & Respond...                │
├─────────────────────────────────────┤
│ Headers(37)  Body  Cookies(12) POST │
├─────────────────────────────────────┤
│ Urlencode  Raw  Hex                  │
│                                      │
│ chid    CT_12875210191...            │ ← YOUR CHAT ID HERE
│ msg     test                          │
│ msgid   1771397291254                 │
│ sid     NENQ1Q6MzU5N...               │
│ dname   BAJRANG                       │
│ unfurl  false                         │
│                                      │
│ ↑ Request          ↓ Response        │
└─────────────────────────────────────┘
```

---

## 🍪 PART 1: Getting Cookies

### Step 1: Install Reqable
- Download **Reqable** from Play Store
- Open app → Install SSL certificate (follow guide)

### Step 2: Capture Traffic
- Open Reqable → Add App → Select your browser
- Turn ON Reqable (allow VPN)
- Open browser → Go to **web.arattai.in**
- LOGIN to your Zoho/Arattai account
- Open any chat (Pocket/Saved Messages)
- Send a message (type "test")

### Step 3: Find the Request
- Go back to Reqable
- Look for **sendofficechatmessage.do** request
- Tap on it to open details

### Step 4: Copy Cookies
- At the top, tap on **Cookies(12)** tab
- You'll see all 12 cookies:
  - zalb_cf22541252
  - __Secure-iamsdt
  - _iamadt
  - _iambdt
  - CT_CSRF_TOKEN
  - x-tkp-token
  - e2ee_registration_id
  - e2ee_device_id
  - JSESSIONID
  - com_avcliq_owner
  - com_chat_owner
  - com_arattai_owner
- Tap copy icon or long press → Copy all

### Step 5: Generate cookies.txt
- Visit: **[IROTECHLAB Cookie Converter](https://irotech-cookie-converter.netlify.app/)**
- Paste cookies → Click Generate
- Download **cookies.txt**
- Place in bot folder

---

## 💬 PART 2: Finding Your Chat ID

### Step 1: Go to Body Tab
- In the same **sendofficechatmessage.do** request
- Tap on **Body** tab (next to Headers/Cookies)

### Step 2: Look for chid parameter
- Scroll down in the Body section
- Find **chid=**
- The value after = is your CHAT ID

**Example:**
```text
chid = CT_1287521019107750094_20004081014-GC
       ↑                                  ↑
            THIS IS YOUR CHAT ID
```

### Step 3: Copy the full CHAT ID
- Copy everything after `chid=`
- It starts with **CT_** and is very long

### Step 4: Update in bot script
Open **bot.py** and find this line:

```python
self.CHAT_ID = "CT_1287521019107750094_20004081014-GC"
```

Replace it with YOUR chat ID:

```python
self.CHAT_ID = "CT_YOUR_CHAT_ID_HERE"
```

---

## 🎯 For Different Chats

Want the bot to work in a different chat?

1. Open that specific chat in your browser
2. Send any message in that chat
3. Go to Reqable
4. Find the new **sendofficechatmessage.do** request
5. Check Body tab → copy the **chid** value
6. Update it in the bot script

---

## 🚀 Running the Bot

Once you have both:
- ✅ **cookies.txt** in bot folder
- ✅ **CHAT_ID** updated in script

```bash
python bot.py
```

**Expected output:**
```text
============================================================
🤖 ArattaiBot - COOKIE FILE VERSION
============================================================
📱 Chat: CT_1287521019107750094_20004081014-GC
👤 Your ID: 20004081014
🤖 Bot signature: 🤖
✅ Loaded 12 cookies from cookies.txt
============================================================

🟢 Bot is running! Send commands with prefix '.'

📨 1 new message(s):

👤 John: .menu
   🔍 Processing command: .menu
   ✅ Bot: **Menu**...

👤 John: Hello
   (no command - ignored)
```

**Note:** Bot only shows output when messages are received. No news is good news!

---

## 🎮 Available Commands

| Command | Description |
|---------|-------------|
| `.menu` | Show all commands |
| `.alive` | Check bot uptime |
| `.time` | Current time |
| `.ping` | Test response |

---

## ⚠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| No cookies loaded | Repeat cookie steps carefully |
| Bot not responding | Cookies expired - get fresh ones |
| Wrong chat responding | Check CHAT_ID in script |
| 401 Unauthorized | Cookies expired - refresh |
| Rate limited | Bot handles this automatically |
| Can't find chid | Look in Body tab, not Headers |
| Nothing in console | Bot is working fine! It only shows when messages arrive |

---

## 🤝 How to Contribute

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

**After your PR is merged, your name will be added to CONTRIBUTORS.md!**

---

## 📄 MIT License with Terms

```MIT License

Copyright (c) 2026 IROTECHLAB

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

ADDITIONAL TERMS:
1. This is REVERSE ENGINEERED software of Zoho's Arattai - EDUCATIONAL USE ONLY
2. Users assume ALL RISK of account suspension/ban from Zoho/Arattai
3. Developers (IROTECHLAB) and CONTRIBUTORS are NOT LIABLE for any misuse or damages
4. NO commercial use without permission
5. NO spamming, harassment, or bulk messaging
6. Users MUST comply with Zoho Corporation's Terms of Service

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
```

---

## 🔒 Legal Notice

Arattai is a product of **ZOHO CORPORATION**. This bot is NOT affiliated with, authorized by, or endorsed by Zoho Corporation or Arattai. All trademarks belong to their respective owners. References to Arattai/Zoho are for identification purposes only.

By using this bot, you agree to take full responsibility for your Zoho/Arattai account.

---

## 📊 SEO & Search Keywords

`Arattai bot, Zoho Arattai bot, Arattai automation, Arattai Python bot, Arattai reverse engineered, Arattai API bot, Arattai chat bot, Arattai auto responder, Arattai self bot, Arattai command bot, how to make Arattai bot, Arattai bot tutorial, Arattai bot GitHub, Arattai bot Python, Arattai bot Android, Arattai cookie extractor, Arattai Reqable guide, Zoho social platform, Arattai messaging bot, IROTECHLAB Arattai, Arattai unofficial bot, Arattai chat ID finder, how to get Arattai chat ID, Arattai chid parameter, Reqable Arattai tutorial, Arattai sendofficechatmessage, Arattai bot 2026, Arattai Python script, Arattai open source`

---

## 📱 Connect with IROTECHLAB

- **Instagram** [Instagram](https://www.instagram.com/Ironmanyt00/)
- **GitHub:** [github.com/IROTECHLAB](https://github.com/IROTECHLAB)
- **Repository:** [github.com/IROTECHLAB/arattai-bot](https://github.com/IROTECHLAB/arattai-simplebot)
- **Issues:** [Report bugs here](https://github.com/IROTECHLAB/arattai-simplebot/issues)
- **Contributions:** [Pull Requests welcome](https://github.com/IROTECHLAB/arattai-simplebot/pulls)
- **Contributors List:** [CONTRIBUTORS.md](https://github.com/IROTECHLAB/arattai-simplebot/blob/main/CONTRIBUTORS.md)

---

## ⭐ Support the Project

- Star the repository on GitHub
- Share with friends (who accept the risks)
- Contribute code or documentation
- Report bugs you find

<div align="center">

**⚠️ USE AT YOUR OWN RISK - NOT OFFICIAL ZOHO PRODUCT ⚠️**

**© 2026 IROTECHLAB** • [GitHub](https://github.com/IROTECHLAB) • [Contributors Welcome](https://github.com/IROTECHLAB/arattai-simplebot/blob/main/CONTRIBUTORS.md)
</div>
