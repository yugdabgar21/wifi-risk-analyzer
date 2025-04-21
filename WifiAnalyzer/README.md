Wi-Fi Risk Analyzer
A Python-based desktop application to evaluate public Wi-Fi network safety. It scans for risks like open ports, DNS leaks, captive portals, and HTTPS downgrades, featuring a multilingual GUI (English, Gujarati, Hindi), custom audio feedback, and a progress bar. Built with tkinter, pygame, and requests.
Features

Network Scanning: Checks local IP, open ports (21, 22, 23, 53, 80, 443, 8080), DNS leaks, captive portals, and HTTPS redirects.
Multilingual GUI: Supports English, Gujarati, and Hindi with translated labels and audio.
Custom Audio: Pre-recorded MP3 files for scan status and risk levels (low, medium, high).
User-Friendly Design: Includes a progress bar, dark mode toggle, and threaded scanning for smooth performance.

Installation

Clone the repository:git clone https://github.com/yugdabgar21/wifi-risk-analyzer.git
cd wifi-risk-analyzer


Install dependencies:pip install -r requirements.txt


Ensure audio files (*.mp3) are in the project root.
Run the application:python wifi_risk_analyser.py



Usage

Select a language (English, Gujarati, or Hindi) from the dropdown.
Click "Start Scan" to analyze the Wi-Fi network.
View results in the text area, with audio feedback for scan status and risk level.
Toggle dark mode for better visibility.

Technologies Used

Python: Core programming language.
tkinter: GUI framework.
pygame: Audio playback for MP3 files.
requests: HTTP requests for network checks.
socket: Port scanning functionality.

Future Improvements

Add more languages for broader accessibility.
Include advanced security checks (e.g., VPN detection, ARP spoofing).
Optimize audio file loading for faster startup.

Contributing
Contributions are welcome! Fork the repository, create a feature branch, and submit a pull request. Report issues or suggestions via GitHub Issues.
License
MIT License
