#
# Usage: python3 get_pem_pubkey.py <asymmetric-key-alias>
#

import binascii
import boto3
import sys

start_string = '-----BEGIN PUBLIC KEY-----'
end_string = '-----END PUBLIC KEY-----'

client = boto3.client('kms')
response = client.get_public_key(KeyId='alias/' + sys.argv[1])
pub_key = binascii.b2a_base64(response['PublicKey']).decode()

out = start_string
for i in range(0, len(pub_key), 64):
    out += '\n' + pub_key[i:i+64]
out += end_string + '\n'

with open(sys.argv[1] + '.pub.der', 'wb') as f:
    f.write(response['PublicKey'])

with open(sys.argv[1] + '.pub.pem', 'w') as f:
    f.write(out)
