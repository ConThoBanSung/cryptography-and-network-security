## Symmetric Encryption

**How it Works:**

One shared key is used for both encryption and decryption.

*   **Sender:** Encrypts plaintext into ciphertext using the shared key.
*   **Receiver:** Decrypts ciphertext back to plaintext using the same key.

**Example Algorithm:** AES (Advanced Encryption Standard)

**AES Process:**

*   **Input:**
    *   Plaintext: "Hello, World!"
    *   Key: `00112233445566778899AABBCCDDEEFF` (128-bit key)
*   **Step-by-Step AES Encryption:**
    1.  Divide the Plaintext into 128-bit blocks (if shorter, pad the data). "Hello, World!" → "Hello, World!____" (padded with underscores).
    2.  **Initial Round:** Apply the AddRoundKey operation (XOR the data with the encryption key).
    3.  **Rounds:** For each round (10 rounds for 128-bit key):
        *   SubBytes: Substitute each byte with values from an S-Box (substitution table).
        *   ShiftRows: Shift the rows of the block to the left.
        *   MixColumns: Mix bytes in each column to ensure diffusion.
        *   AddRoundKey: XOR with a round key derived from the main encryption key.
    4.  **Final Round:** No MixColumns in the final round. Only SubBytes, ShiftRows, and AddRoundKey.
*   **Output:** Encrypted ciphertext: A 128-bit (16-byte) block like `5ad4f4d43e9dcd0c9bfcdb9d1b08df55`.
*   **Decryption:** The receiver uses the same key and the inverse of each operation to retrieve the original plaintext.

**Use Case:** Encrypting sensitive data, like credit card numbers, during online transactions.

## Asymmetric Encryption

**How it Works:**

Uses a pair of keys:

*   Public Key for encryption.
*   Private Key for decryption.

Only the holder of the private key can decrypt data encrypted with the public key.

**Example Algorithm:** RSA (Rivest–Shamir–Adleman)

**RSA Process:**

*   **Input:**
    *   Plaintext message: M = 123 (in numerical form).
    *   Public key: (n, e) where n is the modulus and e is the public exponent.
    *   Private key: (n, d) where n is the modulus and d is the private exponent.
*   **Key Generation:**
    *   Generate two large prime numbers p = 61, q = 53.
    *   Calculate n = p * q = 61 * 53 = 3233.
    *   Compute φ(n) = (p - 1)(q - 1) = 60 * 52 = 3120.
    *   Choose a public exponent e = 17 (such that 1 < e < 3120 and gcd(e, φ(n)) = 1).
    *   Compute private exponent d = 2753 (d * e ≡ 1 (mod 3120)).
*   **Encryption:**
    *   Formula: C = M^e mod n.
    *   Encrypt the message: C = 123^17 mod 3233 = 855.
*   **Decryption:**
    *   Formula: M = C^d mod n.
    *   Decrypt the ciphertext: M = 855^2753 mod 3233 = 123.
*   **Output:**
    *   Encrypted ciphertext: 855.
    *   Decrypted message: 123.

**Use Case:** Secure key exchange in protocols like SSL/TLS (e.g., HTTPS).

## Hashing

**How it Works:**

Hashing converts an input into a fixed-length output, called a hash. The process is one-way, meaning you cannot reverse-engineer the original input from the hash. Hashing is commonly used for data integrity. If the input changes, the hash will change significantly.

**Example Algorithm:** SHA-256 (Secure Hash Algorithm)

**SHA-256 Process:**

*   **Input:** "Hello, World!" (plaintext).
*   **Step 1:** Break the Input into 512-bit blocks. "Hello, World!" → "Hello, World!" (padded to 512 bits).
*   **Step 2:** Compression Function: SHA-256 uses a series of rounds (64 rounds in total) involving bitwise operations like XOR, AND, and rotations.
*   **Output:** The output is a fixed 256-bit (32-byte) hash. For "Hello, World!", the SHA-256 hash would be: `315f5bdb76d0787f3f7d9a5c2a9fdf5b4c8e2f4f87bcdc8a8d2fdc0c26a593cb`

**Use Case:** Verifying file integrity during downloads or preventing data tampering.

## Digital Signatures

**How it Works:**

*   Create a Hash of the message.
*   Sign the hash using the sender's private key to create the digital signature.
*   Verify the signature using the sender's public key and check the hash. If the hashes match, the message's authenticity and integrity are verified.

**Example Workflow:**

*   **Input:**
    *   Message: "Contract Agreement".
    *   Private key of sender: d = 2753.
*   **Step 1:** Create the Hash: Hash the message: SHA-256("Contract Agreement").
*   **Step 2:** Encrypt the Hash with the sender's private key. Signature = Hash(M) ^ d mod n.
*   **Step 3:** Recipient Verifies: Hash the received message and compare it with the decrypted signature.

**Use Case:** Signing digital contracts or software to verify authenticity.

## Security Protocols, Events, and Incident Responses

### Security Protocols

**SSL/TLS Workflow:**

*   **ClientHello:** Client sends supported encryption methods.
*   **ServerHello:** Server sends its certificate with public key.
*   **Key Exchange:** Client generates a session key, encrypts it with the server's public key, and sends it.
*   **Decryption:** Server decrypts the session key and establishes an encrypted session.

**Example Use Case:** Securing HTTPS communication between a browser and a server.

### Security Events and Monitoring

**SIEM Example Workflow:**

*   Collect log data from servers and firewalls.
*   Parse, index, and analyze logs in real-time.
*   Generate alerts based on predefined conditions, such as repeated failed logins.

### Incident Response

**DDoS Attack Workflow:**

*   **Detection:** Cloudflare detects traffic anomalies.
*   **Containment:** Redirect traffic through a Web Application Firewall (WAF).
*   **Eradication:** Block IP addresses generating malicious traffic.
*   **Recovery:** Scale back services after the attack subsides.
*   **Post-Incident Review:** Analyze logs to strengthen future defenses.
