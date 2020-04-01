# Generate and wrap AES-256 keys to import into KMS
1. Create AES-256 Key
    openssl rand -out PlaintextKeyMaterial.bin 32

2. Wrap keys using openssl (using MacOs)

/usr/local/Cellar/openssl/1.0.2s/bin/openssl pkeyutl -encrypt \
    -in PlaintextKeyMaterial.bin \
    -out EncryptedKeyMaterial.bin \
    -pubin -inkey wrappingKey_7eea1e6b-f074-4055-8916-8a8abdbef53a_09261813 \
    -keyform DER \
    -pkeyopt rsa_padding_mode:oaep \
    -pkeyopt rsa_oaep_md:sha256
