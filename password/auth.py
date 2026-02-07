import hmac
import hashlib
import os
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import zxcvbn

# In a real app, this should be in an environment variable or secure vault.
# For this demo, we use a fixed secret pepper.
PEPPER = b"super-secret-server-side-pepper-key"

class PasswordManager:
    def __init__(self):
        # Argon2id settings
        self.ph = PasswordHasher(
            time_cost=3,      # Number of iterations
            memory_cost=65536, # 64MiB
            parallelism=4,    # Number of parallel threads
            hash_len=32,      # Length of the hash in bytes
            salt_len=16       # Length of the random salt
        )

    def _apply_pepper(self, password: str) -> bytes:
        """Apply HMAC-SHA256 pepper to the password."""
        return hmac.new(PEPPER, password.encode(), hashlib.sha256).digest()

    def validate_strength(self, password: str, username: str = ""):
        """Validate password strength using zxcvbn."""
        inputs = [username] if username else []
        results = zxcvbn.zxcvbn(password, user_inputs=inputs)
        
        # Score ranges from 0 (too weak) to 4 (very strong)
        # We require at least 3 for "Strong"
        return {
            "score": results['score'],
            "suggestions": results['feedback']['suggestions'],
            "warning": results['feedback']['warning'],
            "is_strong": results['score'] >= 3
        }

    def hash_password(self, password: str) -> str:
        """Pepper or hash a password using Argon2id."""
        peppered_password = self._apply_pepper(password)
        # We use the digest as input to Argon2
        # Note: Argon2 treats the bytes as the password
        return self.ph.hash(peppered_password)

    def verify_password(self, password: str, hashed_password: str) -> bool:
        """Verify a password against an Argon2 hash."""
        try:
            peppered_password = self._apply_pepper(password)
            return self.ph.verify(hashed_password, peppered_password)
        except VerifyMismatchError:
            return False
        except Exception:
            return False

if __name__ == "__main__":
    # Quick sanity check
    pm = PasswordManager()
    pw = "CorrectHorseBatteryStaple123!"
    h = pm.hash_password(pw)
    print(f"Hashed: {h}")
    print(f"Verify correct: {pm.verify_password(pw, h)}")
    print(f"Verify incorrect: {pm.verify_password('wrong', h)}")
    print(f"Strength: {pm.validate_strength(pw)}")
