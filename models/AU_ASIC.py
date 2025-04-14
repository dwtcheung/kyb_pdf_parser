from pydantic import BaseModel, Field
from typing import List, Optional

class AUAddress(BaseModel):
    address: str
    start_date: str
    type: str
    status: str
    document_number: str

class AUOfficeholders(BaseModel):
    role: str
    name: str
    address: str
    born: Optional[str]
    appointment_date: str
    abn: Optional [str]
    acn: Optional [str]
    document_number: str

class AUHoldingCompany(BaseModel):
    name: str
    acn: str
    abn: str
    document_number: str

class AUOtherRoles(BaseModel):
    role: str
    name: str
    address: str
    start_date: str
    abn: Optional [str]
    acn: Optional [str]
    document_number: str

class AUShareStructure(BaseModel):
    class_code: str
    description: str
    number_issued: int
    total_amount_paid: float
    total_amount_unpaid: float
    document_number: str

class AUShareMembers(BaseModel):
    name: str
    address: str
    acn: Optional[str]
    abn: Optional[str]
    class_code: str
    number_held: int
    beneficially_held: str
    paid: str
    document_number: str


class AUShare(BaseModel):
    current_share_structure: List[AUShareStructure]
    previous_share_structure: Optional[List[AUShareStructure]]
    current_members: List[AUShareMembers]
    previous_members: Optional[List[AUShareMembers]]

class AUAuditor(BaseModel):
    name: str
    type: str
    role: str
    address: str
    appointment_date: str
    court_no: str

class AUCompany(BaseModel):
    """Data model for AU company"""
    name: str
    acn: str
    abn: str
    registered_in: str
    registration_date: str
    next_review_date: str
    name_start_date: str
    previous_state_number: Optional[str]
    status: str
    company_type: str
    company_class: str
    company_subclass: str
    current_address: List[AUAddress]
    previous_address: Optional[AUAddress]
    contact_address: Optional[AUAddress]
    #addresses: List[AUAddress]
    directors: List[AUOfficeholders]
    secretaries: List[AUOfficeholders]
    appointed_auditor: AUOtherRoles
    external_auditor: AUAuditor
    ultimate_holding_company: AUHoldingCompany
    current_share_structure: List[AUShareStructure]
    previous_share_structure: Optional[List[AUShareStructure]]
    members: List[AUShareMembers]
    previous_members: Optional[List[AUShareMembers]]