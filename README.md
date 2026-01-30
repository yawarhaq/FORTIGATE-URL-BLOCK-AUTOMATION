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
