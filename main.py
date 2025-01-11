from selenium import webdriver
import random, string, time

def open(url, length):
    block = string.ascii_lowercase + string.digits
    browser = webdriver.Chrome()

    while True:
        pasta = ''.join(random.choice(block) for _ in range(length))
        browser.get(url.replace('_', pasta))
        
        status_code = browser.execute_script("return window.performance.getEntriesByType('navigation')[0].responseStatus")

        if status_code == 404:
            time.sleep(0.25)
            continue
        else:
            browser.execute_script('document.querySelector("body > video").style = "width: 100%";')
            input()

open('https://video-preview.s3.yandex.net/_AAAAA.mp4', 6)
