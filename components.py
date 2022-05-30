import csv
import time
from selenium import webdriver

# Driver path
chrome_driver_path = "C:\Development\chromedriver.exe"

class Customary:
    def __init__(self, feet, inches, pounds):
        # Store parameters
        self.feet = feet
        self.inches = inches
        self.pounds = pounds

        try:
            # Call driver and calculate BMI
            self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
            self.calculate_bmi()

            # Save BMI and send email, tweet, and end
            self.save_bmi()
            self.end()
        except:
            print("Invalid driver path or Chrome Driver version!")

    def calculate_bmi(self):
        # Open the site
        self.driver.get("https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/english_bmi_calculator/bmi_calculator.html")
        time.sleep(3)

        # Enter height (feet)
        enter_height_feet = self.driver.find_element_by_xpath('//*[@id="feet"]')
        enter_height_feet.send_keys(self.feet)
        time.sleep(3)

        # Enter height (inches)
        enter_height_inches = self.driver.find_element_by_xpath('//*[@id="inches"]')
        enter_height_inches.send_keys(self.inches)
        time.sleep(3)

        # Enter weight (lbs)
        enter_weight = self.driver.find_element_by_xpath('//*[@id="pounds"]')
        enter_weight.send_keys(self.pounds)
        time.sleep(3)

        # Calculate the BMI
        button = self.driver.find_element_by_xpath('//*[@id="calc"]')
        button.click()
        time.sleep(3)

    def save_bmi(self):
        # Calculate BMI
        converted_height = self.feet * 12 + self.inches
        calc = (self.pounds / (converted_height * converted_height)) * 703

        # Store values
        bmi = ""
        bmi_indication = ""
        healthy_weight_min = ""
        healthy_weight_max = ""

        # Get BMI and indications from BMI for underweight
        if calc < 18.5:
            bmi = self.driver.find_element_by_xpath('//*[@id="underweight"]/p[4]/strong[1]').text
            bmi_indication = self.driver.find_element_by_xpath('//*[@id="underweight"]/p[4]/strong[2]').text
            healthy_weight_min = self.driver.find_element_by_xpath('//*[@id="underweight"]/p[5]/strong[1]').text
            healthy_weight_max = self.driver.find_element_by_xpath('//*[@id="underweight"]/p[5]/strong[2]').text

        # Get BMI and indications from BMI for normal
        elif 18.5 <= calc < 25.0:
            bmi = self.driver.find_element_by_xpath('//*[@id="normal"]/p[4]/strong[1]').text
            bmi_indication = self.driver.find_element_by_xpath('//*[@id="normal"]/p[4]/strong[2]').text
            healthy_weight_min = self.driver.find_element_by_xpath('//*[@id="normal"]/p[5]/strong[1]').text
            healthy_weight_max = self.driver.find_element_by_xpath('//*[@id="normal"]/p[5]/strong[2]').text

        # Get BMI and indications from BMI for normal
        elif 25.0 <= calc < 30.0:
            bmi = self.driver.find_element_by_xpath('//*[@id="overweight"]/p[4]/strong[1]').text
            bmi_indication = self.driver.find_element_by_xpath('//*[@id="overweight"]/p[4]/strong[2]').text
            healthy_weight_min = self.driver.find_element_by_xpath('//*[@id="overweight"]/p[5]/strong[1]').text
            healthy_weight_max = self.driver.find_element_by_xpath('//*[@id="overweight"]/p[5]/strong[2]').text

        # Get BMI and indications from BMI for normal
        elif calc >= 30.0:
            bmi = self.driver.find_element_by_xpath('//*[@id="obese"]/p[4]/strong[1]').text
            bmi_indication = self.driver.find_element_by_xpath('//*[@id="obese"]/p[4]/strong[2]').text
            healthy_weight_min = self.driver.find_element_by_xpath('//*[@id="obese"]/p[5]/strong[1]').text
            healthy_weight_max = self.driver.find_element_by_xpath('//*[@id="obese"]/p[5]/strong[2]').text

        with open("bmi.csv", "a+", newline='', encoding="utf-8") as file:
            # Write title of columns
            column_titles = ['Unit', 'Height', 'Weight', 'BMI', 'Healthy weight range for height']
            writer = csv.writer(file)
            # writer.writerow(column_titles)

            # Write row
            row = ["Customary", f"{self.feet}ft, {self.inches}in", f"{self.pounds}lbs", f"{bmi} ({bmi_indication})", f"{healthy_weight_min}lbs - {healthy_weight_max}lbs"]
            writer.writerow(row)

    def end(self):
        # Quit program at end
        time.sleep(10)
        self.driver.quit()


