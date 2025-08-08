**🚀 WiFi Risk Analyser - Secure Your Wi-Fi Network 🚀**
=====================================

Tagline: "An innovative Python project for identifying and mitigating Wi-Fi security risks"

**📖 Description**
----------------

The WiFi Risk Analyser is an open-source Python project designed to help individuals and organizations identify and mitigate potential security risks associated with their Wi-Fi networks. This project is built on top of popular Python libraries and utilizes various tools to scan and analyze Wi-Fi networks, providing a comprehensive report on potential vulnerabilities.

The project's primary goal is to provide a user-friendly interface for network administrators to assess the security posture of their Wi-Fi networks. By leveraging the power of Python, the WiFi Risk Analyser can execute a range of tasks, including network scanning, port scanning, and vulnerability assessment.

**✨ Features**
------------

1. **Network Scanning**: The project can scan for nearby Wi-Fi networks, collecting vital information such as network name, IP address, and signal strength.
2. **Port Scanning**: The project can perform port scanning to identify open ports and services running on the target network.
3. **Vulnerability Assessment**: The project can identify potential vulnerabilities in the target network, including outdated software, weak passwords, and misconfigured services.
4. **Customizable Scanning**: Users can configure the scanning process to suit their specific needs, selecting which protocols and ports to scan.
5. **Real-time Results**: The project provides real-time results, allowing users to monitor the scanning process and receive instant notifications of potential vulnerabilities.
6. **User-Friendly Interface**: The project features a user-friendly graphical interface, making it easy for network administrators to navigate and interpret the results.
7. **Multi-Threading Support**: The project supports multi-threading, allowing it to scan multiple networks and protocols simultaneously.
8. **Output Report**: The project generates a comprehensive report detailing the scanning results, including potential vulnerabilities and recommendations for remediation.

**🧰 Tech Stack**
----------------

| **Component** | **Version** | **Description** |
| --- | --- | --- |
| **Python** | 3.9.x | Programming language used for the project |
| **tkinter** | 8.6.x | GUI library used for the user interface |
| **requests** | 2.25.x | Library used for making HTTP requests |
| **subprocess** | 0.64.x | Library used for executing system commands |
| **socket** | 1.1.x | Library used for working with network sockets |
| **importlib.util** | 1.2.x | Library used for importing modules |
| **ScrolledText** | 1.0.x | Library used for creating scrollable text areas |

**📁 Project Structure**
-------------------------

```
wifi_risk_analyser/
📁 src/
📁 main.py
📁 scanner.py
📁 report_generator.py
📁 gui/
📁 main_window.py
📁 network_scan_widget.py
📁 port_scan_widget.py
📁 vulnerability_widget.py
📁 tests/
📁 test_scanner.py
📁 test_report_generator.py
README.md
requirements.txt
```

**⚙️ How to Run**
----------------

### Setup

1. Install Python 3.9.x or later.
2. Install the required dependencies by running `pip install -r requirements.txt` in the project directory.

### Environment

1. Ensure you have a stable internet connection.
2. Set up a virtual environment using your preferred tool (e.g., `virtualenv` or `conda`).

### Build

1. Run `python main.py` in the project directory to execute the project.
2. Follow the on-screen instructions to configure the scanning process.

### Deploy

1. The project can be run locally or deployed to a remote server for network scanning and reporting.

**🧪 Testing Instructions**
-------------------------

To test the project, follow these steps:

1. Run `python -m unittest tests.test_scanner.py` to execute the scanner tests.
2. Run `python -m unittest tests.test_report_generator.py` to execute the report generator tests.

**📦 API Reference**
------------------

The project does not provide an API reference at this time. However, we plan to add an API in the future for integrating with other tools and services.

**👤 Author**
------------

The WiFi Risk Analyser is maintained by Yug aka MASTERxD, a passionate individual with a focus on network security and Python programming.

**📝 License**
-------------

The WiFi Risk Analyser is licensed under the MIT License. See `LICENSE` for more information.

Thank you for using the WiFi Risk Analyser!