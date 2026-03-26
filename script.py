import requests

# ناونیشانی سەرچاوەکە
url = "http://104.160.15.138/XRmDByf1QHTLYakHbDjPfjcc__ih__9PyRiGk8d42qmaDaz5I1k__ih__pfXjxavgua9Bp1zAx5XSBR4M3827ybujacXDxBeB__hi__uNa"

# ئەم زانیارییانە وای لێ دەکات وەک مۆبایلەکەت دەربکەوێت
headers = {
    "User-Agent": "And$MyTV/1.1 (Linux; Android 9; JKM-LX1 Build/HUAWEIJ KML-LX1)",
    "Accept-Encoding": "gzip",
    "Connection": "Keep-Alive",
    "Host": "104.160.15.138"
}

def get_link():
    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            link = response.text.strip()
            # دروستکردنی فایلی m3u
            with open("falcon_eye.m3u", "w", encoding="utf-8") as f:
                f.write("#EXTM3U\n#EXTINF:-1,Falcon Eye HD\n" + link)
            print("Done! Link Updated.")
        else:
            print(f"Server rejected us with code: {response.status_code}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    get_link()
