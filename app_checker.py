import requests

# Define the application URL you want to check
APP_URL = "https://www.google.com"


def check_application_health(url):
  print(f"Checking uptime and health for: {url}...")

  try:
    # Send a web request with a 5-second timeout
    response = requests.get(url, timeout=5)

    # If status code is 200, the app is functioning correctly ('up')
    if response.status_code == 200:
      print(f"Status: UP")
      print(
          "Details: Application is functioning correctly. (HTTP Status Code:"
          f" {response.status_code})"
      )
    else:
      print(f"Status: DOWN[span_7](start_span)[span_7](end_span)")
      print(
          "Details: Application returned an unexpected status code:"
          f" {response.status_code}"
      )

  except requests.exceptions.ConnectionError:
    print(f"Status: DOWN[span_8](start_span)[span_8](end_span)")
    print(
        "Details: Could not connect to the server. The application is offline"
        " or unavailable."
    )
  except requests.exceptions.Timeout:
    print(f"Status: DOWN[span_9](start_span)[span_9](end_span)")
    print(
        "Details: The request timed out. The application is not responding."
    )


if __name__ == "__main__":
  check_application_health(APP_URL)
  input("press enter to exit...")