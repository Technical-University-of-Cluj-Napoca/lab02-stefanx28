import os
import datetime

def smart_log(*args, **kwargs)-> None:
    
    if kwargs.get("info"):
        level = "INFO"
        color = "\033[94m"
    elif kwargs.get("debug"):
        level = "DEBUG"
        colour = "\033[90m"
    elif kwargs.get("warning"):
        level = "WARNING"
        colour = "\033[93m"
    elif kwargs.get("error"):
        level = "ERROR"
        colour = "\033[91m"

    now = datetime.now()
    prefix_parts = []

    show_timestamp = kwargs.get("timestamp", True)
    show_date = kwargs.get("date", True)

    if show_timestamp:
        if show_date:
            prefix_parts.append(now.strftime("%Y-%m-%d "))
        prefix_parts.append(now.strftime("%H:%M:%S"))

    if prefix_parts:
        time_str = "[" + " ".join(prefix_parts).strip() + "] "
    else:
        time_str = ""

    message_parts = [f"{msg}" for msg in args]
    message = " ".join(message_parts)
    reset = "\033[0m"
    line = f"{time_str}\033[1m[{level}]\033[0m {colour}{message}{reset}"
    print(line)
    pass


    if __name__ == "__main__":
        smart_log("Sys", level="info", timestamp=True)