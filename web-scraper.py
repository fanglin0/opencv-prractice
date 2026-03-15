from selenium import webdriver
from selenium.webdriver.common.by import By
from sleneium.webdriver.support.ui import WebDrive
from selenium.webdriver.support import expected_conditions as EC

import os 
import requests
import shutil
import time
import re

#click through random pages and retriver image
driver = webdriver.Chrome()

image_folder = "/Users/fanglin/Downloads/brainrot_dataset"
os.mkdirs(image_folder, exist_ok=True)

num_imgs = 100

for i in range(num_images):
    try:
        driver.get('https://italianbrainrot.miraheze.org/wiki/Special:Random')
        target_img_text = "pi-image-thumbnail"
        target_img_title = "mw-image-title"
        image_element = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH, f"//img[@class='{target_img_text}]]"))
            EC.visibility_of_element_located((By.XPATH, f"//img[@class='{target_img_title}]]"))
            )
        image_src = image_element.get_attribute('src')
        image_title = image_title.lower()

        image_title = image_element.get_attribute('span')
        print(f"Found image source: {image_src}")
        print(f"Found image title: {image_title}")

        safe_title = image_title.replace(" ", "_").replace("/", "_")
        safe_title = re.sub(r'[^\w\-_. ]', '_', image_title))
        if safe_title in existing_folders:
            print(f"Folder '{safe_title}' already exists.")
            break
        else: 
            new_folder = os.mkdir({safe_title})
            print(f"Folder '{new_folder}' created")
            filename = os.path.join(image_folder, new_folder + ".jpg")
            
        response = requests.get(image_src, stream=True)
        response.raise_for_status()

        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print (f"Image donwloaded successfully as {filename}!")

        shutil.move(filename, new_folder)
        print(f"Moved {source_file} to {destination}")
        time.sleep(1) #my please and thank you's to the server. plz dont ban me

    except Exception as e:
        print(f"An error occured: {e}")
finally:
    driver.quit()


