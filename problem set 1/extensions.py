file = input("File name: ").strip().lower()

media_types = {
    ".gif":  "image/gif",
    ".jpg":  "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png":  "image/png",
    ".pdf":  "application/pdf",
    ".txt":  "text/plain",
    ".zip":  "application/zip",
}

ext = "." + file.rsplit(".", 1)[-1] if "." in file else ""

print(media_types.get(ext, "application/octet-stream"))
