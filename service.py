from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Service:
    driver = None

    def __init__(self, driver_path):
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        self.driver = webdriver.Chrome(executable_path=driver_path, options=options)

    def getSlots(self, userId, password):
        self.driver.get("https://reboks.nus.edu.sg/nus_public_web/public/profile/buypass/gym")

        if self.driver.current_url == "https://reboks.nus.edu.sg/nus_public_web/public/auth?redirect=%2Fnus_public_web%2Fpublic%2Fprofile%2Fbuypass%2Fgym":
            self.driver.get("https://vafs.nus.edu.sg/adfs/ls/?SAMLRequest=lVJRS8MwEP4rJe9t2s7RLmyD6RAHU4urPvgy0iTdgm1Sc8nQf2%2FWKm4PDoRAcl%2Fu%2B%2B7u46ZA26YjC2f36km8OwE2%2BGgbBaT%2FmCFnFNEUJBBFWwHEMrJZ3K9JGsWkM9pqpht0QrnMoADCWKkVClbLGdqOGL1KcprWeRKPJjxjjCajLIs5rVlVxXma1%2BPJOOOTFAUvwoBnzpAX8nQAJ1YKLFXWQ3GahHEWJnmZxGSU%2BvOKgqWfRipqe9be2g4IxgdaQ6QcRIK7CHaY8hpwAxgFi5%2FmbrQC1wqzEeYgmXh%2BWv%2FSjaj025mAf26Pk2%2B9HQfJhcGdqxrJ8BHEreauEVG374YYhjsNKYMeHQRRUHybeS0Vl2p32cdqSAJyV5ZFWDxuSjSfHnVJ74uZ%2F6PdKT4lToeFePAlV8tC%2Bzk%2Bg1ttWmr%2F7iiJkh6RPKz7VOIUdILJWgqO8HyocL5l8y8%3D&RelayState=http%3A%2F%2Freboks.nus.edu.sg%2Fnus_saml_provider%2Fpublic%2Findex.php%2Fadfs%2Fauth&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=LRyuSmCTI4710NRwjkLw0zbdmnWPDdhYNtdfHQBQcHmgReZk%2BXVMuyJMuWdY7kuy4nhnFYJTUEU1w6F3Or8eRN2zvuepKGQBYQ1xFB%2FAfTAUaVxHv%2FG%2BesKmuRznv13EHBlmQzbNrlSWHbGkO3C%2BTujeuAP5sT5enTS%2BqUpdygtU3GyeWjgrSW1LjAFLWmW9beE4Xl5KkeXz8Mr%2BbH8r1FKDOWXAMAz6RLc%2BajJH8QmYIdVRUHv7fowgZBowU2DrxUon2yGaLcyMRMaIImsgCsuCgS%2FxYPy7rirqLRjocsvEti2tZnlm5hQzqF%2BAHNa6u5X%2F3xfRKGD7WBQJG6TbmQ%3D%3D")
            self.driver.find_element_by_id("userNameInput").send_keys(userId)
            self.driver.find_element_by_id("passwordInput").send_keys(password)
            self.driver.find_element_by_id("submitButton").click()
            self.driver.get("https://reboks.nus.edu.sg/nus_public_web/public/profile/buypass/gym")

        response = ""
        gymboxes = self.driver.find_elements_by_class_name("gymbox")
        for i in range(len(gymboxes)):
            if i == 2:
                response = response + "\n" + gymboxes[i].text + "/40" 
            else:
                response = response + "\n" + gymboxes[i].text + "/20" 

        return response
