import random
import string
from time import sleep
from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys
from page_objects.home_page import HomePage


class HomeTest(BaseCase):
    def generate_random_text(self, length=10):
        """Generate random alphanumeric text."""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def generate_random_email(self):
        """Generate a random email with a unique identifier after the '+' sign."""
        random_numbers = ''.join(random.choices(string.digits, k=random.randint(2, 4)))
        return f"a.essam+{random_numbers}@elevatus.io"

    def generate_random_password(self, length=16):
        """Generate a secure password that meets all the specified criteria."""
        if length < 4:
            raise ValueError("Password length must be at least 4 to include all required character types.")

        # Ensure the password has at least one of each required character type
        lower = random.choice(string.ascii_lowercase)
        upper = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        symbol = random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?/~`")

        # Fill the rest of the password length with random characters
        remaining_length = length - 2
        remaining = ''.join(
            random.choices(
                string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?/~`" + string.ascii_uppercase + string.ascii_lowercase,
                k=remaining_length))

        # Combine all characters and shuffle
        password = lower + upper + digit + symbol + remaining
        #password = ''.join(random.sample(password, len(password)))  # Shuffle to avoid predictable pattern
        return password

    def test_home_page(self):
        # Open the page
        self.open(HomePage.link_site)

        # Generate data for text fields
        random_text1 = self.generate_random_text(10)
        random_text2 = self.generate_random_text(10)
        random_email = self.generate_random_email()
        random_password = self.generate_random_password(14)
        confirmation_password = random_password

        print(random_password)

        # Accept cookies
        self.click(HomePage.link_accept_cookies)
        first_url = self.get_current_url()
        self.assert_equal(first_url, HomePage.second_url)

        # Click Register
        self.click(HomePage.register_button)
        sleep(10)
        second_url = self.get_current_url()
        self.assert_equal(second_url, HomePage.second_url_2)

        # Fill the fields
        self.send_keys(HomePage.rand1, random_text1)
        self.send_keys(HomePage.rand2, random_text2)
        self.send_keys(HomePage.mail, random_email)
        self.send_keys(HomePage.password, random_password)
        self.send_keys(HomePage.confirm_pass, confirmation_password)

        # Click checkbox
        self.click(HomePage.checkbox1)
        self.click(HomePage.checkbox2)

        #Verify Mail
        self.open(
            HomePage.veri_mail)
        self.send_keys(
            HomePage.me_mail,
            'a.essam@elevatus.io')
        self.click(HomePage.login_button)
        self.send_keys(
            HomePage.me_pass,
            'GokuBenzemaBale-09')
        self.click(HomePage.me_login)
        sleep(10)
        #self.click("div:contains('nidalcc - You have been successfully registered!')")
        self.click(
            HomePage.word_click)
        self.click("a:contains('Click Here')")  # Click on link containing 'Welcome'
        sleep(10)

        # Click Jobs
        #self.click("/html/body/div[1]/header/div[2]/div[1]/div[2]/div[2]/div[2]/button/div")
        #self.click("/html/body/div[1]/div[2]/div/div[2]/div[7]/button[2]/span[1]")
        #self.click("/html[1]/body[1]/div[1]/header[1]/div[2]/div[1]/div[2]/div[2]/div[2]/button[1]/div[1]")
        #self.click("/html/body/div[1]/header/div[2]/div[1]/div[2]/div[2]/div[2]/button/div")
        #self.click('/html/body/div[1]/header/div[2]/div[1]/div[2]/div[2]/div[2]/button/div')
        #self.click('/html[1]/body[1]/div[1]/header[1]/div[2]/div[1]/div[2]/div[2]/div[2]/button[1]')
        self.open(HomePage.link_site2)

        # Click View
        self.click(HomePage.view_click)
        # Click Apply
        self.click(HomePage.apply_click)
        #Fill data
        #Calendar Press
        #self.click("/html/body/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div[3]/div[2]/div/div/div/div/div/div/div/button/svg")
        #self.click("/html/body/div[5]/div[2]/div/div/div/div[1]/div[1]/div/div")
        #self.click("/html/body/div[5]/div[2]/div/div/div/div[2]/div/div/div[105]/button")
        self.send_keys(
            HomePage.calendar1_click,
            "1990-03-15")
        #Gender
        #self.click("/html/body/div[5]/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[1]/button[1]")
        #self.select_option_by_index("gender", 2)
        self.send_keys(
            HomePage.gender,
            "Male" + Keys.ENTER)
        self.send_keys(HomePage.nationality,
                       "Egyptian" + Keys.ENTER)
        self.send_keys(HomePage.location,
                       "Nasr City Cairo Egypt")

        #Upload
        file_path = './data/Ahmad_Essam_CV.pdf'
        #self.choose_file('#basic-info > div.bg-white.section-card-body.card-body > div > div.mt-1.mb-3.row > div > div > div > p > span > span:nth-child(2', 'E:\CV')
        #self.choose_file('body > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)', file_path)
        #self.choose_file('body > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)',r"E:\CV\Ahmad_Essam_CV")
        self.execute_script("document.querySelector('input[type=\"file\"]').style.display = 'block';")
        self.choose_file("body > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)]", r"E:\CV\Ahmad_Essam_CV")

        sleep(10)
        self.click("/html/body/div[1]/div[2]/div/div[2]/div[7]/button[2]")
        self.click("/html/body/div[4]/div[3]/div/form/div/div[2]/div/div[2]/button/span[1]")
        sleep(5)

        if __name__ == "__main__":
            import pytest
            pytest.main([
                __file__,
                "--html=report.html",
                "--dashboard",
                "--log-path=logs/",
                "--headless",
                "-v"
            ])
