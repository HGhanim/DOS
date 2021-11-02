from flask import Flask

catalog_server = Flask(__name__)


def main():
    catalog_server.run(debug=True)

if __name__ == '__main__':
    main()