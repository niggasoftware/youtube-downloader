
try:
    import pafy
except Exception:
    print("[+] Module pafy not installed")
    quit()

url = raw_input("[+] Insert the url:\n")

try:
    video = pafy.new(url)
except Exception:
    print("[+] Invalid url")
    quit()

print("\n[+] Video selected:\n")
print("\t" + "" + str(video.title))

while True:
    option = int(raw_input("\n[+] Enter 0 for audio or 1 for video:\n"))
    if option == 0 or option == 1:
        break
    print("[+] Invalid option")

if option == 0:
    print("[+] Getting the best quality audio")
    bestaudio = video.getbestaudio()
    
    print("[+] Downloading...")
    bestaudio.download(quiet=False)
    

if option == 1:
    print("[+] Getting the best quality video")
    bestvideo = video.getbest()
    
    print("[+] Downloading at " + bestvideo.resolution + " " + bestvideo.extension)
    bestvideo.download(quiet=False)


print("\n[+] Video downloaded!")
