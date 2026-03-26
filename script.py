import requests

# Linki serchaway tokenaka
url = "http://104.160.15.138/XRmDByf1QHTLYakHbDjPfjcc__ih__9PyRiGk8d42qmaDaz5I1k__ih__pfXjxavgua9Bp1zAx5XSBR4M3827ybujacXDxBeB__hi__uNa"

# Headers bo away serveraka fely lenagret
headers = {
    "User-Agent": "And$MyTV/1.1",
    "Host": "104.160.15.138",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

def update_link():
    try:
        # Nardni dawakari bo server
        response = requests.get(url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            token_data = response.text.strip()
            
            # Drustkrdni faily m3u
            with open("playlist.m3u", "w", encoding="utf-8") as f:
                f.write("#EXTM3U\n")
                f.write("#EXTINF:-1,Falcon Eye HD\n")
                f.write(token_data)
            print("Serkawtw bw! Linkaka nwe krayawa.")
        else:
            print(f"Server error: {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_link()
