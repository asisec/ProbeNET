from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class DomainData:
    domain_name: str
    registrar: Optional[str] = None
    whois_server: Optional[str] = None
    creation_date: Optional[datetime] = None
    expiration_date: Optional[datetime] = None
    updated_date: Optional[datetime] = None
    name_servers: List[str] = field(default_factory=list)
    status: List[str] = field(default_factory=list)
    emails: List[str] = field(default_factory=list)
    dnssec: Optional[str] = None

class DomainEntity:
    def __init__(self, data: DomainData):
        self._data = data

    @property
    def domain_name(self) -> str:
        return self._data.domain_name

    @property
    def registrar_info(self) -> str:
        return self._data.registrar or "Unknown Registrar"

    @property
    def is_privacy_protected(self) -> bool:
        privacy_keywords = ['privacy', 'redacted', 'guard', 'proxy', 'protect']
        raw_text = str(self._data).lower()
        return any(keyword in raw_text for keyword in privacy_keywords)

    @property
    def days_active(self) -> int:
        if not self._data.creation_date:
            return 0
        delta = datetime.now() - self._data.creation_date
        return delta.days

    @property
    def is_fresh(self) -> bool:
        return self.days_active < 90

    @property
    def risk_score(self) -> int:
        score = 0
        if self.is_fresh:
            score += 50
        if self.is_privacy_protected:
            score += 20
        if not self._data.name_servers:
            score += 30
        return score

    def to_dict(self) -> dict:
        return {
            "domain": self.domain_name,
            "registrar": self.registrar_info,
            "creation_date": self._data.creation_date,
            "expiration_date": self._data.expiration_date,
            "age_days": self.days_active,
            "is_fresh": self.is_fresh,
            "privacy": self.is_privacy_protected,
            "risk_score": self.risk_score,
            "name_servers": self._data.name_servers,
            "status": self._data.status
        }
