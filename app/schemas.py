from pydantic import BaseModel

class PartnerBase(BaseModel):
    name: str
    address: str

class PartnerCreate(PartnerBase):
    pass

class Partner(PartnerBase):
    id: int

    class Config:
        # Substitua orm_mode por from_attributes
        from_attributes = True
