"""Build index.html (standalone page for GitHub Pages) from viewer.html.

viewer.html is written as page content without <html>/<head>/<body>, the format
used for the claude.ai artifact. This wraps it into a full HTML document.
"""
import pathlib, re

src = pathlib.Path(__file__).with_name('viewer.html').read_text(encoding='utf-8')
cut = src.index('<div id="app"')
head, body = src[:cut], src[cut:]
head = re.sub(r'<meta (charset|name="viewport")[^>]*>\n?', '', head)

page = f'''<!doctype html>
<html lang="ka">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="დოლაბაური — სამსართულიანი სახლი, 6 ბინა: ინტერაქტიული 3D მოდელი, დიზაინი, განათება, ინჟინერია.">
<meta name="theme-color" content="#16181b">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="დოლაბაური">
<link rel="icon" type="image/png" href="icon-192.png">
<link rel="apple-touch-icon" href="icon-192.png">
<link rel="manifest" href="manifest.webmanifest">
<meta property="og:title" content="დოლაბაური — 3D">
<meta property="og:description" content="სამსართულიანი სახლი, 6 ბინა — ინტერაქტიული 3D მოდელი.">
<meta property="og:image" content="icon-512.png">
{head.strip()}
</head>
<body>
{body.strip()}
</body>
</html>
'''
pathlib.Path(__file__).with_name('index.html').write_text(page, encoding='utf-8')
print('index.html', len(page) // 1024, 'KB')
