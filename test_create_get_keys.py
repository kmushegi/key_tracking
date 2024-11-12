import requests

# Define the base URL for the API
BASE_URL = "http://0.0.0.0:8000"

# Sample keys to create
keys = [
    {"key_id": "GUEST-1", "key_type": "Guest", "status": "Available"},
    {"key_id": "CLEANER-1", "key_type": "Cleaners", "status": "Available"},
    {"key_id": "MAINTENANCE-1", "key_type": "Maintenance", "status": "Available"},
]


# Function to create a key
def create_key(key_data):
    response = requests.post(f"{BASE_URL}/keys/", json=key_data)
    if response.status_code == 200:
        print(f"Successfully created key: {response.json()}")
    else:
        print(f"Failed to create key: {response.status_code} - {response.text}")


# Function to retrieve all keys
def get_all_keys():
    response = requests.get(f"{BASE_URL}/keys/")
    if response.status_code == 200:
        print("All keys:")
        for key in response.json():
            print(key)
    else:
        print(f"Failed to retrieve keys: {response.status_code} - {response.text}")


# Function to delete all keys retrieved from get_all_keys
def delete_all_retrieved_keys():
    response = requests.get(f"{BASE_URL}/keys/")
    if response.status_code == 200:
        keys = response.json()
        for key in keys:
            key_id = key["key_id"]
            response = requests.delete(f"{BASE_URL}/keys/{key_id}")
            if response.status_code == 200:
                print(f"Key {key_id} deleted successfully")
            else:
                print(
                    f"Failed to delete key {key_id}: {response.status_code} - {response.text}"
                )
    else:
        print(f"Failed to retrieve keys: {response.status_code} - {response.text}")


# Function to fetch a specific key
def fetch_specific_key(key_id):
    response = requests.get(f"{BASE_URL}/keys/{key_id}")
    if response.status_code == 200:
        print(f"Key {key_id} fetched successfully: {response.json()}")
    else:
        print(f"Failed to fetch key {key_id}: {response.status_code} - {response.text}")


# Test creating multiple keys
for key in keys:
    create_key(key)

# Query all keys after creation
print("\nQuerying all keys after creation:")
get_all_keys()

# Delete all keys retrieved from get_all_keys
delete_all_retrieved_keys()

print("\nQuerying all keys after creation:")
get_all_keys()
