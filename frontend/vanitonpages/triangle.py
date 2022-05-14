from selenium import webdriver
from selenium.webdriver.common.by import By

class Triangle:
    def __init__(self):
        self.driver = None

    def start_chrome_driver(self) -> None:
        """
        Description:
        Set chrome as navigator
        
        :return:    (WebDriver) implicit return, set chrome has default
        """
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=webdriver.ChromeOptions())

    def start_firefox_driver(self) -> None:
        """
        Description:
        Set firefox as navigator
        
        :return:    (WebDriver) implicit return, set firefox has default
        """
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=webdriver.FirefoxOptions())
    
    def start_edge_driver(self) -> None:
        """
        Description:
        Set edge as navigator
        
        :return:    (WebDriver) implicit return, set edge has default
        """
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=webdriver.EdgeOptions())

    def stop_driver(self) -> None:
        """
        Description:
        Stop selenium browser
        """
        self.driver.quit()

    def open_page(self, website_url: str) -> None:
        """
        Description:
        Access the page provided
        
        Parameters:
        :website_url: (str) url page
        """
        self.driver.get(website_url)

    def set_input_fields(self, insert_text: list) -> None:
        """
        Description:
        Insert values on input fields and press on submit button
        
        Parameters:
        :insert_text: (list(str)) three texts for insert on inputs
        """
        
        input1 = self.driver.find_element(By.NAME, 'V1')
        input2 = self.driver.find_element(By.NAME, 'V2')
        input3 = self.driver.find_element(By.NAME, 'V3')
        
        button_path = "//input[@type='submit' and @value='Identificar']"
        submit_b = self.driver.find_element(By.XPATH, button_path)
        
        input1.send_keys(insert_text[0])
        input2.send_keys(insert_text[1])
        input3.send_keys(insert_text[2])
        
        submit_b.click()
    
    def sleep(self, time:int) -> None:
        """
        Description:
        Waits a preset time (similar to sleep function for python)
        
        Parameters:
        :time: (int) time in seconds
        """
        self.driver.implicitly_wait(time)

    def __check_if_exist(self, elements: list) -> bool:
        """
        Description:
        A searched element may not exist, this function check if list
        is empty, in affirmative case, return false, else, true
        
        Parameters:
        :elements: (list) alleged elements

        :return:    (bool) resp if exist values in list
        
        OBS: Unused function, because is not necessary, but it is right
        way to do it
        """
        return True if (len(elements) > 0) else False

    def get_divs_values(self) -> list:
        """
        Description:
        Try get all texts of the div's (find_elements is the security
        way to check if tag exist on document, him return empty list if
        tag not exist)
        
        :return:    (list) list with founds texts
        
        OBS: Unused function, because is not necessary, but it is right
        way to do it
        """
        divs = self.driver.find_elements(By.TAG_NAME, "div")

        if (self.__check_if_exist(divs)):
            divs_text = [div.text for div in divs]
            return divs_text

        return []

    def get_body_last_value(self) -> str:
        """
        Description:
        In all cases, the output resp is the last text of file, get it
        
        :return:    (str) resp text
        """
        body = self.driver.find_element(By.TAG_NAME, 'body')
        
        return body.text.split('\n')[-1]

    def builder(self, browser: str, url: str, input: list) -> None:
        """
        Description:
        A builder function that simplifies the call methods to run
        simple example.
        
        Parameters:
        :browser: (str) the browser you want
        :insert_text: (list(str)) three texts for insert on inputs
        :website_url: (str) url page

        :return:    (bool) resp if exist values in list
        """
        if browser == 'firefox':
            self.start_firefox_driver()
        elif browser == 'chrome':
            self.start_chrome_driver()
        elif browser == 'edge':
            self.start_edge_driver()
        else:
            exit()

        self.open_page(url)

        self.set_input_fields(input)

        print(self.get_body_last_value())

        self.stop_driver()
