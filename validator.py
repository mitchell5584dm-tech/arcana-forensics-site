#!/usr/bin/env python3
import hashlib
import sys
from pathlib import Path

def generate_hash(file_path, algorithm='sha256'):
    """Generates a cryptographic hash for a given file."""
    try:
        # Dynamically select the hash algorithm
        hash_func = getattr(hashlib, algorithm)()
    except AttributeError:
        return f"Error: Unsupported algorithm '{algorithm}'"

    try:
        # Read in binary chunks to ensure OS-agnostic hashing
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b""):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        return f"Error reading file: {e}"

if __name__ == "__main__":
    # Ensure a file was passed as an argument
    if len(sys.argv) < 2:
        print("Usage: ./validator.py <file_to_hash>")
        sys.exit(1)
    
    target_file = Path(sys.argv[1])
    
    if target_file.is_file():
        print(f"Target: {target_file.name}")
        print(f"SHA-256: {generate_hash(target_file, 'sha256')}")
        print(f"SHA-512: {generate_hash(target_file, 'sha512')}")
    else:
        print(f"Error: '{target_file}' is not a valid file.")
