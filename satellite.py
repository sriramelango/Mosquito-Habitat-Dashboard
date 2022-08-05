from selenium import webdriver
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def obtainSatelliteImage(latitude, longitude):

    driver = webdriver.Chrome(ChromeDriverManager().install())

    # URL of Satellite Imagery
    url = "https://earth.google.com/web/@" + str(latitude) + "," + str(longitude) + ",38000d"
    
    # Opening the website
    driver.get(url)

    sleep(120)

    driver.save_screenshot("satelliteImage.png")
    
    # Loading the image
    satelliteImage = Image.open("satelliteImage.png")

    return satelliteImage