# 🐭 Mouse Jiggler: The Ultimate "I'm Definitely Working" Simulator

A simple, effective mouse jiggler application to keep your system active and prevent Microsoft Teams from tattling on you when you're "definitely not" taking a coffee break, walking your dog, or contemplating the meaning of life.

## ✨ Features (aka "Why Your Boss Will Never Know")

- **⚡ Lightning Fast**: Moves mouse every 0.5 seconds - faster than your manager checking Slack
- **🛡️ Safe Mode**: Returns mouse to original position (like you never left your desk, wink wink)
- **🧠 Smart Movement**: Large movements (100px) in safe mode for maximum "I'm totally here" energy, tiny movements (5px) otherwise for stealth mode
- **🎨 User-Friendly GUI**: So simple, even your cat could use it (and probably should)
- **🌍 Cross-Platform**: Works on macOS, Windows, and Linux - because procrastination is universal

## 🛠️ Installation (Don't Panic, It's Easier Than Explaining Why You're "Away")

### Prerequisites (The Boring Stuff)

- Python 3.6 or higher (if you don't have this, what are you even doing?)
- pip (Python package installer - not to be confused with Pip from South Park)

### Setup (The Fun Part)

1. **Navigate to the project directory** (like walking to the fridge, but for nerds)
   ```bash
   cd mouse_jiggler
   ```

2. **Create a virtual environment** (because we're fancy like that)
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies** (the magic ingredients)
   ```bash
   pip install -r requirements.txt
   ```

4. **Install tkinter support** (macOS only - because Apple likes to be special)
   ```bash
   brew install python-tk
   ```

### 🍎 macOS Specific Setup (Because Apple Users Are Special Snowflakes)

On macOS, you'll need to grant accessibility permissions (don't worry, we're not stealing your data... probably):

1. Run the application once - it will likely fail spectacularly but prompt the system
2. Go to **System Preferences** > **Security & Privacy** > **Privacy** > **Accessibility**
3. Click the lock icon and enter your password (the one you definitely remember)
4. Add **Terminal** or **Python** to the list of allowed applications
5. Restart the application and watch the magic happen

## 🎮 Usage (The Moment You've Been Waiting For)

### Running the Application

1. **Activate virtual environment** (if using one - and you should, you rebel)
   ```bash
   source venv/bin/activate
   ```

2. **Run the application** (drumroll please...)
   ```bash
   python mouse_jiggler.py
   ```

### Using the GUI (It's So Easy, Your Goldfish Could Do It)

The interface is simpler than your last relationship:

1. **🛡️ Safe Mode Checkbox**: 
   - **ON**: Mouse does the cha-cha (100px moves) and returns home like a good boy
   - **OFF**: Mouse takes tiny baby steps (5px) and never comes back (commitment issues)
2. **Click "Start Jiggling"** to begin the deception (moves every 0.5 seconds)
3. **Click "Stop"** when your boss walks by

### Settings Explained (For Those Who Read Manuals)

- **🛡️ Safe Mode ON**: Large 100-pixel movements that return to original position - like a boomerang, but for your cursor
- **🛡️ Safe Mode OFF**: Small 5-pixel movements that accumulate over time - death by a thousand cuts, mouse edition
- **⏰ Interval**: Fixed at 0.5 seconds because we're impatient and so is your status indicator

## 💼 Perfect for Microsoft Teams (And Your Sanity)

This tool is specifically designed to keep Microsoft Teams from snitching on you when you're "definitely working from home" and not binge-watching Netflix. The lightning-fast 0.5-second interval ensures your status stays greener than your envy of people with better work-life balance.

## 🛡️ Safety Features (Because We're Responsible Adults... Sort Of)

- **🏠 Safe Mode**: Returns mouse to original position (like it never happened - the perfect crime)
- **🚧 Boundary Checking**: Ensures mouse stays within screen bounds (no escaping to other dimensions)
- **🎭 Graceful Shutdown**: Properly stops all threads when closing (unlike your last relationship)
- **🔧 Error Handling**: Continues running even if individual movements fail (more reliable than your internet connection)

## 🆘 Troubleshooting (When Things Go Wrong, As They Do)

### 🔒 Permission Issues (macOS)
If you get permission errors (and you probably will):
1. Go to System Preferences > Security & Privacy > Privacy > Accessibility
2. Add Terminal or Python to the allowed apps list (trust us, we're friendly)
3. Restart the application and pray to the tech gods

### 🐍 Virtual Environment Issues
If you get "command not found" errors (classic):
1. Make sure you've activated the virtual environment: `source venv/bin/activate`
2. Install dependencies within the virtual environment (not in your neighbor's)
3. Run the application from within the activated environment (stay in your lane)

### 🖼️ tkinter Not Found (macOS)
If you get "_tkinter module not found" (Apple being Apple):
1. Install tkinter support: `brew install python-tk`
2. Restart your terminal and try again (turn it off and on again, the universal solution)

### 🐭 Application Not Moving Mouse
- Ensure you've granted the necessary permissions (we're not mind readers)
- Try running with administrator/sudo privileges if needed (go full dictator mode)
- Check that pyautogui is properly installed (it's not you, it's the dependencies)

## 🤓 Technical Details (For the Nerds Among Us)

- Built with Python and Tkinter for the GUI (because we're old school like that)
- Uses pyautogui for mouse control (the puppet master of cursors)
- Runs mouse movements in a separate thread to prevent GUI freezing (multitasking like a boss)
- Configurable and safe for extended use (marathon-ready procrastination tool)

## 📜 License

This project is open source and available under the MIT License (aka "do whatever you want, just don't sue us").

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements. We welcome all contributions, especially if they make this tool even more sneaky.

---

**⚠️ Disclaimer**: This tool is designed for "legitimate" use cases like preventing system idle during presentations or maintaining active status in communication applications. Please use responsibly and in accordance with your organization's policies. We are not responsible for any awkward conversations with HR. 😉

*P.S. - If your boss is reading this, this is definitely a productivity tool and not at all what you think it is. Trust us, we're engineers.* 