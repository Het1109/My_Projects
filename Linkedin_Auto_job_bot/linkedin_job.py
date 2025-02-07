import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# personal details like mail_id and password in details file
from details import * 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach" , True)


Linkedin_URL = webdriver.Chrome(options= chrome_options)
# personal url link from jobs section after applying particular filters 🖗 add ease apply also . 
Linkedin_URL.get('https://www.linkedin.com/jobs/search/?currentJobId=4141100193&f_AL=true&f_PP=105214831%2C105556991%2C106888327%2C103671728%2C116703352%2C106164952%2C104990346&geoId=102713980&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R')




Sign_in =Linkedin_URL.find_element(by=By.XPATH , value= '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
# print(Sign_in.text)
# click using selenium
Sign_in.click()





email = Linkedin_URL.find_element(By.XPATH , value='//*[@id="base-sign-in-modal_session_key"]')
email.send_keys(EMAIL_ID)

password = Linkedin_URL.find_element(By.XPATH , value='//*[@id="base-sign-in-modal_session_password"]')
password.send_keys(PASSWORD)

_2nd_sign_in =  Linkedin_URL.find_element(By.XPATH , value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
_2nd_sign_in.click()

# Ease apply for the first job 
ease_apply = Linkedin_URL.find_element(By.XPATH , value= '//*[@id="ember52"]/span')
ease_apply.click()

# filling phone number in apply section

phone = Linkedin_URL.find_element(by=By.XPATH, value= '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4141100193-8943130649-phoneNumber-nationalNumber"]')
if phone.text == "":
    phone.send_keys(PHONE_NO)

# next button
next = Linkedin_URL.find_element(by=By.CSS_SELECTOR, value="footer button")
next.click()


# Resume subimiision
# Upload resume from setting before hand 

next_buuton_in_resume = Linkedin_URL.find_element(by=By.XPATH, value='//*[@id="ember320"]/span')
next_buuton_in_resume.click()









# Facing error in multiple job applications.


# # loop to Save all the companies


# def abort_application():
#     # Click Close Button
#     close_button = Linkedin_URL.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
#     close_button.click()

#     time.sleep(2)
#     # Click Discard Button
#     discard_button = Linkedin_URL.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
#     discard_button.click()






# # Get Listings
# time.sleep(5)
# all_listings = Linkedin_URL.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

# # Apply for Jobs
# for listing in all_listings:
#     print("Opening Listing")
#     listing.click()
#     time.sleep(2)
#     try:
#         # Click Apply Button
#         apply_button = Linkedin_URL.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
#         apply_button.click()

#         # Insert Phone Number
#         # Find an <input> element where the id contains phoneNumber
#         time.sleep(5)
#         phone = Linkedin_URL.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
#         if phone.text == "":
#             phone.send_keys(PHONE_NO)

#         # Check the Submit Button
#         submit_button = Linkedin_URL.find_element(by=By.CSS_SELECTOR, value="footer button")
#         if submit_button.get_attribute("data-control-name") == "continue_unify":
#             abort_application()
#             print("Complex application, skipped.")
#             continue
#         else:
#             # Click Submit Button
#             print("Submitting job application")
#             submit_button.click()

#         time.sleep(2)
#         # Click Close Button
#         close_button = Linkedin_URL.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
#         close_button.click()

#     except NoSuchElementException:
#         abort_application()
#         print("No application button, skipped.")
#         continue

# time.sleep(5)
# Linkedin_URL.quit()
