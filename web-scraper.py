from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import requests
import shutil
import time
import re

# click through random pages and retrieve image
driver = webdriver.Chrome()

image_folder = "/Users/fanglin/Downloads/brainrot_dataset/test"
os.makedirs(image_folder, exist_ok=True)

num_images = 100

for i in range(num_images):
    try:
        driver.get('https://italianbrainrot.miraheze.org/wiki/Special:Random')

        target_img_text = "pi-image-thumbnail"

        image_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//img[@class='{target_img_text}']"))
        )

        image_src = image_element.get_attribute('src')
        image_title = image_element.get_attribute('alt')

        image_title = image_title.lower()

        print(f"Found image source: {image_src}")
        print(f"Found image title: {image_title}")

        safe_title = image_title.replace(" ", "_").replace("/", "_")
        safe_title = re.sub(r'[^\w\-_. ]', '_', safe_title)

        new_folder = os.path.join(image_folder, safe_title)
        os.makedirs(new_folder, exist_ok=True)

        filename = os.path.join(new_folder, safe_title + ".jpg")

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Referer": driver.current_url
        }

        response = requests.get(image_src, headers=headers, stream=True)
        response.raise_for_status()

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Image downloaded successfully as {filename}!")

        time.sleep(1)  # polite delay

    except Exception as e:
        print(f"An error occurred: {e}")

driver.quit()

#current issue to fix: 403 errors.
#add this under response.get(): 