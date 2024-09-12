# import time

from django.http import HttpRequest, JsonResponse
from ninja import Router

# import plaid
# from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
# from plaid.model.transactions_sync_request import TransactionsSyncRequest
# from plaid.model.products import Products
# from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
# from plaid.model.auth_get_request import AuthGetRequest
# from plaid.model.institutions_get_by_id_request import InstitutionsGetByIdRequest
# from plaid.model.country_code import CountryCode
# from plaid.model.link_token_create_request import LinkTokenCreateRequest
# from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser

# from plugins.plaid import client
# from plaids.models import Plaid
from plaids.schemas import (
    ItemIDSchema,
    TransactionResponseSchema,
    LinkTokenResponseSchema,
    SPTCRequestSchema,
    InstitutionResponseSchema,
    AuthResponseSchema,
)

from util.plaid_utils import filter_transactions
from util.schemas import Token, Message

router = Router(tags=['plaid'])

@router.post('/create_link_token', response={200: LinkTokenResponseSchema, frozenset({401, 404, 500}): Message})
def create_link_token(request: HttpRequest):
    pass # This code is private

@router.post('/sandbox_public_token', response={200: Token, frozenset({401, 404, 500}): Message})
def sandbox_public_token(request: HttpRequest, creds: SPTCRequestSchema):
    pass # This code is private
        

@router.post('/gen_access_token', response={200: ItemIDSchema, frozenset({401, 404, 500}): Message})
def gen_access_token(request: HttpRequest, public_token: Token):
    pass # This code is private
    
@router.get('/institutions/{ins_id}', response={200: InstitutionResponseSchema, frozenset({401, 404, 500}): Message})
def get_institution(request: HttpRequest, ins_id: str):
    pass # This code is private

@router.get('/auth', response={200: AuthResponseSchema, frozenset({401, 404, 500}): Message})
def get_auth(request: HttpRequest):
    pass # This code is private
    
@router.get('/items', response={200: list[ItemIDSchema], frozenset({401, 404}): Message})
def get_items(request: HttpRequest):
    pass # This code is private

@router.delete('/items', response={200: tuple[int, dict], frozenset({401, 404}): Message})
def delete_items(request: HttpRequest, item_id: ItemIDSchema):
    pass # This code is private

@router.get('/transactions', response={200: TransactionResponseSchema, frozenset({401, 404, 500}): Message})
def get_transactions(request: HttpRequest):
    pass # This code is private