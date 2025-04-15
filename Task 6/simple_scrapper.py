import requests  # To send HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML
from rich.console import Console  # For styled console output
from rich.table import Table  # For displaying data in a table format

# Create a styled console instance
console = Console()

def fetch_page(url):
    """
    Fetches the HTML content of the given URL.
    """
    try:
        # Send a GET request to the URL with a user-agent header
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad responses (e.g., 404)
        return response.text  # Return HTML content
    except Exception as e:
        # Handle errors like timeouts, connection issues, etc.
        console.print(f"[red]❌ Error fetching page:[/red] {e}")
        return None

def scrape_data(html, tag, class_name=None):
    """
    Extracts text data from the specified HTML tag and class.
    """
    soup = BeautifulSoup(html, 'html.parser')  # Parse HTML
    if class_name:
        # Find elements by tag and class name
        elements = soup.find_all(tag, class_=class_name)
    else:
        # Find elements by tag only
        elements = soup.find_all(tag)
    # Extract and clean text from each element
    return [el.get_text(strip=True) for el in elements]

def display_results(data):
    """
    Displays the scraped data in a table using Rich.
    """
    if not data:
        console.print("[yellow]⚠️ No data found.[/yellow]")
        return
    
    # Create a table with two columns
    table = Table(title="Scraped Data")
    table.add_column("No.", style="cyan", justify="right")
    table.add_column("Content", style="green")

    # Add each scraped item as a row
    for i, item in enumerate(data, start=1):
        table.add_row(str(i), item)
    
    # Print the table to the console
    console.print(table)

def main():
    """
    Main program logic: Get user input, scrape website, and display results.
    """
    console.print("[bold blue]🌐 Simple Web Scraper[/bold blue]")

    # Get URL and HTML selector details from the user
    url = input("Enter the full URL (e.g., https://example.com): ").strip()
    tag = input("Enter the HTML tag to scrape (e.g., h1, p, span): ").strip()
    class_name = input("Optional: Enter the class name (or leave blank): ").strip()
    class_name = class_name if class_name else None  # Convert empty string to None

    # Fetch and parse the web page
    html = fetch_page(url)
    if html:
        # Scrape and display results
        data = scrape_data(html, tag, class_name)
        display_results(data)

# Run the script only when it is executed directly
if __name__ == "__main__":
    main()
