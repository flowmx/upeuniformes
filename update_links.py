import re

# Update index.html
with open('c:/Users/angel/upe-unifomres-mx/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace links targeting `catalogo`
text = re.sub(r"mostrarVistaPrincipalYScroll\('catalogo',\s*'([^']+)'\)", r"window.location.href='catalogo.html?cat=\1'", text)
text = re.sub(r"mostrarVistaPrincipalYScroll\('catalogo'\)", r"window.location.href='catalogo.html'", text)
text = re.sub(r"manejarMenuMovil\('catalogo',\s*'([^']+)'\)", r"window.location.href='catalogo.html?cat=\1'", text)
text = re.sub(r"manejarMenuMovil\('catalogo'\)", r"window.location.href='catalogo.html'", text)

with open('c:/Users/angel/upe-unifomres-mx/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

# Update catalogo.html
with open('c:/Users/angel/upe-unifomres-mx/catalogo.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make home links go to index.html
text = re.sub(r"mostrarVistaPrincipalYScroll\('inicio'\)", r"window.location.href='index.html'", text)
text = re.sub(r"mostrarVistaPrincipalYScroll\('servicios'\)", r"window.location.href='index.html#servicios'", text)
text = re.sub(r"mostrarVistaPrincipalYScroll\('contacto'\)", r"window.location.href='index.html#contacto'", text)
text = re.sub(r"mostrarVistaPrincipal\(\)", r"window.location.href='index.html'", text)

# For catalog links, just call the filter function directly
text = re.sub(r"mostrarVistaPrincipalYScroll\('catalogo',\s*'([^']+)'\)", r"filtrarCatalogo('\1')", text)
text = re.sub(r"mostrarVistaPrincipalYScroll\('catalogo'\)", r"filtrarCatalogo('todos')", text)

# Mobile menu replacements
text = re.sub(r"manejarMenuMovil\('inicio'\)", r"window.location.href='index.html'", text)
text = re.sub(r"manejarMenuMovil\('servicios'\)", r"window.location.href='index.html#servicios'", text)
text = re.sub(r"manejarMenuMovil\('contacto'\)", r"window.location.href='index.html#contacto'", text)
text = re.sub(r"manejarMenuMovil\('catalogo',\s*'([^']+)'\)", r"filtrarCatalogo('\1'); document.getElementById('mobile-menu').classList.add('hidden');", text)
text = re.sub(r"manejarMenuMovil\('catalogo'\)", r"filtrarCatalogo('todos'); document.getElementById('mobile-menu').classList.add('hidden');", text)

with open('c:/Users/angel/upe-unifomres-mx/catalogo.html', 'w', encoding='utf-8') as f:
    f.write(text)
