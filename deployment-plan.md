# Deployment Plan: Navi Mutual Fund Chatbot

This project is fully designed to be deployed using modern serverless and PaaS platforms.
- **Backend**: Railway (FastAPI app running on Python)
- **Frontend**: Vercel (Vite + React SPA)

---

## Part 1: Deploying the Backend on Railway

Railway natively supports Python apps out of the box and requires almost zero configuration.

### Prerequisites
1. Create a free account on [Railway.app](https://railway.app/).
2. Link your GitHub account to Railway.

### Deployment Steps
1. Click **New Project** from the Railway dashboard.
2. Select **Deploy from GitHub repo**.
3. Select this repository (`Mutual-fund-chatbot-Nextleap`).
4. Railway will automatically detect that this is a Python project (via `requirements.txt`).
5. **Set Environment Variables**:
   Go to the "Variables" tab for your newly created backend service in Railway and add the following:
   - `GOOGLE_API_KEY`: *(Paste your Gemini API key here)*
   - `EMBEDDING_MODEL`: `models/gemini-embedding-2`
   - `EMBEDDING_DIMENSIONS`: `384`
   - `PORT`: `8000` (Railway injects `$PORT`, but you can explicitly specify it)

### Customizing the Start Command (If needed)
If Railway fails to auto-detect the FastAPI startup command, go to **Settings > Deploy > Start Command** and set it to:
```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

### Get your Backend URL
Once deployed successfully, go to the **Settings > Environment > Domains** section. 
Click **Generate Domain**. You will receive a URL that looks like `https://mutual-fund-backend-production.up.railway.app`. 
**Copy this URL**, you will need it for the frontend!

---

## Part 2: Deploying the Frontend on Vercel

Vercel is perfectly tailored for Vite + React applications.

### Prerequisites
1. Create a free account on [Vercel.com](https://vercel.com/).
2. Link your GitHub account.

### Deployment Steps
1. In Vercel, click **Add New...** > **Project**.
2. Select your `Mutual-fund-chatbot-Nextleap` repository and click **Import**.
3. **Important Configuration**:
   - **Project Name**: `navi-mutual-fund-bot`
   - **Framework Preset**: Select `Vite` (Vercel usually auto-detects this).
   - **Root Directory**: **Click "Edit" and type `frontend`** (Because our React app is inside the `frontend/` folder, not the root of the repo).
   
4. **Environment Variables**:
   In the Environment Variables section, add a new variable so the React app knows where your Railway backend is hosted:
   - **Name**: `VITE_API_URL`
   - **Value**: `https://<YOUR-RAILWAY-DOMAIN>` *(Paste the domain you got from Railway in Part 1. Do NOT include `/api` at the end)*.

5. Click **Deploy**.

---

## Part 3: Architecture and CI/CD Note

Once both are deployed:
- Your Vercel app will connect securely over HTTPS to your Railway backend via CORS.
- Since we already set up a GitHub Action (`scheduler.yml`), the data scraping and ChromaDB updates will happen entirely in the cloud. Every night, GitHub will commit the new vector store back to the `master` branch.
- **Auto-Deployments:** Whenever the GitHub Action pushes new vector data to the `master` branch, **Railway will automatically pull the new data and restart the backend server**, meaning your chatbot will stay completely up to date with zero manual intervention!
