Hector - Voice Assistant 🤖🎙️

Hector is a Python-based desktop voice assistant that can perform system tasks, open websites, respond using AI-powered Wikipedia summaries, manage files, control volume, take screenshots, and more — all through voice commands.

This project is designed for beginners who want to learn:

Voice recognition in Python
Text-to-speech systems
Desktop automation
AI assistant logic
Python automation projects
✨ Features
🎤 Voice Recognition

Hector listens to your microphone and converts speech into text using Google Speech Recognition.

🔊 Text-to-Speech

Uses pyttsx3 for offline speech synthesis.

🌐 Open Websites

Can open:

YouTube
Google
GitHub
Stack Overflow
WhatsApp Web
Facebook
Instagram
🖥️ System Controls
Shutdown PC
Restart PC
Lock System
Volume Up/Down
Mute Audio
📸 Screenshot Capture

Takes screenshots and saves them automatically.

📂 File & Folder Operations
Create folders
Open files
⏰ Timer Feature

Set countdown timers using voice commands.

📊 System Monitoring

Checks:

CPU Usage
RAM Usage
🎲 Fun Commands
Flip a coin
Roll a dice
Tell jokes
🧠 AI Chat

Uses Wikipedia summaries to answer general questions.

🛠️ Technologies Used
Python
SpeechRecognition
pyttsx3
pyautogui
psutil
Wikipedia API
Webbrowser Module
OS Automation
📦 Required Libraries

Install all dependencies using:

pip install pyttsx3 SpeechRecognition wikipedia pyautogui pyperclip psutil requests beautifulsoup4 pyaudio
▶️ How to Run
Clone the repository:
git clone https://github.com/yourusername/hector-voice-assistant.git
Navigate to the project folder:
cd hector-voice-assistant
Run the Python file:
python hector.py
🎯 Voice Commands Examples
Command	Action
"Open YouTube"	Opens YouTube
"Open GitHub"	Opens GitHub
"What is the time"	Speaks current time
"System info"	Tells CPU & RAM usage
"Take screenshot"	Saves screenshot
"Shutdown"	Shuts down computer
"Restart"	Restarts computer
"Mute"	Mutes volume
"Set timer 10"	Sets 10 second timer
"Flip a coin"	Random coin toss
"Search Python tutorials"	Searches Google
🧠 Project Structure
hector/
│
├── hector.py          # Main assistant file
├── screenshots/       # Saved screenshots
├── README.md
⚙️ How It Works
1. Speech Input

The assistant listens using the microphone through:

speech_recognition
2. Command Processing

The spoken text is converted to lowercase and checked against command conditions.

Example:

elif 'open youtube' in query:
    webbrowser.open("https://youtube.com")
3. Voice Response

The assistant replies using:

pyttsx3
4. Automation Tasks

System commands use:

os
pyautogui
psutil
🚀 Future Improvements

Possible upgrades:

ChatGPT API integration
GUI Interface
Face Recognition
Music Controls
Weather Updates
Email Sender
Alarm System
AI Conversation Memory
Smart Home Control
⚠️ Notes
This project currently works best on Windows because it uses:
sapi5
Make sure microphone permissions are enabled.
Some commands require administrator permissions.
📚 Learning Outcomes

By building this project, you learn:

Python automation
Voice AI fundamentals
APIs and libraries
Desktop assistants
Event-driven programming
🤝 Contributing

Pull requests are welcome.

For major changes:

Fork the repository
Create a new branch
Commit changes
Open a Pull Request
📄 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Built with Python and automation ❤️
