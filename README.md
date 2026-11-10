# GHAZAL Restaurant website (HTML, CSS, JavaScript + Python)

Portuguese (default) and English. Home, menu, reservations (sent to WhatsApp and saved in a database), gallery, Find us, AI chat assistant "Gul".

## Folder structure
```
ghazal-restaurant/
  start.bat / start.sh      run on Windows / Mac-Linux
  README.md, DEPLOY.md
  frontend/                 everything visitors see
    index.html              home, menu, reservation form, find us
    gallery.html            gallery page
    css/style.css           site styles          css/gallery.css  gallery styles
    js/menu-data.js         MENU DATA: edit dishes and prices here
    js/main.js              menu, language switch, reservation form, navigation
    js/gallery.js           gallery grid and lightbox
    js/widget.js            WhatsApp button, Gul chat bubble and welcome pop-up
    img/                    logo and gallery images
  backend/                  Python server
    app.py                  pages, security, reservations, AI chat, sitemap, robots
    requirements.txt        Python packages (Flask, waitress)
    view_reservations.py    shows saved reservations (add --csv for a spreadsheet file)
    .env.example            settings template (copy to backend/.env)
```

## Run on Windows
1. Install Python 3.10 or newer from python.org (tick "Add python.exe to PATH").
2. In the `backend` folder copy `.env.example` to a new file named `.env` and fill in `WHATSAPP_NUMBER` (country code, digits only), `GROQ_API_KEY` (your Groq key from console.groq.com/keys, optional, for the chat bubble) and later `SITE_URL`.
3. Double-click `start.bat` in the main folder, then open http://localhost:3000

Mac/Linux: run `./start.sh`.

## Daily use
- Reservations are saved in `backend/data/ghazal.db`. In the `backend` folder run `python view_reservations.py`.
- Change dishes/prices in `frontend/js/menu-data.js`, then restart the server.
- Add gallery photos to `frontend/img/` and add a line to the `G` list in `frontend/js/gallery.js`.
- Never share or upload `.env` or `data/`.

See DEPLOY.md for hosting.