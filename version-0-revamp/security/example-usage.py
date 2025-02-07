"""
An example of how this will be used
"""
@app.route('/login', methods=['POST'])
def login():
    user_agent_str = request.headers.get('User-Agent', '')
    ip_address = request.remote_addr

    user_agent = user_agents.parse(user_agent_str)
    device_info = {
        "ip_address": ip_address,
        "browser": user_agent.browser.family,
        "browser_version": user_agent.browser.version_string,
        "os": user_agent.os.family,
        "os_version": user_agent.os.version_string,
        "device": user_agent.device.family,
    }

    # Example user_id after authentication
    user_id = 1  # Replace with actual authenticated user ID
    save_device_info(user_id, device_info)

    return {"message": "Login successful"}
