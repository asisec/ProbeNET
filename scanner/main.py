from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess

app = FastAPI()


class DomainRequest(BaseModel):
    domain: str


class DomainResponse(BaseModel):
    domain: str
    status: str
    output: str


@app.post("/scan", response_model=DomainResponse)
async def scan_domain(request: DomainRequest):
    try:
        command = ["echo", f"Scanning target: {request.domain}"]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        return DomainResponse(
            domain=request.domain,
            status="success",
            output=result.stdout.strip()
        )

    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e.stderr))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))