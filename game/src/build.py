"""Builds game/index.html (standalone page) from game/src/game.html + game/src/face.jpg."""
import base64, pathlib, sys
src = pathlib.Path(__file__).parent
body = (src / "game.html").read_text(encoding="utf-8")
face = base64.b64encode((src / "face.jpg").read_bytes()).decode()
body = body.replace("__FACE__", face)
page = ('<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">\n'
        '<meta name="theme-color" content="#0e1220">\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')
(src.parent / "index.html").write_text(page, encoding="utf-8")
if len(sys.argv) > 1:  # optional: body-only copy for embedding
    pathlib.Path(sys.argv[1]).write_text(body, encoding="utf-8")
print("ok")
