def main():
    file_name = input("File name: ").strip().lower()
    format = extension(file_name)
    print(format)


def extension(fn):
    if fn.endswith(".gif"):
        return "image/gif"
    elif fn.endswith(".jpg") or fn.endswith(".jpeg"):
        return "image/jpeg"
    elif fn.endswith(".png"):
        return "image/png"
    elif fn.endswith(".pdf"):
        return "application/pdf"
    elif fn.endswith(".txt"):
        return "text/plain"
    elif fn.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


main()