class Metric:
    def __init__(self, height, weight):
        # Store parameters
        self.height = height
        self.weight = weight

        # Call driver and calculate BMI
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.calculate_bmi()

        # Save BMI and quit
        self.message = ""
        self.save_bmi()
        self.end()

    def twitter_login(self):
        pass

    def calculate_bmi(self):
        # Open the site
        self.driver.get("https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/english_bmi_calculator/bmi_calculator.html")
        time.sleep(3)

        # Change to metric
        metric = self.driver.find_element_by_xpath('//*[@id="calc_form"]/div[1]/div/div[2]/p/a')
        metric.click()
        time.sleep(3)

        # Enter height
        enter_height = self.driver.find_element_by_xpath('//*[@id="meters"]')
        enter_height.send_keys(self.height)
        time.sleep(3)

        # Enter weight
        enter_weight = self.driver.find_element_by_xpath('//*[@id="kilograms"]')
        enter_weight.send_keys(self.weight)
        time.sleep(3)

        # Call driver and calculate BMI
        button = self.driver.find_element_by_xpath('//*[@id="calc"]')
        button.click()
        time.sleep(3)

    def save_bmi(self):
        # Calculate BMI and store values from site
        calc = (self.weight / (self.height * self.height)) * 10000
        bmi = ""
        bmi_indication = ""
        healthy_weight_min = ""
        healthy_weight_max = ""

        # Get BMI and indications from BMI for underweight
        if calc < 18.5:
            bmi = self.driver.find_element_by_xpath('//*[@id="underweight"]/p[4]/strong[1]').text
            bmi_indication = self.driver.find_element_by_xpath('//*[@id="underweight"]/p[4]/strong[2]').text
            healthy_weight_min = self.driver.find_element_by_xpath('//*[@id="underweight"]/p[5]/strong[1]').text
            healthy_weight_max = self.driver.find_element_by_xpath('//*[@id="underweight"]/p[5]/strong[2]').text

        # Get BMI and indications from BMI for normal
        elif 18.5 <= calc < 25.0:
            bmi = self.driver.find_element_by_xpath('//*[@id="normal"]/p[4]/strong[1]').text
            bmi_indication = self.driver.find_element_by_xpath('//*[@id="normal"]/p[4]/strong[2]').text
            healthy_weight_min = self.driver.find_element_by_xpath('//*[@id="normal"]/p[5]/strong[1]').text
            healthy_weight_max = self.driver.find_element_by_xpath('//*[@id="normal"]/p[5]/strong[2]').text

        # Get BMI and indications from BMI for normal
        elif 25.0 <= calc < 30.0:
            bmi = self.driver.find_element_by_xpath('//*[@id="overweight"]/p[4]/strong[1]').text
            bmi_indication = self.driver.find_element_by_xpath('//*[@id="overweight"]/p[4]/strong[2]').text
            healthy_weight_min = self.driver.find_element_by_xpath('//*[@id="overweight"]/p[5]/strong[1]').text
            healthy_weight_max = self.driver.find_element_by_xpath('//*[@id="overweight"]/p[5]/strong[2]').text

        # Get BMI and indications from BMI for normal
        elif calc >= 30.0:
            bmi = self.driver.find_element_by_xpath('//*[@id="obese"]/p[4]/strong[1]').text
            bmi_indication = self.driver.find_element_by_xpath('//*[@id="obese"]/p[4]/strong[2]').text
            healthy_weight_min = self.driver.find_element_by_xpath('//*[@id="obese"]/p[5]/strong[1]').text
            healthy_weight_max = self.driver.find_element_by_xpath('//*[@id="obese"]/p[5]/strong[2]').text

        # Build message and send message
        self.message = f"Here's your BMI Calculator results: \n" \
                       f"\tHeight: {self.height}cm\n" \
                       f"\tWeight: {self.weight}kg\n" \
                       f"\tBMI: {bmi} ({bmi_indication})\n" \
                       f"\tHealthy weight range for height: {healthy_weight_min}kg - {healthy_weight_max}kg"

        with open("bmi.csv", "a", newline='', encoding="utf-8") as file:
            # Write title of columns
            # column_titles = ['Unit', 'Height', 'Weight', 'BMI', 'Healthy weight range for height']
            writer = csv.writer(file)

            # Write row
            row = ["Metric", f"{self.height}cm", f"{self.weight}kg", f"{bmi} ({bmi_indication})", f"{healthy_weight_min}kg - {healthy_weight_max}kg"]
            writer.writerow(row)

    def end(self):
        # Quit program at end
        time.sleep(10)
        self.driver.quit()