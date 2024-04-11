from utils import calculate_pizza_cost
import requests
from bs4 import BeautifulSoup


def fetch_webpage(url):
    """
    Fetches the content of a webpage.

    Parameters:
    - url (str): The URL of the webpage to fetch.

    Returns:
    - str: The HTML content of the webpage.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_webpage(html):
    """
    Parses the HTML content of a webpage and extracts the title.

    Parameters:
    - html (str): The HTML content of the webpage.

    Returns:
    - str: The title of the webpage.
    """
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string if soup.title else 'No title found'
    return title


def main():
    price_per_size = {'small': 5.99, 'medium': 7.99, 'large': 9.99}
    total_cost = 0.0

    try:
        number_of_pizzas = int(input("Enter the number of pizzas: "))
        for i in range(number_of_pizzas):
            size = input(f"Enter size for pizza {i + 1} (small, medium, large): ").lower()
            total_cost += calculate_pizza_cost(size, price_per_size)

        print(f"Total cost of the order: ${total_cost:.2f}")

        # Example of using requests and BeautifulSoup
        url = input("Enter a URL to fetch its title: ")
        html_content = fetch_webpage(url)
        if html_content:
            title = parse_webpage(html_content)
            print(f"The title of the webpage is: {title}")
        else:
            print("Failed to fetch the webpage.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
