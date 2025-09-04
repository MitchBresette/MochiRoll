 Random Anime Generator - https://mochiroll.net/ 

MochiROll is a Django web application that uses the MyAnimeList API to fetch the top 4000 anime titles.  
Users can roll a random anime and save it to their personal watchlist after creating an account.

- Fetches anime data from MyAnimeList and stores it locally in a JSON file.  
- Randomly selects titles and displays their names and images.  
- Uses Django’s built-in authentication for account creation and login.  
- User data is stored in an ephemeral SQLite database so demo users can try adding items without long-term persistence.   


- Hosted on Google Cloud Run with custom DNS management.  
- Built with Python 3.10 and Django
