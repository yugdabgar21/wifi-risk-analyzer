import socket
import requests
import subprocess
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
import threading
import os
import pygame

# ========== Language Packs ==========
LANGUAGES = {
    "English": {
        "title": "Public Wi-Fi Risk Analyzer",
        "start": "Start Scan",
        "ip": "Your IP",
        "open_ports": "Open Ports",
        "dns_leak": "DNS Leak Detected",
        "captive": "Captive Portal Detected",
        "https": "HTTPS Downgrade Detected",
        "final": "Final Risk Score",
        "low": "Low Risk: Network seems safe.",
        "medium": "Medium Risk: Use VPN if possible.",
        "high": "High Risk: Avoid sensitive activity.",
        "no_wifi": "Please connect to a Wi-Fi network to run the test.",
        "error": "An error occurred during the scan.",
        "scan_started": "Scan started"
    },
    "Gujarati": {
        "title": "પબ્લિક Wi-Fi જોખમ વિશ્લેષક",
        "start": "સ્કેન શરૂ કરો",
        "ip": "તમારું IP",
        "open_ports": "ખુલ્લા પોર્ટ્સ",
        "dns_leak": "DNS લીક શોધાયું",
        "captive": "કૅપ્ટિવ પોર્ટલ શોધાયું",
        "https": "HTTPS ડાઉનગ્રેડ શોધાયું",
        "final": "અંતિમ જોખમ સ્કોર",
        "low": "ઓછું જોખમ: નેટવર્ક સુરક્ષિત લાગે છે.",
        "medium": "મધ્યમ જોખમ: શક્ય હોય તો VPN વાપરો.",
        "high": "ઉચ્ચ જોખમ: સંવેદનશીલ પ્રવૃત્તિથી બચો.",
        "no_wifi": "કૃપા કરીને ટેસ્ટ માટે Wi-Fi સાથે જોડાઓ.",
        "error": "સ્કેન દરમિયાન ભૂલ થઈ.",
        "scan_started": "સ્કેન શરૂ થયું"
    },
    "Hindi": {
        "title": "पब्लिक Wi-Fi जोखिम विश्लेषक",
        "start": "स्कैन प्रारंभ करें",
        "ip": "आपका IP",
        "open_ports": "ओपन पोर्ट्स",
        "dns_leak": "DNS लीक पाया गया",
        "captive": "कैप्टिव पोर्टल पाया गया",
        "https": "HTTPS डाउनग्रेड पाया गया",
        "final": "अंतिम जोखिम स्कोर",
        "low": "कम जोखिम: नेटवर्क सुरक्षित लगता है।",
        "medium": "मध्यम जोखिम: यदि संभव हो तो VPN का उपयोग करें।",
        "high": "उच्च जोखिम: संवेदनशील गतिविधि से बचें।",
        "no_wifi": "कृपया परीक्षण के लिए Wi-Fi से कनेक्ट करें।",
        "error": "स्कैन के दौरान एक त्रुटि हुई।",
        "scan_started": "स्कैन शुरू हुआ"
    }
}

# ========== Audio File Mappings ==========
AUDIO_FILES = {
    "English": {
        "scan_started": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\scan_started_en.mp3",
        "no_wifi": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\no_wifi_en.mp3",
        "error": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\error_en.mp3",
        "low": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\low_risk_en.mp3",
        "medium": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\medium_risk_en.mp3",
        "high": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\high_risk_en.mp3"
    },
    "Gujarati": {
        "scan_started": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\scan_started_gu.mp3",
        "no_wifi": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\no_wifi_gu.mp3",
        "error": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\error_gu.mp3",
        "low": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\low_risk_gu.mp3",
        "medium": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\medium_risk_gu.mp3",
        "high": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\high_risk_gu.mp3"
    },
    "Hindi": {
        "scan_started": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\scan_started_hi.mp3",
        "no_wifi": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\no_wifi_hi.mp3",
        "error": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\error_hi.mp3",
        "low": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\low_risk_hi.mp3",
        "medium": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\medium_risk_hi.mp3",
        "high": r"C:\Users\yugda\OneDrive\Desktop\Yug VS\WifiAnalyzer\high_risk_hi.mp3"
    }
}

current_lang = "English"

# Initialize pygame mixer for audio playback
pygame.mixer.init()

def speak(key):
    try:
        audio_file = AUDIO_FILES[current_lang].get(key)
        if audio_file and os.path.exists(audio_file):
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():  # Wait for audio to finish
                pygame.time.Clock().tick(10)
        else:
            print(f"Audio file for '{key}' in {current_lang} not found: {audio_file or 'None'}")
    except Exception as e:
        print(f"Error playing audio for '{key}': {e}")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return None

def scan_ports(ip):
    common_ports = [21, 22, 23, 53, 80, 443, 8080]
    open_ports = []
    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            continue
    return open_ports

