from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time


def main():

    profile = FirefoxProfile()

    # Настройка SOCKS5 через Tor
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.socks", "127.0.0.1")
    profile.set_preference("network.proxy.socks_port", 9150)
    profile.set_preference("network.proxy.socks_remote_dns", True)

    # Важно для .onion
    profile.set_preference("network.dns.blockDotOnion", False)

    profile.update_preferences()

    options = Options()
    options.headless = False  # можно True если не нужно окно

    driver = webdriver.Firefox(firefox_profile=profile, options=options)

    print("Tor Firefox запущен")

    url = input("Enter the .onion URL: ")
    driver.get(url)

    time.sleep(15)

    html = driver.page_source

    with open("tor.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Saved HTML to tor.html")

    driver.quit()


if __name__ == "__main__":
    main()