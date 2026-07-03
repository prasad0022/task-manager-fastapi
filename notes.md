# FastAPI - Commands Reference

## 1. Create Project

```bash
mkdir fastapi-crud
cd fastapi-crud
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Git Bash

```bash
source venv/Scripts/activate
```

or

```bash
. venv/Scripts/activate
```

### PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### Command Prompt

```cmd
venv\Scripts\activate.bat
```

---

## 4. Deactivate Virtual Environment

```bash
deactivate
```

---

## 5. Install Packages

```bash
python -m pip install fastapi uvicorn
```

---

## 6. Verify Installed Packages

```bash
python -m pip show fastapi
python -m pip show uvicorn
```

---

## 7. Run FastAPI Development Server

```bash
python -m uvicorn app.main:app --reload
```

If your file is named `app.py`:

```bash
python -m uvicorn app.app:app --reload
```

## 8. Alembic

```bash
alembic revision --autogenerate -m "add description column"
alembic upgrade head
```
