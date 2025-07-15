# Mouse Jiggler

A simple, effective mouse jiggler application to keep your system active and prevent Microsoft Teams (and other applications) from going idle.

## Features

- **Fast Movement**: Moves mouse every 0.5 seconds for maximum effectiveness
- **Safe Mode**: Option to return mouse to original position after each movement
- **Smart Movement**: Large movements (100px) in safe mode, small movements (5px) otherwise
- **User-Friendly GUI**: Simple, clean interface
- **Cross-Platform**: Works on macOS, Windows, and Linux

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. **Navigate to the project directory**
   ```bash
   cd mouse_jiggler
   ```

2. **Create a virtual environment** (recommended for macOS)
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install tkinter support** (macOS only)
   ```bash
   brew install python-tk
   ```

### macOS Specific Setup

On macOS, you'll need to grant accessibility permissions:

1. Run the application once - it will likely fail but prompt the system
2. Go to **System Preferences** > **Security & Privacy** > **Privacy** > **Accessibility**
3. Click the lock icon and enter your password
4. Add **Terminal** or **Python** to the list of allowed applications
5. Restart the application

## Usage

### Running the Application

1. **Activate virtual environment** (if using one)
   ```bash
   source venv/bin/activate
   ```

2. **Run the application**
   ```bash
   python mouse_jiggler.py
   ```

### Using the GUI

The interface is simple and focused:

1. **Safe Mode Checkbox**: 
   - **ON**: Mouse moves up to 100 pixels and returns to original position
   - **OFF**: Mouse moves 5 pixels and stays there
2. **Click "Start Jiggling"** to begin (moves every 0.5 seconds)
3. **Click "Stop"** to end the mouse movement

### Settings Explained

- **Safe Mode ON**: Large 100-pixel movements that return to original position - more noticeable but doesn't interfere with your work
- **Safe Mode OFF**: Small 5-pixel movements that accumulate over time
- **Interval**: Fixed at 0.5 seconds for maximum effectiveness

## Perfect for Microsoft Teams

This tool is specifically designed to keep Microsoft Teams active by preventing your system from going idle. The fast 0.5-second interval ensures your status stays active.

## Safety Features

- **Safe Mode**: Returns mouse to original position (recommended)
- **Boundary Checking**: Ensures mouse stays within screen bounds
- **Graceful Shutdown**: Properly stops all threads when closing
- **Error Handling**: Continues running even if individual movements fail

## Troubleshooting

### Permission Issues (macOS)
If you get permission errors:
1. Go to System Preferences > Security & Privacy > Privacy > Accessibility
2. Add Terminal or Python to the allowed apps list
3. Restart the application

### Virtual Environment Issues
If you get "command not found" errors:
1. Make sure you've activated the virtual environment: `source venv/bin/activate`
2. Install dependencies within the virtual environment
3. Run the application from within the activated environment

### tkinter Not Found (macOS)
If you get "_tkinter module not found":
1. Install tkinter support: `brew install python-tk`
2. Restart your terminal and try again

### Application Not Moving Mouse
- Ensure you've granted the necessary permissions
- Try running with administrator/sudo privileges if needed
- Check that pyautogui is properly installed

## Technical Details

- Built with Python and Tkinter for the GUI
- Uses pyautogui for mouse control
- Runs mouse movements in a separate thread to prevent GUI freezing
- Configurable and safe for extended use

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

---

**Note**: This tool is designed for legitimate use cases like preventing system idle during presentations or maintaining active status in communication applications. Please use responsibly and in accordance with your organization's policies. 