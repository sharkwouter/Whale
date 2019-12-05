#!/usr/bin/env python3
from controllers import server

if __name__ == "__main__":
    server.run(reloader=True, debug=True)
