import os

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "ui_path": os.path.join(os.path.dirname(__file__), "ui"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "distri_apps": os.path.join(os.path.dirname(__file__), "distri_apps"),
    "debug": False,
    "gzip": True,
    "autoescape": None,
}
