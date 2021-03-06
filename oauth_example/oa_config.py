# -*- coding: utf-8 -*-

baseurl = "https://localhost"
#baseurl = "https://lingon.ladok.umu.se"
issuer = "%s:%%d" % baseurl
# keys = {
#     "rsa": {
#         "key": "oc_keys/key.pem",
#         "usage": ["enc", "sig"]
#     }
# }

# ..... If you want to use CAS authentication ....
#AUTHN = "CasAuthnMethod"
CAS_SERVER = "https://cas.umu.se"
SERVICE_URL = "%s/verify" % issuer

# ..... Otherwise
AUTHN = "Simple"

COOKIENAME= 'pyoic'
COOKIETTL = 4*60 # 4 hours
SYM_KEY = "SoLittleTime,GotToHurry"
SERVER_CERT = "certs/server.crt"
SERVER_KEY = "certs/server.key"
#CERT_CHAIN="certs/chain.pem"
CERT_CHAIN = None

# =======  SIMPLE DATABASE ==============

USERDB = {
    "diana": {
        "user_id": "dikr0001",
        "name": "Diana Krall",
        "given_name": "Diana",
        "family_name": "Krall",
        "nickname": "Dina",
        "email": "diana@example.org",
        "email_verified": False,
        "phone_number": "+46 90 7865000",
        "address": {
            "street_address": "Umeå Universitet",
            "locality": "Umeå",
            "postal_code": "SE-90187",
            "country": "Sweden"
        },
    },
    "babs": {
        "user_id": "babs0001",
        "name": "Barbara J Jensen",
        "given_name": "Barbara",
        "family_name": "Jensen",
        "nickname": "babs",
        "email": "babs@example.com",
        "email_verified": True,
        "address": {
            "street_address": "100 Universal City Plaza",
            "locality": "Hollywood",
            "region": "CA",
            "postal_code": "91608",
            "country": "USA",
        },
    },
    "upper": {
        "user_id": "uppe0001",
        "name": "Upper Crust",
        "given_name": "Upper",
        "family_name": "Crust",
        "email": "uc@example.com",
        "email_verified": True,
    }
}

DISTDB = USERDB.copy()

# ============= LDAP ==============

LDAP = {
    "uri": "ldaps://ldap.umu.se",
    "base": "dc=umu, dc=se",
    "filter_pattern": "(uid=%s)",
    "user": "",
    "passwd": "",
    "attr": ["eduPersonScopedAffiliation", "eduPersonAffiliation"],
}

LDAP_EXTRAVALIDATION = {
    "verifyAttr": "eduPersonAffiliation",
    "verifyAttrValid": ['employee', 'staff', 'student']
}

#USERINFO = "LDAP"
USERINFO = "SIMPLE"
