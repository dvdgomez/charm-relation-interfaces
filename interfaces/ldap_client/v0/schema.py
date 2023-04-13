"""This file defines the schemas for the provider and requirer sides of the ldap-client interface.

It must expose one interfaces.schema_base.DataBagSchema subclasses called:
- ProviderSchema

Examples:
    ProviderSchema:
        unit: <empty>
        app: {
            "basedn": "dc=glauth,dc=com"
            "ca_cert": "glauth.crt contents"
            "ldap_default_bind_dn": "cn=serviceuser,ou=svcaccts,dc=glauth,dc=com"
            "ldap_password": "mysecret"
            "ldap_uri": "ldaps://jujuabc-123:3894"
        }
"""

from pydantic import BaseModel

from interfaces.schema_base import DataBagSchema


class LdapClientProviderAppData(BaseModel):
    basedn: str # base dn
    ca_cert: str # CA certificate contents.
    ldap_default_bind_dn: str # default bind dn.
    ldap_password: str # ldap password.
    ldap_uri: str # LDAP uri. 


class ProviderSchema(DataBagSchema):
    """Provider Schema for ldap-client."""
    app: LdapClientProviderAppData
