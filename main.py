import requests
from concurrent.futures import ThreadPoolExecutor
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from tqdm import tqdm
import threading

# Read the cookie from an external file `cookie.txt`
def read_cookie_from_file(file_path='cookie.txt'):
    try:
        with open(file_path, 'r') as file:
            # Read the first line of the file and strip any extra spaces
            cookie = file.readline().strip()
            return cookie
    except FileNotFoundError:
        return None

# Initialize headers with the dynamic cookie
def initialize_headers(cookie):
    return {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8,fr-FR;q=0.7,fr;q=0.6',
        'content-type': 'application/json',
        'cookie': cookie,
        'origin': 'https://coccoc.com',
        'referer': 'https://coccoc.com/webhp?espv=2&ie=UTF-8&l=vi',
        'sec-ch-ua': '"CocCoc";v="135", "Not-A.Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Mobile Safari/537.36',
    }

# Retry logic
session = requests.Session()
retries = Retry(total=5, backoff_factor=0.3, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

# Total requests count for the progress bar
total_requests = 1033  # Total from previous calculation
progress_bar = tqdm(total=total_requests, desc="Processing requests")
progress_lock = threading.Lock()

def diem_danh(headers, steak_num):
    responses = []
    for i in range(steak_num * 10, steak_num * 10 + 11):
        json_data = {'streak_id': i}
        try:
            response = session.post('https://points-frontend-api.coccoc.com/api/v1/streaks', headers=headers, json=json_data)
            response.raise_for_status()
            responses.append(response.text)
        except requests.RequestException as e:
            None
        finally:
            with progress_lock:
                progress_bar.update(1)  # Update progress for each request
    return responses

def lam_nv(headers, mission_num):
    responses = []
    for mission_id in range(mission_num * 100, mission_num * 100 + 100):
        json_data = {'mission_id': mission_id}
        try:
            response = session.post('https://points-frontend-api.coccoc.com/api/v1/missions', headers=headers, json=json_data)
            response.raise_for_status()
            responses.append(response.text)
            None
        except requests.RequestException as e:
            None
        finally:
            with progress_lock:
                progress_bar.update(1)  # Update progress for each request
    return responses

def run_diem_danh(headers, threads_count):
    with ThreadPoolExecutor(max_workers=threads_count) as executor:
        futures = [executor.submit(diem_danh, headers, x) for x in range(3)]
        for future in futures:
            future.result()  # Wait for each future to complete

def run_lam_nv(headers, threads_count):
    with ThreadPoolExecutor(max_workers=threads_count) as executor:
        futures = [executor.submit(lam_nv, headers, x) for x in range(10)]
        for future in futures:
            future.result()  # Wait for each future to complete

if __name__ == "__main__":
    # Load cookie from the file
    cookie = read_cookie_from_file()
    if not cookie:
        None
    else:
        # Initialize headers with the loaded cookie
        headers = initialize_headers(cookie)
        
        # Run diem_danh with multiple threads
        None
        run_diem_danh(headers, threads_count=3)

        # Run lam_nv with multiple threads
        None
        run_lam_nv(headers, threads_count=10)

        # Close the progress bar after all tasks are complete
        progress_bar.close()
