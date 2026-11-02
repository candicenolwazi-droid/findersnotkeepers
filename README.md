# FindersNotKeepers — Lost & Found Web App

A lost-and-found platform where people can post lost or found items, browse listings and contact each other to return belongings. Built as the group project for **EPE 321: Software Engineering** (University of Pretoria, 2025) by Group 10.

This is a cleaned showcase copy of the group's codebase. Passwords, API keys, `.env` files, database files, user uploads, installed dependencies and personal details have been removed or replaced with placeholders such as `CHANGE_ME` and `YOUR_...`.

## My contribution

I worked mainly on the **Flask backend API** (`Backend_api`, `Backend_api_new`, `API_CORE_FRONTEND/Backend_api`):

- REST API routes organised into Flask blueprints
- JWT authentication, user roles and password reset
- Audit and report logging
- API and unit tests (`test_run.py`, `test_roles.py`, `unit_tests.py`)

## Project structure

| Folder | What it is |
| --- | --- |
| `LiveSite/` | Final React + Vite front end (listings, login/sign-up incl. Google sign-in, admin page) |
| `LiveBackend/` | Final Flask API used by the deployed site |
| `Server/` | Node.js service, including email notifications |
| `AI/` | AI chatbot assistant (LangChain + OpenAI) that answers questions about the site |
| `Networking/` | Networking module and its tests |
| `Backend_api/`, `Backend_api_new/`, `Backend_temp/`, `Backend core/`, `API_CORE_FRONTEND/` | Earlier iterations of the backend and front end kept for history |

Deployment notes: [`RENDER_DEPLOYMENT.md`](RENDER_DEPLOYMENT.md), [`GOOGLE_AUTH_SETUP.md`](GOOGLE_AUTH_SETUP.md), [`ADMIN_PAGE_GUIDE.md`](ADMIN_PAGE_GUIDE.md).

## Running locally

Configuration comes from environment variables. Copy the examples and fill in your own values:

```bash
cp LiveSite/.env.example LiveSite/.env
cp Server/.env.example Server/.env
```

Front end:

```bash
cd LiveSite
npm install
npm run dev
```

Backend:

```bash
cd LiveBackend
python -m venv venv
venv/Scripts/activate   # on macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Team

Group 10, EPE 321 (2025). Thanks to all my teammates, including [@TadiK26](https://github.com/TadiK26), [@calemchetty](https://github.com/calemchetty), [@CidraHanni](https://github.com/CidraHanni), [@MrSobble](https://github.com/MrSobble) and [@bokaisfuture](https://github.com/bokaisfuture).
