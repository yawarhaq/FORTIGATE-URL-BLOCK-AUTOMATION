import requests
import urllib3

urllib3.disable_warnings()

# CONFIG

FORTIGATE_IP = "<YOUR-URL>"
API_TOKEN = "<YOUR-API-TOKEN>"
VDOM = "root"

WEBFILTER_PROFILE = "<YOUR-WEB-PROFILE-NAME>"
URL_FILE = "/path/to/file/blocked_url.txt"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# FUNCTIONS

def get_webfilter_profile():
    api = f"{FORTIGATE_IP}/api/v2/cmdb/webfilter/profile/{WEBFILTER_PROFILE}?vdom={VDOM}"
    r = requests.get(api, headers=HEADERS, verify=False)
    if r.status_code != 200:
        raise Exception(r.text)
    return r.json()["results"][0]


def get_urlfilter(urlfilter_id):
    api = f"{FORTIGATE_IP}/api/v2/cmdb/webfilter/urlfilter/{urlfilter_id}?vdom={VDOM}"
    r = requests.get(api, headers=HEADERS, verify=False)
    if r.status_code != 200:
        raise Exception(r.text)
    return r.json()["results"][0]


def update_urlfilter(urlfilter_id, entries):
    payload = {
        "entries": entries
    }

    api = f"{FORTIGATE_IP}/api/v2/cmdb/webfilter/urlfilter/{urlfilter_id}?vdom={VDOM}"
    r = requests.put(api, headers=HEADERS, json=payload, verify=False)

    print("\n PUT status:", r.status_code)
    print("Response:", r.text)

    if r.status_code == 200 and '"revision_changed":true' in r.text:
        print("\n URL Filter updated successfully")
    else:
        print("\n No revision change")


# MAIN

if __name__ == "__main__":
    print("Adding blocked URLs via correct urlfilter-table\n")

    profile = get_webfilter_profile()
    urlfilter_id = profile.get("web", {}).get("urlfilter-table")

    if not urlfilter_id:
        print("No urlfilter-table linked to this profile")
        exit(1)

    urlfilter = get_urlfilter(urlfilter_id)
    entries = urlfilter.get("entries", [])

    existing_urls = {e["url"] for e in entries if "url" in e}
    next_id = max([e.get("id", 0) for e in entries], default=0) + 1

    with open(URL_FILE) as f:
        urls = [line.strip() for line in f if line.strip()]

    changed = False

    for url in urls:
        if url in existing_urls:
            print(f"Already exists: {url}")
            continue

        entries.append({
            "id": next_id,
            "url": url,
            "type": "simple",
            "action": "block",
            "status": "enable"
        })

        print(f"Added: {url}")
        next_id += 1
        changed = True

    if changed:
        update_urlfilter(urlfilter_id, entries)
    else:
        print("\n No new URLs to add")
