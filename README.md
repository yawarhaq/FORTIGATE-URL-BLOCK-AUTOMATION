📌 Overview:-
- This project provides a Python-based automation script to block websites (URLs/domains) on a FortiGate firewall using the official FortiGate REST API.
- The script reads URLs from a text file and safely updates the URL Filter linked to a specified Web Filter Profile. It is designed for FortiOS 7.x and follows Fortinet’s internal configuration model.

🔐 Why This Script Is Needed:-
- In FortiOS 7.x:
  Web Filter Profiles do not directly store blocked URLs.
  Blocked URLs are stored inside a URL Filter object.
  The Web Filter Profile only references that URL Filter.
- This script correctly:
  Identifies the URL Filter linked to the Web Filter Profile.
  Updates the blocked URLs in the correct object.
  Prevents accidental configuration overwrites.

🔑 Configuration:-
1. Clone the repository in your system.

2. Create Virtual Environment where are the data and main folders with the following command-
   python3 -m venv fgvenv
   
3. Make sure to activate the virtual environment-
   source fgenv/bin/activate
   
4. Install the dependency-
   pip install requests
   
5. Mention the credentials and the give the following inputs in scripts (one time setup only)-
   FORTIGATE_IP = "<YOUR-URL>"
   API_TOKEN = "<YOUR-API-TOKEN>"
   
   WEBFILTER_PROFILE = "<YOUR-WEB-PROFILE-NAME>"
   URL_FILE = "/path/to/file/blocked_url.txt"

6. Edit the blocked_url.txt file as per the requirements and run the script.

7. The urls will be blocked.
