# Deploy (Python)
Needs Python 3.10+ and any host that runs Python (VPS, Render, Railway, PythonAnywhere...).
1. Upload the whole project (keep `frontend/` and `backend/` side by side; skip `venv`, `data`, `.env`).
2. In `backend/`: `pip install -r requirements.txt`
3. Set environment variables on the host (or a `.env` file): `HOST=0.0.0.0`, `PORT`, `SITE_URL=https://your-domain`, `WHATSAPP_NUMBER`, `ANTHROPIC_API_KEY`. Set `TRUST_PROXY=1` only if the host puts one reverse proxy in front (so rate limits see real visitor IPs).
4. From `backend/`, start with `python app.py` (uses waitress, a production server). Serve it over HTTPS (host-managed, or Nginx/Caddy with Let's Encrypt).
5. Google Search Console: add your domain, submit `https://your-domain/sitemap.xml`.
6. Back up `data/ghazal.db` (reservations). Keep packages updated: `pip install -U -r requirements.txt` and `pip list --outdated`.
## Notes
- WhatsApp button, footer link and reservation-to-WhatsApp appear only when `WHATSAPP_NUMBER` is set; the chat bubble only when `ANTHROPIC_API_KEY` is set.
- Rate limits are kept in memory (one server process); fine for one restaurant site.
- The chat only knows the address, hours and the menu in `frontend/js/menu-data.js`.
