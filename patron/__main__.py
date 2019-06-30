import sys

from patron import app


def start():
    print('[+] API ON')
    app.run(port=sys.argv[1], debug=sys.argv[2])


if __name__ == '__main__':
    start()
