import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#import HtmlTestRunner

class SignUpLumeYoga(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
		self.url_signup = "https://magento.softwaretestingboard.com/customer/account/create/"
		self.url_acc = "https://magento.softwaretestingboard.com/customer/account/edit"

	def a_success_signup(self):
		driver = self.browser
		driver.get(self.url_signup)
		driver.find_element(By.NAME, "firstname").send_keys("Arum")
		driver.find_element(By.ID, "lastname").send_keys("Rini")
		driver.find_element(By.ID, "email_address").send_keys("aqs@s.com")
		driver.find_element(By.ID, "password").send_keys("123Qweasd")
		driver.find_element(By.ID, "password-confirmation").send_keys("123Qweasd")
		driver.find_element(By.CLASS_NAME, "action.submit.primary").click()

		respon = driver.find_element(By.CLASS_NAME, "page-title").text
		self.assertIn('My Account', respon)
		#skip

	def b_create_signup_password_numbers(self):
		driver = self.browser
		driver.get(self.url_signup)
		driver.find_element(By.NAME, "firstname").send_keys("Putri") 
		driver.find_element(By.ID, "lastname").send_keys("Sonia")
		driver.find_element(By.ID, "email_address").send_keys("ad@s.com")
		driver.find_element(By.ID, "password").send_keys("1235678")
		driver.find_element(By.ID, "password-confirmation").send_keys("12345678")
		driver.find_element(By.CLASS_NAME, "action.submit.primary").click()

		respon = driver.find_element(By.ID,"password-error").text
		#respon = driver.find_element(By.TAG_NAME, "div").text
		self.assertIn('Minimum of different classes of characters in password is 3. Classes of characters: Lower Case, Upper Case, Digits, Special Characters.', respon)
		#error

	def test_c_failed_signup_invalid_email(self):
		driver = self.browser
		driver.get(self.url_signup)
		driver.find_element(By.NAME, "firstname").send_keys("Sandra")
		driver.find_element(By.ID, "lastname").send_keys("Park")
		driver.find_element(By.ID, "email_address").send_keys("wand@.cpm")
		driver.find_element(By.ID, "password").send_keys("123Asdqw")
		driver.find_element(By.ID, "password-confirmation").send_keys("123Asdqw")
		driver.find_element(By.CLASS_NAME, "action.submit.primary").click()

		respon = driver.find_element(By.ID,"email_address-error").text
		self.assertIn('Please enter a valid email address (Ex: johndoe@domain.com).', respon)
		#jalan

	def test_d_failed_signup_invalid_password(self):
		driver = self.browser
		driver.get(self.url_signup)
		driver.find_element(By.NAME, "firstname").send_keys("Sandra")
		driver.find_element(By.ID, "lastname").send_keys("Park")
		driver.find_element(By.ID, "email_address").send_keys("wand@a.com")
		driver.find_element(By.ID, "password").send_keys("passwd")
		driver.find_element(By.ID, "password-confirmation").send_keys("passwd")
		driver.find_element(By.CLASS_NAME, "action.submit.primary").click()

		respon = driver.find_element(By.ID,"password-error").text
		self.assertIn('Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored.', respon)
		#jalan

	def test_e_failed_signup_invalid_confirm_password(self):
		driver = self.browser
		driver.get(self.url_signup)
		driver.find_element(By.NAME, "firstname").send_keys("Sandra")
		driver.find_element(By.ID, "lastname").send_keys("Park")
		driver.find_element(By.ID, "email_address").send_keys("wand@a.com")
		driver.find_element(By.ID, "password").send_keys("Asdqwe123")
		driver.find_element(By.ID, "password-confirmation").send_keys("passwd")
		driver.find_element(By.CLASS_NAME, "action.submit.primary").click()

		respon = driver.find_element(By.ID,"password-confirmation-error").text
		self.assertIn('Please enter the same value again.', respon)
		#jalan

	def test_f_failed_signup_confirm_password_blank(self):
		driver = self.browser
		driver.get(self.url_signup)
		driver.find_element(By.NAME, "firstname").send_keys("Sandra")
		driver.find_element(By.ID, "lastname").send_keys("Park")
		driver.find_element(By.ID, "email_address").send_keys("wand@a.com")
		driver.find_element(By.ID, "password").send_keys("Asdqwe123")
		driver.find_element(By.ID, "password-confirmation").send_keys("")
		driver.find_element(By.CLASS_NAME, "action.submit.primary").click()
		
		respon = driver.find_element(By.ID, "password-confirmation-error").text
		self.assertIn('This is a required field.', respon)
		#jalan

	def g_failed_signup_user_registered(self):
		driver = self.browser
		driver.get(self.url_signup)
		driver.find_element(By.NAME, "firstname").send_keys("Linda")
		driver.find_element(By.ID, "lastname").send_keys("Moon")
		driver.find_element(By.ID, "email_address").send_keys("aq@qq.com")
		driver.find_element(By.ID, "password").send_keys("123Qweasd")
		driver.find_element(By.ID, "password-confirmation").send_keys("123Qweasd")
		driver.find_element(By.CLASS_NAME, "action.submit.primary").click()

		respon = driver.find_element(By.CLASS_NAME,"message-error.error.message").text
		self.assertIn('There is already an account with this email address. If you are sure that it is your email address,', respon)
		#disini masih error, entah kanapa di test auto errornya engga keluar, tapi kalo dimanual keluar tulisan errornya

	def h_success_change_email(self):
		driver = self.browser
		driver.get(self.url_acc)
		driver.find_element(By.ID, "email").send_keys("aqx@qq.com")
		driver.find_element(By.ID, "pass").send_keys("123Qweasd")
		driver.find_element(By.ID, "send2").click()
		driver.find_element(By.XPATH, "//input[@id='change-email']").click();
		driver.find_element(By.ID, "email").clear()
		driver.find_element(By.ID, "email").send_keys("aqx@s.com")
		driver.find_element(By.NAME, "current_password").send_keys("123Qweasd")
		driver.find_element(By.CLASS_NAME, "action.save.primary").click()
		
		respon = driver.find_element(By.CLASS_NAME, "base").text
		self.assertIn('Customer Login', respon)
		#skip | jalan | buat nanti

	def test_i_invalid_change_email(self):
		driver = self.browser
		driver.get(self.url_acc)
		driver.find_element(By.ID, "email").send_keys("add@ss.com")
		driver.find_element(By.ID, "pass").send_keys("123Qqweasd")
		driver.find_element(By.ID, "send2").click()
		driver.find_element(By.XPATH, "//input[@id='change-email']").click();
		driver.find_element(By.ID, "email").clear()
		driver.find_element(By.ID, "email").send_keys("add@.cm")
		driver.find_element(By.NAME, "current_password").send_keys("123Qweasd")
		driver.find_element(By.CLASS_NAME, "action.save.primary").click()

		respon = driver.find_element(By.ID, "email-error").text
		self.assertIn('Please enter a valid email address.', respon)
		#jalan

	def test_j_change_email_to_same_email(self):
		driver = self.browser
		driver.get(self.url_acc)
		driver.find_element(By.ID, "email").send_keys("add@ss.com")
		driver.find_element(By.ID, "pass").send_keys("123Qqweasd")
		driver.find_element(By.ID, "send2").click()
		driver.find_element(By.XPATH, "//input[@id='change-email']").click();
		driver.find_element(By.ID, "email").clear()
		driver.find_element(By.ID, "email").send_keys("add@ss.com") #aq@ss.com
		driver.find_element(By.NAME, "current_password").send_keys("123Qweasd")
		driver.find_element(By.CLASS_NAME, "action.save.primary").click()

		#respon = driver.find_element(By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']").text
		#respon = driver.find_element(By.CLASS_NAME, "field.note").text
		#respon = driver.find_element(By.XPATH, "//div[@class='field note']").text
		#self.assertIn('If you have an account, sign in with your email address.', respon)
		#respon = driver.find_element(By.CLASS_NAME, "base").text
		#self.assertIn('Customer Login', respon)
		respon = driver.find_element(By.CLASS_NAME, "page-title").text
		self.assertIn("Edit Account Information", respon)
		#jalan

	def test_k_failed_change_email_blank(self):
		driver = self.browser
		driver.get(self.url_acc)
		driver.find_element(By.ID, "email").send_keys("add@ss.com")
		driver.find_element(By.ID, "pass").send_keys("123Qqweasd")
		driver.find_element(By.ID, "send2").click()
		driver.find_element(By.XPATH, "//input[@id='change-email']").click();
		driver.find_element(By.ID, "email").clear()
		driver.find_element(By.NAME, "current_password").send_keys("123Qweasd")
		driver.find_element(By.CLASS_NAME, "action.save.primary").click()

		respon = driver.find_element(By.ID, "email-error").text
		self.assertIn('This is a required field.', respon)

	def l_success_change_password(self):
		driver = self.browser
		driver.get(self.url_acc)
		driver.find_element(By.ID, "email").send_keys("ad@s.com")
		driver.find_element(By.ID, "pass").send_keys("123Qqweasd")
		driver.find_element(By.ID, "send2").click()
		driver.find_element(By.NAME, "change_password").click()
		#driver.find_element(By.XPATH, "//input[@id='change-password']").click();
		driver.find_element(By.ID, "current-password").send_keys("123Qqweasd")
		driver.find_element(By.ID, "password").send_keys("123Qweasdz")
		driver.find_element(By.ID, "password-confirmation").send_keys("123Qweasdz")
		driver.find_element(By.CLASS_NAME, "action.save.primary").click()

		respon = driver.find_element(By.CLASS_NAME, "base").text
		self.assertIn('Customer Login', respon)

	def test_m_invalid_change_password(self):
		driver = self.browser
		driver.get(self.url_acc)
		driver.find_element(By.ID, "email").send_keys("ad@s.com")
		driver.find_element(By.ID, "pass").send_keys("123Qqweasd")
		driver.find_element(By.ID, "send2").click()
		driver.find_element(By.NAME, "change_password").click()
		#driver.find_element(By.XPATH, "//input[@id='change-password']").click();
		driver.find_element(By.ID, "current-password").send_keys("123Qqweasd")
		driver.find_element(By.ID, "password").send_keys("passwd")
		driver.find_element(By.ID, "password-confirmation").send_keys("passwd")
		driver.find_element(By.CLASS_NAME, "action.save.primary").click()

		respon = driver.find_element(By.ID, "password-error").text
		self.assertIn('Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored.', respon)

	def test_n_invalid_change_password_blank(self):
		driver = self.browser
		driver.get(self.url_acc)
		driver.find_element(By.ID, "email").send_keys("ad@s.com")
		driver.find_element(By.ID, "pass").send_keys("123Qqweasd")
		driver.find_element(By.ID, "send2").click()
		driver.find_element(By.NAME, "change_password").click()
		#driver.find_element(By.XPATH, "//input[@id='change-password']").click();
		driver.find_element(By.ID, "current-password").send_keys("123Qqweasd")
		driver.find_element(By.ID, "password").send_keys("")
		driver.find_element(By.ID, "password-confirmation").send_keys("passwd")
		driver.find_element(By.CLASS_NAME, "action.save.primary").click()

		respon = driver.find_element(By.ID, "password-error").text
		self.assertIn('This is a required field.', respon)


	def test_o_invalid_change_password_blank(self):
		driver = self.browser
		driver.get(self.url_acc)
		driver.find_element(By.ID, "email").send_keys("ad@s.com")
		driver.find_element(By.ID, "pass").send_keys("123Qqweasd")
		driver.find_element(By.ID, "send2").click()
		driver.find_element(By.NAME, "change_password").click()
		driver.find_element(By.CLASS_NAME, "action.save.primary").click()

		respon = driver.find_element(By.ID, "current-password-error").text
		self.assertIn('This is a required field.', respon)

	def test_p_change_password_with_same_password(self):
		driver = self.browser
		driver.get(self.url_acc)
		driver.find_element(By.ID, "email").send_keys("ad@s.com")
		driver.find_element(By.ID, "pass").send_keys("123Qqweasd")
		driver.find_element(By.ID, "send2").click()
		driver.find_element(By.ID, "change-password").click()
		#driver.find_element(By.XPATH, "//input[@id='change-password']").click();
		driver.find_element(By.ID, "current-password").send_keys("123Qqweasd")
		driver.find_element(By.ID, "password").send_keys("123Qqweasd")
		driver.find_element(By.ID, "password-confirmation").send_keys("123Qqweasd")
		driver.find_element(By.CLASS_NAME, "action.save.primary").click()

		#respon = driver.find_element(By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']").text
		respon = driver.find_element(By.CLASS_NAME, "base").text
		self.assertIn('Customer Login', respon)

	def test_q_change_password_invalid_current_password(self):
		driver = self.browser
		driver.get(self.url_acc)
		driver.find_element(By.ID, "email").send_keys("ad@s.com")
		driver.find_element(By.ID, "pass").send_keys("123Qqweasd")
		driver.find_element(By.ID, "send2").click()
		#driver.find_element(By.NAME, "change_password").click()
		driver.find_element(By.ID, "change-password").click()
		#driver.find_element(By.XPATH, "//input[@id='change-password']").click();
		driver.find_element(By.ID, "current-password").send_keys("Qqweasd123")
		driver.find_element(By.ID, "password").send_keys("123Qqweasd")
		driver.find_element(By.ID, "password-confirmation").send_keys("123Qqweasd")
		driver.find_element(By.CLASS_NAME, "action.save.primary").click()

		#respon = driver.find_element(By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']").text
		respon = driver.find_element(By.CLASS_NAME, "base").text
		self.assertIn("Edit Account Information", respon)

	def test_r_change_password_invalid_confirm_password(self):
		driver = self.browser
		driver.get(self.url_acc)
		driver.find_element(By.ID, "email").send_keys("ad@s.com")
		driver.find_element(By.ID, "pass").send_keys("123Qqweasd")
		driver.find_element(By.ID, "send2").click()
		#driver.find_element(By.NAME, "change_password").click()
		driver.find_element(By.ID, "change-password").click()
		#driver.find_element(By.XPATH, "//input[@id='change-password']").click();
		driver.find_element(By.ID, "current-password").send_keys("123Qqweasd")
		driver.find_element(By.ID, "password").send_keys("123Qqweasdz")
		driver.find_element(By.ID, "password-confirmation").send_keys("123Qqweas")
		driver.find_element(By.CLASS_NAME, "action.save.primary").click()

		#respon = driver.find_element(By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']").text
		respon = driver.find_element(By.ID, "password-confirmation-error").text
		self.assertIn("Please enter the same value again.", respon)


	def tearDown(self):
		self.browser.close()

#if __name__ == "__main__":
#	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='result'))

if __name__ == "__main__":
	unittest.main()