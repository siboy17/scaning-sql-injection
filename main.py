import requests

def load_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def scan_sql_injection(urls, payloads):
    for url in urls:
        vulnerable = False
        for payload in payloads:
            query = url + payload
            try:
                response = requests.get(query)
                if response.status_code == 200:
                    if "error" not in response.text.lower():
                        print(f"[+] SQL injection vulnerability detected in {query}")
                        vulnerable = True
            except requests.exceptions.RequestException as e:
                print(f"[!] Error accessing {query}: {e}")

        if not vulnerable:
            print(f"[!] No SQL injection vulnerabilities found in {url}")

if __name__ == "__main__":
    urls_file = input("Enter the path to the URL file: ")
    payloads_file = input("Enter the path to the payload file: ")

    urls = load_file(urls_file)
    payloads = load_file(payloads_file)

    scan_sql_injection(urls, payloads)
