from pydantic import BaseModel, Field
from typing import List, Optional

class SGOfficers(BaseModel):
    position: str
    name: str
    address: str
    appointment_date: str
    identification_number: str
    nationality: str

class SGShareholders(BaseModel):
    name: str
    address: str
    identification_number: str
    nationality: str
    number_shares: int
    currency: str
    address_changed: str

class SGBusinessActivities(BaseModel):
    type: str
    code: str

class SGCompany(BaseModel):
    """Data model for SG company"""
    name: str
    former_name: Optional[str]
    uen: str
    incorporation_date: str
    status: str
    company_type: str
    status_date: str
    registered_addresses: str
    address_date: str
    last_agm_date: str
    last_ar_date: str
    primary_activity: SGBusinessActivities
    secondary_activity: SGBusinessActivities
    officers: List[SGOfficers]
    shareholders: List[SGShareholders]