#!/usr/bin/env python3
import crypt
import sys

# The hash from flag01
target_hash = "42hDRfypTqqnw"

# Common passwords to try
passwords = [
    "abcdefg",
    "password",
    "123456",
    "admin",
    "root",
    "flag01",
    "flag",
    "42",
    "snow",
    "crash",
    "guest",
    "user",
    "test",
    "hello",
    "world",
    "linux",
    "ubuntu",
    "debian",
    "qwerty",
    "abc123",
    "letmein",
    "welcome",
    "monkey",
    "dragon",
    "master",
    "shadow",
    "sunshine",
    "princess",
    "football",
    "computer",
    "internet",
    "secret",
    "love",
    "freedom",
    "whatever",
    "killer",
    "trustno1",
    "superman",
    "batman",
    "michael",
    "jennifer",
    "jordan"
]

print(f"Attempting to crack hash: {target_hash}")
print("Trying common passwords...")

for password in passwords:
    # DES crypt uses first 2 characters as salt
    salt = target_hash[:2]
    hashed = crypt.crypt(password, salt)
    
    if hashed == target_hash:
        print(f"\n🎉 PASSWORD FOUND: {password}")
        sys.exit(0)
    else:
        print(f"❌ {password} -> {hashed}")

print("\n❌ Password not found in common list.")
print("Try using a dictionary attack with a larger wordlist.")