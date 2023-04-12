"""This file defines the schemas for the provider and requirer sides of this relation interface.

It must expose one interfaces.schema_base.DataBagSchema subclasses called:
- ProviderSchema
"""

from pydantic import BaseModel

from interfaces.schema_base import DataBagSchema


class MyProviderAppData(BaseModel):
    basedn: str
    ca_cert: str
    ldap_default_bind_dn: str
    ldap_password: str
    ldap_uri: str


class ProviderSchema(DataBagSchema):
    """The schema for the provider side of this interface."""
    app: MyProviderAppData
