import requests
import string

def scan_sql_injection(url):
    payloads = [' OR 1=1', ' AND 1=1', ' OR 1=2', ' AND 1=2', "' OR 1=1", "' AND 1=1", "' OR 1=2", "' AND 1=2"]
    vulnerable = False

    for payload in payloads:
        query = url + payload
        response = requests.get(query)
        if response.status_code == 200:
            if "error" not in response.text.lower():
                print(f"[+] SQL injection vulnerability detected in {query}")
                vulnerable = True

    if not vulnerable:
        print("[!] No SQL injection vulnerabilities found")

if __name__ == "__main__":
    url = input("Enter the URL to scan (including query parameters): ")
    scan_sql_injection(url)