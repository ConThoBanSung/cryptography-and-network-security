# Cryptography Algorithms and How They Work for Security Purposes

## 1. Symmetric Encryption

### How it Works:
- A single shared key is used for both encryption and decryption.
- The sender encrypts the plaintext using the key, and the ciphertext is sent over the network.
- The receiver uses the same key to decrypt the ciphertext back into plaintext.

### Example Algorithm: AES (Advanced Encryption Standard)
- **Process**:
  1. Divides the plaintext into fixed-size blocks (128 bits by default).
  2. Performs multiple rounds (10, 12, or 14 depending on the key size):
     - **SubBytes**: Replace bytes using a substitution table (S-box).
     - **ShiftRows**: Shift rows in the block to the left.
     - **MixColumns**: Combine bytes within columns for diffusion.
     - **AddRoundKey**: XOR the data with the encryption key.

### Use Case:
- Encrypting sensitive data, like credit card numbers during online transactions.


## 2. Asymmetric Encryption

### How it Works:
- A key pair (public key and private key) is generated.
- The public key is used to encrypt data, and the private key is used to decrypt it.
- Only the owner of the private key can decrypt the data encrypted with the public key.

### Example Algorithm: RSA (Rivest–Shamir–Adleman)

**Process:**
1. Generate two large prime numbers \( p \) and \( q \), then compute \( n = p \times q \).
2. Compute \( \phi(n) = (p - 1) \times (q - 1) \).
3. Choose a public key exponent \( e \) such that \( 1 < e < \phi(n) \) and \( e \) is co-prime to \( \phi(n) \).
4. Compute the private key \( d \) where \( (d \times e) \mod \phi(n) = 1 \).
5. **Encryption:** \( C = M^e \mod n \).
6. **Decryption:** \( M = C^d \mod n \).

### Use Case:
- Securely exchanging keys in SSL/TLS (e.g., HTTPS).

---

## 3. Hashing

### How it Works:
- Hashing takes an input and converts it into a fixed-length output (hash).
- The process is **one-way**; you cannot derive the original input from the hash.
- Hashing ensures data integrity, as any change in the input results in a completely different hash.

### Example Algorithm: SHA-256

**Process:**
1. Breaks the input into 512-bit blocks.
2. Applies compression functions to produce a fixed 256-bit output.

### Use Case:
- Verifying the integrity of downloaded files.

---

## 4. Digital Signatures

### How it Works:
1. A hash of the data is created.
2. The hash is encrypted using the sender's private key to create the digital signature.
3. The recipient decrypts the signature using the sender’s public key and compares the hash with the received data.
4. If the hashes match, the data’s authenticity and integrity are verified.

### Use Case:
- Signing contracts electronically.

---

# Security Protocols, Events, and Incident Responses

## 1. Security Protocols

### How SSL/TLS Works:
1. The client sends a `ClientHello` message with supported encryption methods.
2. The server responds with a `ServerHello` and its certificate containing its public key.
3. The client validates the certificate.
4. The client encrypts a randomly generated "session key" with the server's public key and sends it.
5. The server decrypts the session key and uses it for encrypted communication.

### Example Use Case:
- HTTPS secures communication between a browser and a web server.

---

## 2. Security Events and Monitoring

### Example Workflow for SIEM (Splunk):
1. Log data from servers, firewalls, and applications is collected.
2. Data is parsed, indexed, and analyzed in real-time.
3. Alerts are triggered based on predefined rules (e.g., failed login attempts).

---

## 3. Incident Response

### Example Workflow for a DDoS Attack:
1. **Detection**: Monitoring tools like Cloudflare detect unusual traffic spikes.
2. **Containment**: Traffic is rerouted through a Web Application Firewall (WAF).
3. **Eradication**: IP blocking is implemented for malicious sources.
4. **Recovery**: Services are scaled back to normal levels after traffic subsides.
5. **Post-Incident Review**: Logs are analyzed to improve defenses.
