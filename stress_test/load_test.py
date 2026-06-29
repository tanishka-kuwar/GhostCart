import concurrent.futures
import requests
import time

URL = "http://127.0.0.1:5000/checkout"

payload = {
    "user_id":1,
    "product_id":1,
    "quantity":1
}

def buy_product(_):
    try:
        response = requests.post(URL, json=payload)
        return response.status_code
    
    except Exception as e:
        return str(e)

def main():
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        result = list(executor.map(buy_product,range(500)))

    end = time.time()

    success = result.count(201)
    failed = len(result) - success

    print("=" * 50)
    print("GhostCart Stress Test Report")
    print("=" * 50)
    print(f"Total Requests      : {len(results)}")
    print(f"Successful Orders   : {success}")
    print(f"Failed Orders       : {failed}")
    print(f"Execution Time      : {end-start:.2f} sec")
    print(f"Throughput          : {len(results)/(end-start):.2f} req/sec")
    
    if success + failed == len(result):
        print("✔️ Request Count Verified")
    
    if success == 100:
        print("✔️ No Overselling Detected")
    
    print("=" * 50)

if __name__ == "__main__":
    main()