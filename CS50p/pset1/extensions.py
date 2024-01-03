media = {
    "gif" : "image/gif",
    "jpg" : "image/jpeg",
    "jpeg" : "image/jpeg",
    "png" : "image/png",
    "pdf" : "application/pdf",
    "txt" : "text/plain",
    "zip" : "application/zip"
}

ext = input("File name: ").strip().lower()

if ext.rfind(".") != -1:
    i = int(ext.rindex(".")) + 1
    out = ext[i:]

    if out not in media:
        print ("application/octet-stream")
    else:
        print(media[out])
else:
    print ("application/octet-stream")