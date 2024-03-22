import mcstatus

def check_server_status(ip, port):
    try:
        server = mcstatus.lookup(f"{ip}:{port}")
        status = server.status()
        print("The server is online.")
        return True
    except (ConnectionRefusedError, OSError):
        print("The server is offline.")
        return False

if __name__ == "__main__":
    server_ip = "ruby.magmanode.com"
    server_port = 32301 # Default Minecraft server port

    check_server_status(server_ip, server_port)
