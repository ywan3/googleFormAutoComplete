from form_fillers import *
from google_login import *
import config
from selenium import webdriver
import pandas as pd
import time
import json
from datetime import datetime
import pathlib
import glob
import sys
sys.path.append(".")
import faker
import numpy as np
import pandas as pd


name_element_class = "rFrNMe k3kHxc RdH0ib yqQS1 zKHdkd"
choice_element_class = "Od2TWd hYsg7c"
date_element_class = "whsOnd zHQkBf"
submit_element_class = "uArJ5e UQuaGc Y5sE8d VkkpIf QvWxOd"
driver = webdriver.Chrome()

if __name__ == '__main__':
    google_login_handler(driver)
    driver_process(driver, name_element_class, choice_element_class, date_element_class, submit_element_class)