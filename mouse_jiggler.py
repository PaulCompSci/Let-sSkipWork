#!/usr/bin/env python3
"""
Mouse Jiggler - Keep your system active by moving the mouse
Perfect for keeping Microsoft Teams and other applications active
"""

import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui
import threading
import time
import random
import sys
import os

class MouseJiggler:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Jiggler")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Variables
        self.is_running = False
        self.jiggle_thread = None
        self.interval = tk.DoubleVar(value=0.5)  # Default 0.5 seconds
        self.movement_type = tk.StringVar(value="small")
        self.safe_mode = tk.BooleanVar(value=True)
        
        # Disable pyautogui failsafe for smooth operation
        pyautogui.FAILSAFE = False
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Title
        title_label = ttk.Label(main_frame, text="Mouse Jiggler", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Safe mode
        ttk.Checkbutton(main_frame, text="Safe Mode (return to original position)", 
                       variable=self.safe_mode).grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=10)
        
        # Status
        self.status_label = ttk.Label(main_frame, text="Status: Stopped", font=("Arial", 10))
        self.status_label.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Control buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        self.start_button = ttk.Button(button_frame, text="Start Jiggling", command=self.start_jiggling)
        self.start_button.grid(row=0, column=0, padx=5)
        
        self.stop_button = ttk.Button(button_frame, text="Stop", command=self.stop_jiggling, state=tk.DISABLED)
        self.stop_button.grid(row=0, column=1, padx=5)
        
        # Info text
        info_text = ("This tool moves your mouse every 0.5 seconds to keep your system active.\n"
                    "Perfect for preventing Microsoft Teams from going idle.")
        info_label = ttk.Label(main_frame, text=info_text, font=("Arial", 9), 
                              justify=tk.CENTER, wraplength=350)
        info_label.grid(row=4, column=0, columnspan=2, pady=20)
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        
    def start_jiggling(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.status_label.config(text="Status: Running")
            
            # Start jiggling in a separate thread
            self.jiggle_thread = threading.Thread(target=self.jiggle_loop, daemon=True)
            self.jiggle_thread.start()
            
    def stop_jiggling(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Stopped")
        
    def jiggle_loop(self):
        while self.is_running:
            try:
                self.move_mouse()
                # Wait for the specified interval
                time.sleep(self.interval.get())
            except Exception as e:
                print(f"Error in jiggle loop: {e}")
                break
                
    def move_mouse(self):
        try:
            # Get current mouse position
            current_x, current_y = pyautogui.position()
            
            # Get screen size
            screen_width, screen_height = pyautogui.size()
            
            # Use bigger movement in safe mode since it returns to original position
            if self.safe_mode.get():
                distance = 100  # Larger movement in safe mode
            else:
                distance = 5 # Small movement when not in safe mode
            
            # Generate random movement
            dx = random.randint(-distance, distance)
            dy = random.randint(-distance, distance)
            
            new_x = max(0, min(screen_width - 1, current_x + dx))
            new_y = max(0, min(screen_height - 1, current_y + dy))
            
            # Move mouse
            pyautogui.moveTo(new_x, new_y, duration=0.1)
            
            # If safe mode is enabled, move back to original position
            if self.safe_mode.get():
                time.sleep(0.1)
                pyautogui.moveTo(current_x, current_y, duration=0.1)
                
        except Exception as e:
            print(f"Error moving mouse: {e}")
            
    def on_closing(self):
        self.stop_jiggling()
        self.root.destroy()

def main():
    # Check if running on macOS and provide accessibility permission info
    if sys.platform == "darwin":
        print("Mouse Jiggler for macOS")
        print("Note: You may need to grant accessibility permissions to Terminal or Python")
        print("Go to System Preferences > Security & Privacy > Privacy > Accessibility")
        print("and add Terminal or Python to the list of allowed apps.")
        print()
    
    root = tk.Tk()
    app = MouseJiggler(root)
    
    # Handle window closing
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        app.stop_jiggling()
        print("\nMouse Jiggler stopped.")

if __name__ == "__main__":
    main() 