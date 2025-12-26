from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import socket
import whois  # python-whois kütüphanesi
from typing import List, Optional

app = FastAPI()


class DomainRequest(BaseModel):
    domain: str


class ScanResult(BaseModel):
    domain_name: str
    ip_address: Optional[str] = None
    registrar: Optional[str] = None
    whois_server: Optional[str] = None
    creation_date: Optional[str] = None
    expiration_date: Optional[str] = None
    name_servers: List[str] = []
    status: List[str] = []
    emails: List[str] = []
    open_ports: List[int] = []


def check_port(ip: str, port: int) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            return s.connect_ex((ip, port)) == 0
    except:
        return False


@app.post("/scan", response_model=ScanResult)
async def scan_domain(request: DomainRequest):
    domain = request.domain
    response_data = {"domain_name": domain}

    try:
        try:
            ip = socket.gethostbyname(domain)
            response_data["ip_address"] = ip

            open_ports = []
            for port in [80, 443, 21, 22]:
                if check_port(ip, port):
                    open_ports.append(port)
            response_data["open_ports"] = open_ports
        except:
            response_data["ip_address"] = None

        w = whois.whois(domain)

        def parse_date(date_obj):
            if isinstance(date_obj, list):
                return str(date_obj[0]) if date_obj else None
            return str(date_obj) if date_obj else None

        response_data.update({
            "registrar": w.registrar,
            "whois_server": w.whois_server,
            "creation_date": parse_date(w.creation_date),
            "expiration_date": parse_date(w.expiration_date),
            "name_servers": w.name_servers if w.name_servers else [],
            "status": w.status if isinstance(w.status, list) else [w.status] if w.status else [],
            "emails": w.emails if isinstance(w.emails, list) else [w.emails] if w.emails else []
        })

        return response_data

    except Exception as e:
        print(f"Error: {e}")
        return response_data