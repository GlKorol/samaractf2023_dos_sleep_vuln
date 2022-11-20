import requests
import sys
import logging


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        logging.warning('\nNeed arg[1]: url')
        sys.exit()
    try:
        resp = requests.get(url, timeout=2)
        print(f'Server status: {resp.status_code}')
    except requests.exceptions.ReadTimeout:
        logging.error('Timeout error !!!!!!!!!')
    except requests.exceptions.ConnectionError:
        logging.error('Connection refused !!!!!!!')
