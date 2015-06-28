import os

def file_ext(file_name):
    ext = os.path.splitext(file_name)[-1].lower()

    # Now we can simply use == to check for equality, no need for wildcards.
    if ext == ".py":
        return "python"
    elif ext == ".js":
        return "javascript"
    elif ext == ".java":
        return "java"
    elif ext == ".c":
        return "C"
    elif ext == ".cpp":
        return "c++"
    elif ext == ".rb":
        return "ruby"
    elif ext == ".css":
        return "css"
    else:
        return " "
