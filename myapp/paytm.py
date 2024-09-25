# utils/paytm.py
import base64
import hashlib
import hmac

def generate_checksum(params, merchant_key):
    params = {k: str(v) for k, v in sorted(params.items())}
    data = '|'.join([params[key] for key in sorted(params)])
    return base64.b64encode(hmac.new(merchant_key.encode(), data.encode(), hashlib.sha256).digest()).decode()

def verify_checksum(params, merchant_key, checksum):
    params = {k: str(v) for k, v in sorted(params.items()) if k != 'CHECKSUMHASH'}
    data = '|'.join([params[key] for key in sorted(params)])
    generated_checksum = base64.b64encode(hmac.new(merchant_key.encode(), data.encode(), hashlib.sha256).digest()).decode()
    return generated_checksum == checksum
