import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#import HtmlTestRunner

class LoginKasir(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
		self.url = "https://magento.softwaretestingboard.com/customer/account/create/"

	def a_failed_signup_user_registered(self):
		driver = self.browser
		driver.get(self.url)
		driver.find_element(By.NAME, "firstname").send_keys("Wanda")
		driver.find_element(By.ID, "lastname").send_keys("Wong")
		driver.find_element(By.ID, "email_address").send_keys("w@a.com")
		driver.find_element(By.ID, "password").send_keys("123Asdqw")
		driver.find_element(By.ID, "password-confirmation").send_keys("123Asdqw")
		driver.find_element(By.CLASS_NAME, "action.submit.primary").click()

		respon = driver.find_element(By.CLASS_NAME,"message-error.error.message").text
		self.assertIn('There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account.', respon)
		#disini masih error, entah kanapa di test auto errornya engga keluar, tapu kalo dimanual keluar tulisan errornya

	def test_b_failed_signup_blank(self):
		driver = self.browser
		driver.get(self.url)
		driver.find_element(By.CLASS_NAME, "action.submit.primary").click()

		respon = driver.find_element(By.ID, "firstname-error").text
		self.assertIn('This is a required field.', respon)

	def test_c_failed_signup_invalid_email(self):
		driver = self.browser
		driver.get(self.url)
		driver.find_element(By.NAME, "firstname").send_keys("Sandra")
		driver.find_element(By.ID, "lastname").send_keys("Park")
		driver.find_element(By.ID, "email_address").send_keys("wand@.cpm")
		driver.find_element(By.ID, "password").send_keys("123Asdqw")
		driver.find_element(By.ID, "password-confirmation").send_keys("123Asdqw")
		driver.find_element(By.CLASS_NAME, "action.submit.primary").click()

		respon = driver.find_element(By.ID,"email_address-error").text
		self.assertIn('Please enter a valid email address (Ex: johndoe@domain.com).', respon)

	def test_d_failed_signup_invalid_password(self):
		driver = self.browser
		driver.get(self.url)
		driver.find_element(By.NAME, "firstname").send_keys("Sandra")
		driver.find_element(By.ID, "lastname").send_keys("Park")
		driver.find_element(By.ID, "email_address").send_keys("wand@a.com")
		driver.find_element(By.ID, "password").send_keys("passwd")
		driver.find_element(By.ID, "password-confirmation").send_keys("passwd")
		driver.find_element(By.CLASS_NAME, "action.submit.primary").click()

		respon = driver.find_element(By.ID,"password-error").text
		self.assertIn('Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored.', respon)

	def test_e_failed_signup_invalid_confirm_password(self):
		driver = self.browser
		driver.get(self.url)
		driver.find_element(By.NAME, "firstname").send_keys("Sandra")
		driver.find_element(By.ID, "lastname").send_keys("Park")
		driver.find_element(By.ID, "email_address").send_keys("wand@a.com")
		driver.find_element(By.ID, "password").send_keys("Asdqwe123")
		driver.find_element(By.ID, "password-confirmation").send_keys("passwd")
		driver.find_element(By.CLASS_NAME, "action.submit.primary").click()

		respon = driver.find_element(By.ID,"password-confirmation-error").text
		self.assertIn('Please enter the same value again.', respon)	

	def failed_signup(self):
		driver = self.browser
		driver.get(self.url)
		driver.find_element(By.NAME, "firstname").send_keys("Lala")
		driver.find_element(By.ID, "lastname").send_keys("Okta")
		driver.find_element(By.ID, "email_address").send_keys("a@b,com")
		driver.find_element(By.ID, "password").send_keys("a")
		driver.find_element(By.ID, "password-confirmation").send_keys("B")
		driver.find_element(By.CLASS_NAME, "action.submit.primary").click()

		#respons = driver.find_element(By.CLASS_NAME, "mage-error").text
		#self.assertIn('Please enter a valid email address (Ex: johndoe@domain.com).', respons)

def tearDown(self):
		self.browser.close()

#if __name__ == "__main__":
#	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='result'))

if __name__ == "__main__":
	unittest.main()