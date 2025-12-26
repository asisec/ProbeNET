import requests
import os
from django.shortcuts import render
from .models import DomainData, DomainEntity
from dateutil import parser


def index(request):
    context = {}

    if request.method == "POST":
        domain_input = request.POST.get("domain")

        api_url = os.getenv("SCANNER_URL", "http://localhost:8000/scan")

        try:
            response = requests.post(api_url, json={"domain": domain_input}, timeout=15)
            api_data = response.json()

            def parse_dt(date_str):
                if not date_str: return None
                try:
                    return parser.parse(date_str)
                except:
                    return None

            domain_data = DomainData(
                domain_name=api_data.get("domain_name"),
                registrar=api_data.get("registrar"),
                whois_server=api_data.get("whois_server"),
                creation_date=parse_dt(api_data.get("creation_date")),
                expiration_date=parse_dt(api_data.get("expiration_date")),
                name_servers=api_data.get("name_servers", []),
                status=api_data.get("status", []),
                emails=api_data.get("emails", [])
            )

            entity = DomainEntity(domain_data)

            context = {
                "entity": entity,
                "raw_data": api_data
            }

        except Exception as e:
            context = {"error": f"Connection error: {str(e)}"}

    return render(request, 'index.html', context)