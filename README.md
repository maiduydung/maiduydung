## Mai Personal Site

Simple portfolio built with Reflex + Tailwind v4.

### Prerequisites
- Python 3.11
- Node (bundled by Reflex)

### Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

### Run locally
```bash
reflex run
```
App: `http://localhost:3000`

### Notes
- Tailwind is provided via `TailwindV4Plugin` in `rxconfig.py`.
- Public stylesheet is injected via `stylesheets=["/public/output.css"]`.
- Main app code is in `mai_personal_site/mai_personal_site.py`.

### Deploy (Reflex Pro)
Push to your linked repo; Reflex Pro will build using the same config. If styles look off locally, clear caches:
```bash
rm -rf .reflex .web node_modules package-lock.json
reflex run
```


