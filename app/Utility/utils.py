from datetime import datetime
import shutil

# TODO: make it use color_text instead of fixed vals
# from .kivy_markup_helper import color_text


# utility functions
def write_crash(e: Exception):
    index = datetime.today()
    error = f"[b][color=#fa0000][ {index} ]:[/color][/b]\n(\n\n{e}\n\n)\n"
    try:
        with open("crashdump.txt", "a") as file:
            file.write(error)
    except:
        with open("crashdump.txt", "w") as file:
            file.write(error)
    return index


def move_file(source_path, dest_path):
    try:
        path = shutil.move(source_path, dest_path)
        return (1, path)
    except Exception as e:
        return (0, e)
