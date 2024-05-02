#!/usr/bin/env python3
import argparse
import pytest
import sys
from dotenv import set_key

def setup(args):
    """
    Sets up the environment variables for the test.

    Args:
        args (Namespace): The command line arguments containing the username, password, and base URL.
    """
    env_path = '.env'
    set_key(env_path, "TEST_USERNAME", args.username)
    set_key(env_path, "TEST_PASSWORD", args.password)
    set_key(env_path, "TEST_BASE_URL", args.base_url)

def run(args):
    # Run pytest and pass the additional arguments
    sys.exit(pytest.main(args.pytest_args))

def main():
    parser = argparse.ArgumentParser(description="Run pytest with environment variables and additional arguments.")
    subparsers = parser.add_subparsers(help="commands", dest="command")
    subparsers.required = True  # Python 3.7 and above needs this to ensure a subparser is always specified

    # Subparser for setup
    setup_parser = subparsers.add_parser("setup", help="Setup the test environment")
    setup_parser.add_argument("--username", type=str, required=True, help="Username for the test environment")
    setup_parser.add_argument("--password", type=str, required=True, help="Password for the test environment")
    setup_parser.add_argument("--base-url", type=str, required=True, help="Base URL for the test environment")
    setup_parser.set_defaults(func=setup)

    # Subparser for run
    run_parser = subparsers.add_parser("run", help="Run tests")
    run_parser.add_argument("test_type", choices=["api"], help="Type of tests to run")
    run_parser.add_argument("-m", "--mode", help="Mode for the tests")
    run_parser.add_argument("pytest_args", nargs=argparse.REMAINDER, help="Arguments to pass to pytest")
    run_parser.set_defaults(func=run)

    # Parse arguments and call the appropriate function
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
