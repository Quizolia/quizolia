"""
This Flask code extracts the user's device information
and stores it into the database
"""
from flask import Flask, request
import user_agents

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    user_agent_str = request.headers.get('User-Agent', '')
    ip_address = request.remote_addr  # Gets user IP

    # Parse user-agent string
    user_agent = user_agents.parse(user_agent_str)

    device_info = {
        "ip_address": ip_address,
        "browser": user_agent.browser.family,
        "browser_version": user_agent.browser.version_string,
        "os": user_agent.os.family,
        "os_version": user_agent.os.version_string,
        "device": user_agent.device.family,
    }

    return device_info  # For testing, return JSON response

if __name__ == '__main__':
    app.run(debug=True)
