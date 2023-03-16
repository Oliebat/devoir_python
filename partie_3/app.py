from flask import Flask, render_template
import platform
import cpuinfo
import socket
import os
import psutil

# # Creating the Flask app
app = Flask(__name__)

# Class to get the system information
class SystemInfo:
    def __init__(self):
        self.os = platform.system()
        self.hostname = socket.gethostname()
        self.ip_address = socket.gethostbyname(self.hostname)
        self.cpu_info = cpuinfo.get_cpu_info()
        self.os_version = platform.version()
        self.python_version = platform.python_version()
        self.username = os.getlogin()
        self.total_ram = psutil.virtual_memory().total
        self.ip = socket.gethostbyname(socket.gethostname())

# Function to get the system information
    def get_info(self):
        return {
            "os": self.os,
            "hostname": self.hostname,
            "ip_address": self.ip_address,
            "cpu_info": self.cpu_info,
            "os_version": self.os_version,
            "python_version": self.python_version,
            "username": self.username,
            "total_ram": self.total_ram,
            "ip": self.ip
        }
# Route to the index page
@app.route("/")
def index():
    # SystemInfo object
    system_info = SystemInfo()
    # Return the index.html template with the system information
    return render_template("index.html", info=system_info.get_info())


app.run(debug=True)
