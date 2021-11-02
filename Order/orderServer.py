from flask import Flask
import pandas as pd

order_server = Flask(__name__)

def main():
    order_server.run(debug=True)

if __name__ == '__main__':
    main()