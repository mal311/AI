import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time

# Initialize colorama
init(autoreset=True)

# Load and preprocess the dataset
def load_data():
    try:
        df = pd.read_csv(r"D:\AI\lesson 6\imdb_top_1000.csv")
        df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file 'imdb_top_1000.csv' was not found.")
        exit()

movies_df = load_data()

# Vectorize the combined features and compute cosine similarity
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# List all unique genres
def list_genres(df):
    return sorted(set(genre.strip() for sublist in df['Genre'].dropna().str.split(', ') for genre in sublist))

genres = list_genres(movies_df)

# Recommend movies based on filters (genre, mood, rating)
def recommend_movies(genre=None, mood=None, rating=None, top_n=5):
    filtered_df = movies_df
    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]
    if rating:
        filtered_df = filtered_df[filtered_df['IMBD_Rating'] >= rating]
    
    filtered_df = filtered_df.sample(frac=1).reset_index(drop=True) # Randomize the order

# Display recommendations 🍿     
def display_recommendations(recs, name):
    print(Fore.YELLOW + f"\n🍿 AI-Analysed movie recommendation for {name} :")
    for idx, (title, polarity) in enumerate(recs, 1):
        sentiment = "Positive 😊" if polarity > 0 else "Negative😞" if polarity < 0 else "Neutral"
        print(f"{Fore.CYAN}{idx}  🎥 {title} (polarity: {.2f}, {sentiment})")

# Small processing animation
def processing_animation():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

# Handle AI recommendation flow 🔍
def handle_ai(name):
    # Show genres in a single line


    # Processing animation while analyzing mood 😊  😞  😐

        # Small processing animation during mood analysis
    
    # Processing animation while finding movies
    
      # Small processing animation while finding movies 🎬🍿

   
# Main program 
def main():
    print(Fore.BLUE + "🎥 Welcome to your Personal Movie Recommendation Assistant! 🎥\n")
    name = input(Fore.YELLOW + "What's your name? ").strip()

    print(f"\n{Fore.GREEN}Great to meet you, {name}!\n")
    handle_ai(name)

if __name__ == "__main__":
    main()