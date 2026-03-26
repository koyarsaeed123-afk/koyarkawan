import requests

# ناونیشانی سەرچاوەی تۆکنەکە
url = "http://104.160.15.138/XRmDByf1QHTLYakHbDjPfjcc__ih__9PyRiGk8d42qmaDaz5I1k__ih__pfXjxavgua9Bp1zAx5XSBR4M3827ybujacXDxBeB__hi__uNa"

# ئەم بەشە زۆر گرنگە بۆ ئەوەی سێرڤەرەکە فێڵت لێ نەگرێت
headers = {
    "User-Agent": "And$MyTV/1.1",
    "Host": "104.160.15.138",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

def update_link():
    try:
        # ناردنی داواکاری بە زانیارییە مۆبایلییەکانەوە
        response = requests.get(url, headers=headers, timeout=20)
        
        if response.status_code == 200 and response.text.strip():
            new_link = response.text.strip()
            
            # دروستکردنی فایلی m3u8 بە لینکی نوێوە
            with open("playlist.m3u", "w", encoding="utf-8") as f:
                f.write("#EXTM3U\n")
                f.write("#EXTINF:-1,Falcon Eye HD\n")
                f.write(new_link)
            print("سەرکەوتوو بوو: لینکەکە نوێ کرایەوە.")
        else:
            print(f"سێرڤەر وەڵامی نەدا. کۆدی هەڵە: {response.status_code}")
            
    except Exception as e:
        print(f"کێشەیەک ڕوویدا: {e}")

if __name__ == "__main__":
    update_link()
