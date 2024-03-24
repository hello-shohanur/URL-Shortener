import pyshorteners


def shorten_url(url):

    # Initialize a Shortener object
    shortener = pyshorteners.Shortener()

    # Shorten the URL
    shortened_url = shortener.tinyurl.short(url)

    return shortened_url


if __name__ == "__main__":
    original_url = input("Enter a URL: ")
    shortened_url = shorten_url(original_url)
    print("Shortened URL is:", shortened_url)
