from tkinter import *
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

bd_connection = mysql.connector.connect(host=os.getenv("HOST"),
                                        user=os.getenv("USER"),
                                        password=os.getenv("PASSWORD"),
                                        database=os.getenv("DATABASE_NAME"))

