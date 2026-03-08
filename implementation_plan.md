# Start Server Plan

The goal is to start the backend server, which will also host the frontend.

## Proposed Changes

### [Backend]

#### [RUN] Start Server
Navigate to `student-risk-dashboard\backend` and run the FastAPI server using `uvicorn`.

```powershell
cd student-risk-dashboard\backend
.\venv\Scripts\activate
uvicorn main:app --reload
```

## Verification Plan

### Automated Tests
- Ping the `/api/ping` endpoint to ensure the server is responding.
- Access the root URL `/` to ensure the frontend is being served.

### Manual Verification
- Open the browser to `http://127.0.0.1:8000` and check if the dashboard loads.
