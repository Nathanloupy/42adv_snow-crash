#!/usr/bin/env python3

def decrypt_token(token_data):
    """
    Reverse the transformation: output_char = input_char + position
    So: input_char = output_char - position
    """
    password = ""
    
    for position, char in enumerate(token_data):
        # Convert char to its ASCII value, subtract position, then back to char
        decrypted_char = chr(ord(char) - position)
        password += decrypted_char
    
    return password

def main():
    try:
        # Read the token file
        with open('token', 'rb') as f:
            token_data = f.read().decode('latin-1').strip()
        
        # Decrypt the token
        password = decrypt_token(token_data)
        
        print(f"Decrypted password: {password}")
        
        # Verify by re-encrypting
        print("Verification - re-encrypting the password:")
        verification = ""
        for position, char in enumerate(password):
            encrypted_char = chr(ord(char) + position)
            verification += encrypted_char
        
        print(f"Re-encrypted: {repr(verification)}")
        print(f"Original token: {repr(token_data)}")
        print(f"Match: {verification == token_data}")
        
    except FileNotFoundError:
        print("Error: token file not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 