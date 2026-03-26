import requests

url = "http://104.160.15.138/XRmDByf1QHTLYakHbDjPfjcc__ih__9PyRiGk8d42qmaDaz5I1k__ih__pfXjxavgua9Bp1zAx5XSBR4M3827ybujacXDxBeB__hi__uNa"

headers = {
    "User-Agent": "And$MyTV/1.1 (Linux; Android 9; JKM-LX1 Build/HUAWEIJ KML-LX1)",
    "Host": "104.160.15.138",
    "Connection": "Keep-Alive"
}

def update():
    try:
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code == 200:
            # ناوی فایلەکە لێرە گرنگە
            with open("playlist.m3u", "w", encoding="utf-8") as f:
                f.write("#EXTM3U\n#EXTINF:-1,Falcon Eye HD\n" + response.text.strip())
            print("Success!")
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Fail: {e}")

if __name__ == "__main__":
    update()