def check_dns_leak():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        return response.status_code != 200
    except:
        return True

def detect_captive_portal():
    try:
        r = requests.get("http://1.1.1.1", timeout=5)
        return "cloudflare" not in r.text.lower()
    except:
        return True

def check_https_redirect():
    try:
        r = requests.get("http://example.com", allow_redirects=True, timeout=5)
        return not r.url.startswith("https://")
    except:
        return True

def calculate_risk_score(open_ports, dns_leak, captive, https_downgrade):
    score = 0
    if any(p in open_ports for p in [23, 21]): score += 2
    if dns_leak: score += 2
    if captive: score += 2
    if https_downgrade: score += 2
    if not open_ports: score -= 1
    return max(0, min(score, 10))

def run_scan():
    labels = LANGUAGES[current_lang]
    ip = get_local_ip()
    if not ip or ip.startswith("169.") or ip == "0.0.0.0":
        messagebox.showerror("Wi-Fi Not Connected", labels['no_wifi'])
        speak("no_wifi")
        return

    progress['value'] = 0
    progress.pack(pady=5)
    result_label.config(text="")
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, f"{labels['ip']}: {ip}\n")
    speak("scan_started")

    tasks = 4  # Ports, DNS, Captive, HTTPS
    progress_step = 100 / tasks

    try:
        open_ports = scan_ports(ip)
        progress['value'] += progress_step
        root.update()

        dns_leak = check_dns_leak()
        progress['value'] += progress_step
        root.update()

        captive = detect_captive_portal()
        progress['value'] += progress_step
        root.update()

        https_downgrade = check_https_redirect()
        progress['value'] += progress_step
        root.update()

        text_output.insert(tk.END, f"{labels['open_ports']}: {open_ports}\n")
        text_output.insert(tk.END, f"{labels['dns_leak']}: {'No' if not dns_leak else 'Yes'}\n")
        text_output.insert(tk.END, f"{labels['captive']}: {'No' if not captive else 'Yes'}\n")
        text_output.insert(tk.END, f"{labels['https']}: {'No' if not https_downgrade else 'Yes'}\n")

        score = calculate_risk_score(open_ports, dns_leak, captive, https_downgrade)
        result_text = f"\n{labels['final']}: {score}/10\n"

        if score >= 7:
            result_text += f"{labels['high']}"
            result_label.config(fg="red")
            speak("high")
        elif score >= 4:
            result_text += f"{labels['medium']}"
            result_label.config(fg="orange")
            speak("medium")
        else:
            result_text += f"{labels['low']}"
            result_label.config(fg="green")
            speak("low")

        result_label.config(text=result_text)
        text_output.insert(tk.END, result_text)
    except Exception as e:
        messagebox.showerror("Error", labels['error'])
        speak("error")
    finally:
        progress.pack_forget()

def run_in_thread():
    threading.Thread(target=run_scan, daemon=True).start()

def change_language(lang):
    global current_lang
    current_lang = lang
    labels = LANGUAGES[lang]
    title.config(text=labels['title'])
    start_button.config(text=labels['start'])
    root.title(labels['title'])

def toggle_dark_mode():
    dark = root.cget('bg') == '#121212'
    new_bg = '#f2f2f2' if dark else '#121212'
    new_fg = '#000000' if dark else '#ffffff'

    root.configure(bg=new_bg)
    style.configure("TCombobox", fieldbackground=new_bg, background=new_bg, foreground=new_fg)
    text_output.configure(bg=new_bg, fg=new_fg, insertbackground=new_fg)

    for widget in [title, start_button, result_label, toggle_btn]:
        widget.configure(bg=new_bg, fg=new_fg)

# GUI
root = tk.Tk()
root.title(LANGUAGES[current_lang]['title'])
root.geometry("550x600")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

style = ttk.Style()
style.theme_use('clam')

title = tk.Label(root, text=LANGUAGES[current_lang]['title'], font=("Helvetica", 16, "bold"), bg="#f2f2f2")
title.pack(pady=10)

start_button = tk.Button(root, text=LANGUAGES[current_lang]['start'], font=("Arial", 14), bg="#4CAF50", fg="white", command=run_in_thread)
start_button.pack(pady=5)

progress = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=300, maximum=100)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f2f2f2")
result_label.pack()

text_output = ScrolledText(root, width=62, height=20, font=("Consolas", 10), bg="#f2f2f2")
text_output.pack(padx=10, pady=10)

lang_menu = ttk.Combobox(root, values=list(LANGUAGES.keys()), state="readonly")
lang_menu.set(current_lang)
lang_menu.pack()
lang_menu.bind("<<ComboboxSelected>>", lambda e: change_language(lang_menu.get()))

toggle_btn = tk.Button(root, text="Toggle Dark Mode", command=toggle_dark_mode)
toggle_btn.pack(pady=5)

root.mainloop()