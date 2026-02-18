#!/usr/bin/env python3
"""
Arattai Bot - COOKIE FILE VERSION
"""

import requests
import json
import time
import re
from datetime import datetime
from collections import defaultdict
import http.cookiejar as cookielib

class ArattaiBot:
    def __init__(self):
        # ===== YOUR ARATTAI CREDENTIALS =====
        self.BASE_URL = "https://web.arattai.in"
        self.CHAT_ID = "CT_1287521019107750094_20004081014-GC"
        self.USER_ID = "20004081014"  # Your user ID
        
        # ===== BOT'S OWN IDENTITY =====
        self.BOT_SIGNATURE = "🤖"  # Bot uses this emoji
        self.BOT_NAME = "ArattaiBot"
        
        # ===== LOAD COOKIES FROM FILE =====
        self.session = requests.Session()
        self.load_cookies_from_file('cookies.txt')
        
        # Extract CSRF token from cookies
        self.CSRF_TOKEN = None
        for cookie in self.session.cookies:
            if cookie.name == 'CT_CSRF_TOKEN':
                self.CSRF_TOKEN = cookie.value
                break
        
        if not self.CSRF_TOKEN:
            print("⚠️ WARNING: CT_CSRF_TOKEN not found in cookies.txt")
            self.CSRF_TOKEN = ""
        
        # ===== BOT CONFIG =====
        self.PREFIX = "."
        self.CHECK_INTERVAL = 2
        self.LAST_SEEN_TIME = int(time.time() * 1000)
        
        # ===== RATE LIMITING =====
        self.user_last_command = defaultdict(float)
        self.RATE_LIMITS = {
            'default': 2,
            'menu': 5,
            'alive': 3,
            'time': 2,
            'ping': 1,
        }
        
        self.commands = {
            'menu': self.cmd_menu,
            'alive': self.cmd_alive,
            'time': self.cmd_time,
            'ping': self.cmd_ping
        }
        
        self.start_time = time.time()
        
        print("=" * 60)
        print(f"🤖 {self.BOT_NAME} - COOKIE FILE VERSION")
        print("=" * 60)
        print(f"📱 Chat: {self.CHAT_ID[-30:]}")
        print(f"👤 Your ID: {self.USER_ID}")
        print(f"🤖 Bot signature: {self.BOT_SIGNATURE}")
        print(f"🍪 Cookies loaded from: cookies.txt")
        print("=" * 60)
    
    def load_cookies_from_file(self, filename):
        """Load cookies from Netscape format cookie file"""
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
            
            cookie_count = 0
            for line in lines:
                line = line.strip()
                # Skip comments and empty lines
                if line.startswith('#') or not line:
                    continue
                
                # Parse Netscape cookie format
                parts = line.split('\t')
                if len(parts) >= 7:
                    domain = parts[0]
                    flag = parts[1] == 'TRUE'
                    path = parts[2]
                    secure = parts[3] == 'TRUE'
                    expires = parts[4]
                    name = parts[5]
                    value = parts[6]
                    
                    # Create cookie
                    cookie = requests.cookies.create_cookie(
                        domain=domain,
                        name=name,
                        value=value,
                        path=path,
                        secure=secure,
                        expires=None if expires == '0' else int(expires)
                    )
                    self.session.cookies.set_cookie(cookie)
                    cookie_count += 1
            
            print(f"✅ Loaded {cookie_count} cookies from {filename}")
            
        except FileNotFoundError:
            print(f"❌ ERROR: {filename} not found!")
            exit(1)
        except Exception as e:
            print(f"❌ ERROR loading cookies: {e}")
            exit(1)
    
    def is_bot_message(self, text):
        """Check if a message is from the bot"""
        return text and self.BOT_SIGNATURE in text
    
    def send_message(self, message):
        """Send a message with bot signature"""
        # Add bot signature to identify own messages
        full_message = f"{self.BOT_SIGNATURE} {message}"
        
        url = f"{self.BASE_URL}/sendofficechatmessage.do"
        msgid = str(int(time.time() * 1000))
        
        # Build cookie string for header
        cookie_string = '; '.join([f"{c.name}={c.value}" for c in self.session.cookies])
        
        headers = {
            'Host': 'web.arattai.in',
            'Cookie': cookie_string,
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'x-zcsrf-token': f"zchat_csrparam={self.CSRF_TOKEN}",
            'origin': self.BASE_URL,
            'referer': f"{self.BASE_URL}/",
            'client-time': str(int(time.time() * 1000))
        }
        
        data = {
            'chid': self.CHAT_ID,
            'msg': full_message,
            'msgid': msgid,
            'dname': 'BAJRANG',
            'unfurl': 'false'
        }
        
        try:
            response = self.session.post(url, data=data, headers=headers)
            if response.status_code == 200:
                print(f"   ✅ Bot: {message[:30]}")
                return True
            return False
        except:
            return False
    
    def get_new_messages(self):
        """Get new messages only"""
        url = f"{self.BASE_URL}/v2/chats/{self.CHAT_ID}/transcript"
        
        # Build cookie string for header
        cookie_string = '; '.join([f"{c.name}={c.value}" for c in self.session.cookies])
        
        headers = {
            'Host': 'web.arattai.in',
            'Cookie': cookie_string,
            'accept': 'application/json, text/plain, */*',
            'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36',
            'x-requested-with': 'mark.via.gp',
            'x-zcsrf-token': f"zchat_csrparam={self.CSRF_TOKEN}",
            'client-time': str(int(time.time() * 1000)),
            'referer': f"{self.BASE_URL}/"
        }
        
        params = {
            'lineslimit': 30,
            'nocache': str(int(time.time() * 1000))
        }
        
        try:
            response = self.session.get(url, params=params, headers=headers)
            if response.status_code == 200:
                # Fix JSON
                text = response.text
                if text.endswith(',]'):
                    text = text[:-2] + ']'
                
                messages = json.loads(text)
                
                # Find messages after last seen time
                new_messages = []
                for msg in messages:
                    if msg.get('msg') == 'chat.more':
                        continue
                    
                    msg_time = int(msg.get('lmsgtime', 0))
                    if msg_time > self.LAST_SEEN_TIME:
                        new_messages.append(msg)
                        if msg_time > self.LAST_SEEN_TIME:
                            self.LAST_SEEN_TIME = msg_time
                
                if new_messages:
                    print(f"\n📨 {len(new_messages)} new message(s):")
                
                return new_messages
            return []
        except Exception as e:
            print(f"⚠️ Error: {e}")
            return []
    
    def extract_message_info(self, msg_obj):
        """Extract message info"""
        try:
            return {
                'id': msg_obj.get('msgid', msg_obj.get('msguid', '')),
                'sender': msg_obj.get('sender', ''),
                'name': msg_obj.get('dname', 'Unknown'),
                'text': msg_obj.get('msg', ''),
                'time': int(msg_obj.get('lmsgtime', 0))
            }
        except:
            return None
    
    def process_message(self, msg_info):
        """Process a single message"""
        # Show all messages for debugging
        print(f"\n👤 {msg_info['name']}: {msg_info['text']}")
        
        # Skip bot's OWN messages (check by signature, not user ID!)
        if self.is_bot_message(msg_info['text']):
            print(f"   🤖 This is my own message - ignoring")
            return
        
        # Check if it's a command
        if not msg_info['text'].startswith(self.PREFIX):
            return
        
        cmd = msg_info['text'][1:].lower().strip()
        if cmd not in self.commands:
            print(f"   ❓ Unknown command: {cmd}")
            return
        
        print(f"   🔍 Processing command: .{cmd}")
        
        # Rate limiting
        now = time.time()
        last = self.user_last_command.get(msg_info['sender'], 0)
        limit = self.RATE_LIMITS.get(cmd, self.RATE_LIMITS['default'])
        
        if now - last < limit:
            wait = int(limit - (now - last))
            print(f"   ⏳ Rate limited: wait {wait}s")
            self.send_message(f"@{msg_info['name']} ⏳ Wait {wait}s")
            return
        
        self.user_last_command[msg_info['sender']] = now
        
        # Execute command
        response = self.commands[cmd](msg_info['sender'], msg_info['name'])
        self.send_message(response)
    
    def cmd_menu(self, user_id, user_name):
        return f"""**Menu**
• .menu - This menu
• .alive - Bot status
• .time - Current time
• .ping - Test"""
    
    def cmd_alive(self, user_id, user_name):
        uptime = int(time.time() - self.start_time)
        return f"**Alive** • Uptime: {uptime//3600}h {(uptime%3600)//60}m {uptime%60}s"
    
    def cmd_time(self, user_id, user_name):
        return f"**Time**: {datetime.now().strftime('%H:%M:%S')}"
    
    def cmd_ping(self, user_id, user_name):
        return "**PONG!**"
    
    def run(self):
        """Main bot loop"""
        print("\n🟢 Bot is running! Send commands with prefix '.'\n")
        self.send_message("Bot online in this chat!")
        
        while True:
            try:
                messages = self.get_new_messages()
                
                for msg_obj in messages:
                    msg_info = self.extract_message_info(msg_obj)
                    if msg_info:
                        self.process_message(msg_info)
                
                time.sleep(self.CHECK_INTERVAL)
                
            except KeyboardInterrupt:
                print("\n\n👋 Bot stopped")
                break
            except Exception as e:
                print(f"⚠️ Error: {e}")
                time.sleep(5)

if __name__ == "__main__":
    bot = ArattaiBot()
    bot.run()