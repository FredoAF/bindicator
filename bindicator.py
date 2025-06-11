#!/usr/bin/python
import requests
from datetime import datetime, timedelta

# API endpoint
url = "https://api.westnorthants.digital/openapi/v1/unified-waste-collections/100031184867"
today = datetime.now().date()

# Fetch data from the API
response = requests.get(url)
data = response.json()

# Extract collection items
collection_items = data.get('collectionItems', [])

# Find refuse and recycling dates
refuse_date_str = next((item['date'] for item in collection_items if item.get('type') == 'refuse'), None)
recycling_date_str = next((item['date'] for item in collection_items if item.get('type') == 'recycling'), None)

if refuse_date_str:
    # Parse the refuse date (assuming ISO format: YYYY-MM-DD)
    refuse_date = datetime.strptime(refuse_date_str, "%Y-%m-%d").date()
    
    # Check if today is one day before refuse_date
    if today == refuse_date - timedelta(days=1):
        # Send alert to ntfy.sh
        topic = "towcester-bindicator-test"  # Change this to your ntfy.sh topic
        message = f"Reminder: Black bin collection is tomorrow ({refuse_date})!"
        ntfy_url = f"https://ntfy.sh/{topic}"
        requests.post(ntfy_url, data=message.encode('utf-8'), headers={"Tags": "wastebasket,black_circle"})
        print("Alert sent to ntfy.sh!")
    else:
        print("No refuse alert needed today.")
else:
    print("No refuse date found.")

if recycling_date_str:
    # Parse the refuse date (assuming ISO format: YYYY-MM-DD)
    recycling_date = datetime.strptime(recycling_date_str, "%Y-%m-%d").date()
    
    # Check if today is one day before refuse_date
    if today == recycling_date - timedelta(days=1):
        # Send alert to ntfy.sh
        topic = "towcester-bindicator"  # Change this to your ntfy.sh topic
        message = f"Reminder: Recycling collection is tomorrow ({recycling_date})!"
        ntfy_url = f"https://ntfy.sh/{topic}"
        requests.post(ntfy_url, data=message.encode('utf-8'), headers={"Tags": "recycle,large_blue_circle"})
        print("Alert sent to ntfy.sh!")
    else:
        print("No recycling alert needed today.")
else:
    print("No recycling date found.")