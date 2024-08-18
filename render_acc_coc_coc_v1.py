import selenium,requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import os
import pydub,psutil
import speech_recognition as sr
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import speech_recognition as sr
from pydub import AudioSegment

def end_task_chrome():
    run_exe_file_names=(requests.get('https://raw.githubusercontent.com/David22092007/About-xyz-2007-coding-/main/run_exe_file_name').text).replace('[','').replace(']','').replace('\n','').replace('"','').split(',')
    for file_exe_run_chrom in run_exe_file_names:
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] == file_exe_run_chrom:
                    pid = proc.info['pid'];os.system(f"taskkill /f /pid {pid}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
def delete_temp_files():
    os.system('rmdir //S //Q C:\\Users\\DEVICE~1\\AppData\\Local\\Temp')
def solve_captcha():
        global driver
        for i in range (2):
            try:
                    WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
                    break
            except:
                    None
            if i==1:
                print ('--LỖI-THAO-TÁC--')    
                exit()        
        iframes = driver.find_elements(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframes[0])
        for i in range (2):
            try:
                    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "recaptcha-checkbox-border")))
                    break
            except:
                    None
            if i==1:
                print ('--LỖI-THAO-TÁC--')    
                exit()                
        driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()
        sleep(3)
        driver.switch_to.default_content()
        frames = driver.find_elements(By.TAG_NAME,"iframe")
        driver.switch_to.frame(frames[-1])
        try:
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "recaptcha-audio-button")))
                driver.find_element(By.ID,"recaptcha-audio-button").click()
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "audio-source")))
                src=driver.find_element(By.ID,"audio-source").get_attribute("src")
                with open('audio\\audio.mp3','wb') as f:
                        f.write(requests.get(src).content)
                sound = AudioSegment.from_mp3("audio\\audio.mp3")
                sound.export("audio\\audio.wav", format="wav")

                # Khởi tạo Recognizer
                recognizer = sr.Recognizer()

                # Mở file WAV
                with sr.AudioFile("audio\\audio.wav") as source:
                    audio_data = recognizer.record(source)

                # Nhận diện giọng nói trong file âm thanh
                try:
                    text = recognizer.recognize_google(audio_data, language="en-US")
                    print("Nội dung nhận diện được: ", text)
                except sr.UnknownValueError:
                    print("Không thể nhận diện được âm thanh.")
                except sr.RequestError as e:
                    print(f"Lỗi khi kết nối với dịch vụ nhận diện: {e}")
                driver.find_element(By.ID,"audio-response").send_keys(text.lower())
                driver.find_element(By.ID,"audio-response").send_keys(Keys.ENTER)
                sleep(3)
                driver.switch_to.default_content()
                frames = driver.find_elements(By.TAG_NAME,"iframe")
                driver.switch_to.frame(frames[0])
                rsp= (driver.find_elements(By.TAG_NAME, "span"))
                for i in rsp:
                        if i.get_attribute('role')=="checkbox":
                            print (i.get_attribute('class'))
                            if i.get_attribute('class')=="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-checked" or i.get_attribute('class')=="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-focused recaptcha-checkbox-checked" or i.get_attribute('class')=="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-checked recaptcha-checkbox-focused":                                                                      
                                    print ('Đã Xác Minh Thành Công ✅')
                                    return True
                            else:
                                    print ('GIẢI KHÔNG THÀNH CÔNG ❎')
                                    return False
        except:
                print ('--LỖI KHÔNG GIẢI ĐƯỢC CAPTCHA AUDIO-- TIẾN HÀNH KIỂM TRA --')
                sleep(3)
                driver.switch_to.default_content()
                frames = driver.find_elements(By.TAG_NAME,"iframe")
                driver.switch_to.frame(frames[0])
                rsp= (driver.find_elements(By.TAG_NAME, "span"))
                for i in rsp:
                        if i.get_attribute('role')=="checkbox":
                            print (i.get_attribute('class'))
                            if i.get_attribute('class')=="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-checked" or i.get_attribute('class')=="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-focused recaptcha-checkbox-checked" or i.get_attribute('class')=="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-checked recaptcha-checkbox-focused":                                                                      
                                    print ('Đã Xác Minh Thành Công ✅')
                                    return True
                            else:
                                    print ('GIẢI KHÔNG THÀNH CÔNG ❎')
                                    return False
