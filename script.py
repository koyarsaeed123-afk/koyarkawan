import requests

# ئەمە ئەو لینکە سەرەکییەیە کە ئەپەکە تەنها تۆکنی لێ وەردەگرێت
token_source = "http://104.160.15.138/XRmDByf1QHTLYakHbDjPfjcc__ih__9PyRiGk8d42qmaDaz5I1k__ih__pfXjxavgua9Bp1zAx5XSBR4M3827ybujacXDxBeB__hi__uNa"

headers = {
    "User-Agent": "And$MyTV/1.1",
    "Host": "104.160.15.138"
}

def get_link():
    try:
        # لێرەدا کۆدەکە دەچێت تۆکنە نوێیەکە ڕاو دەکات
        response = requests.get(token_source, headers=headers, timeout=15)
        if response.status_code == 200:
            new_token_link = response.text.strip()
            
            # دروستکردنی فایلی m3u بۆ ئەوەی هەرگیز نەوەستێت
            with open("falcon_eye.m3u", "w", encoding="utf-8") as f:
                f.write("#EXTM3U\n")
                f.write("#EXTINF:-1,Falcon Eye HD\n")
                f.write(new_token_link)
            print("لینکەکە نوێ کرایەوە!")
    except:
        print("کێشەیەک لە سێرڤەر هەیە")

if __name__ == "__main__":
    get_link()
