import random
import string
from time import sleep
from seleniumbase import BaseCase

class HomeTest(BaseCase):
    def generate_random_text(self, length=10):
        """Generate random alphanumeric text."""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def generate_email(self):
        """Generate a random email address ending with @gmail.com."""
        prefix = self.generate_random_text(length=8)
        return f"{prefix}@gmail.com"

    def generate_password(self, length=12):
        """Generate a random password with at least one capital letter."""
        characters = string.ascii_lowercase + string.digits
        password = ''.join(random.choice(characters) for _ in range(length - 1))
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
        # Ensure at least one capital letter
        return password + random.choice(string.ascii_uppercase)+ random.choice(string.ascii_lowercase)+random.choice(string.digits) + random.choice(symbols) + random.choice(string.ascii_letters)

    def test_home_page(self):
        # Open the page
        self.open("https://mcitcareerssd.elevatus.io/")

        # Generate data for text fields
        random_text1 = self.generate_random_text(10)
        random_text2 = self.generate_random_text(10)
        random_email = self.generate_email()
        random_password = self.generate_password(12)
        confirmation_password = random_password
       # print(random_password)

        # Accept cookies
        self.click("/html/body/div[3]/div/div[2]/div[1]/div[4]/button[1]")
        first_url = self.get_current_url()
        self.assert_equal(first_url, "https://mcitcareerssd.elevatus.io/")

        # Click Register
        self.click('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[5]/button[2]/span[1]')
        sleep(5)
        second_url = self.get_current_url()
        self.assert_equal(second_url, "https://mcitcareerssd.elevatus.io/register")

        # Fill the fields
        self.send_keys("input[placeholder='First name']", random_text1)
        self.send_keys("input[placeholder='Last name']", random_text2)
        self.send_keys("input[placeholder='Email']", random_email)
        self.send_keys("input[placeholder='Password']", random_password)
        self.send_keys("input[placeholder='Confirm Password']", confirmation_password)

        # Click checkbox
        self.click("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[7]/label[1]")
        self.click("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[8]/button[1]")

        # Click Jobs
        self.click("/html[1]/body[1]/div[1]/header[1]/div[2]/div[1]/div[2]/div[2]/div[2]/button[1]/div[1]")
        # Click View
        self.click("/html[1]/body[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]/span[1]")
        # Click Apply
        self.click("/html[1]/body[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[6]/button[1]")
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