def login_get_cookie(mail,password):
        global driver
        driver.get('https://accounts.coccoc.com/loginEmail')
        elements=driver.find_elements(By.TAG_NAME, "input")
        for element in elements:
                name_tag=element.get_attribute("name")
                if name_tag=="email":
                        element.send_keys(email)
                if name_tag=="password":
                        element.send_keys(password)
        a=solve_captcha()
        if a:            
            driver.switch_to.default_content()        
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
            elements = driver.find_elements(By.TAG_NAME, "button")
            for element in elements:
                if element.get_attribute('type')=="submit":
                    if (element.get_attribute('class'))[0:4]=='py-2':
                        element.click()
                        break
            for i in range(3):
                try:
                    driver.switch_to.default_content()        
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "trigger-btn")))
                    break
                except:
                    driver.refresh()
            driver.get('https://accounts.coccoc.com/ServiceLogin?passive=true&service=points&continue=https://points.coccoc.com')
            for i in range(3):
                try:
                    driver.switch_to.default_content()
                    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "span")))
                    elements = driver.find_elements(By.TAG_NAME, "div")
                    for element in elements:
                        if element.get_attribute('class')=='cp-avatar':
                            break
                        if element==elements[len(elements)-1]:
                            print ('--SẢY-RA-LỖI--VUI--LÒNG--KIỂM--TRA--WIFI--')
                            exit()
                    break
                except:
                    driver.refresh()

            driver.switch_to.default_content()
            cookies=driver.get_cookies()
            cookie=''
            for i in cookies:
                if i==cookies[len(cookies)-1]:
                    cookie=cookie+i['name']+'='+i['value']
                else:
                    cookie=cookie+i['name']+'='+i['value']+';'            
            with open ('cookies.txt','a') as f:
                f.write(cookie+'\n')
                f.close()
            return cookie
        print ('--GIẢI--CAPTCHA--THẤT--BẠI--')

def checkmail_api(mail,password):        
        rsp=requests.get(f'https://gmx.live/login/new.php?login={mail}|{password}').text
        list_=rsp.split('https://accounts.coccoc.com/activate/')
        a=list_[1]
        link_active='https://accounts.coccoc.com/activate/'+str(a[0:a.find('\n')])
        return link_active

for i in ((requests.get('https://raw.githubusercontent.com/David22092007/Auto-Tik-Tok-TDS-/main/readme.txt').text).split('\n')):
    if i.find('secret=') >=0:
        password=i.replace('secret=','')
        break
requests=requests.session()

with open('mail_list\\mail.txt','r') as f:
        list_mail=f.readlines()
for mail in list_mail:   


    mail=mail.split('|')
    
    email=(mail[0].replace('\n',''))
     
    op = webdriver.ChromeOptions()

    ua = UserAgent()

    op.add_argument("--start-maximized")

    op.add_argument(f"user-agent={ua.random}")

    op.add_argument("--force-device-scale-factor=0.6")
            
    driver = uc.Chrome(options=op)

    try:
            driver.get('https://accounts.coccoc.com/signup')
            while True:
                    try:
                            WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
                            iframes = driver.find_elements(By.TAG_NAME, "iframe") 
                            break
                    except:
                            driver.refresh()
            sleep(5)
            driver.switch_to.default_content()                  
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "Email")))
            elements = driver.find_elements(By.TAG_NAME, "input")
            for element in elements:
                    name_tag=element.get_attribute("name")
                    if name_tag=="email":
                            element.send_keys(email)
                    if name_tag=="password":
                            element.send_keys(password)
                    if name_tag=="password_confirmation":
                            element.send_keys(password)
            solve_captcha()             
            driver.switch_to.default_content()        
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
            elements = driver.find_elements(By.TAG_NAME, "button")                
            for element in elements:
                    type_name=element.get_attribute('type')
                    if type_name=="submit":
                            element.click()
            sleep(10)
            driver.switch_to.default_content()
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "DialogContent")))
            elements = driver.find_elements(By.TAG_NAME, "div")
            count=0
            for element in elements:
                    delete_temp_files()
                    if count>=1:                                
                            break
                    type_name=element.get_attribute('aria-label')
                    if type_name=="confirm":
                            element.click()
                            sleep(20)
                            try:
                                    driver.switch_to.default_content()
                                    elements = driver.find_elements(By.TAG_NAME, "div")
                                    for element in elements:
                                            class_=element.get_attribute('class')
                                            if class_=="mb-4":
                                                    content=element.text
                                                    if content.find('Email đã được đăng ký') >= 0:
                                                            a=login_get_cookie(mail,password)
                                                            end_task_chrome()
                                                            driver.quit()  
                                                            break  
                                                    
                            except:
                                    sleep(20)
                                    driver.get(checkmail_api(email,password))
                                    elements=driver.find_elements(By.TAG_NAME, "div")
                                    for element in elements:
                                            class_=element.get_attribute('class')
                                            if class_=="flex flex-col gap-y-3":
                                                    print(element.text)
                                                    a=login_get_cookie(mail,password)
                                                    if a:
                                                            with open('cookie.txt','a') as f:
                                                                    f.write(cookie+'\n')
                                                                    f.close()
                                                            end_task_chrome()
                                                            driver.quit()  
                                                            break      
    finally:
        end_task_chrome()
        driver.quit()            

