import random
import time
import os
from colorama import init, Fore, Style

init(autoreset=True)
max_attempts = 9

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display(word, guessed):
    return ' '.join([ch if guessed[i] else '_' for i, ch in enumerate(word)])

def word_guessed(guessed):
    return all(guessed)

def draw_hangman(attempts_left):
    parts = [
        " _______\n",
        "|/      |\n",
        f"|      {'( )' if attempts_left <= 7 else ''}\n",
        f"|      {'/' if attempts_left <= 6 else ' '}{'|' if attempts_left <= 5 else ' '}{'\\' if attempts_left <= 4 else ' '}\n",
        f"|       {'|' if attempts_left <= 3 else ''}\n",
        f"|      {'/' if attempts_left <= 2 else ' '}{' \\' if attempts_left <= 1 else ''}\n",
        "|\n_|___\n"
    ]
    return ''.join(parts)

def animation():
    frames = [
        """
         _______
        |/      |
        |
        |
        |
        |
        |
       _|___
        """,
        """
         _______
        |/      |
        |      ( )
        |
        |
        |
        |
       _|___
        """,
        """
         _______
        |/      |
        |      ( )
        |       |
        |
        |
        |
       _|___
        """,
        """
         _______
        |/      |
        |      ( )
        |      /|
        |
        |
        |
       _|___
        """,
        """
         _______
        |/      |
        |      ( )
        |      /|\\
        |
        |
        |
       _|___
        """,
        """
         _______
        |/      |
        |      ( )
        |      /|\\
        |       |
        |
        |
       _|___
        """,
        """
         _______
        |/      |
        |      ( )
        |      /|\\
        |       |
        |      /
        |
       _|___
        """,
        """
         _______
        |/      |
        |      ( )
        |      /|\\
        |       |
        |      / \\
        |
       _|___
        """
    ]
    for frame in frames:
        clear()
        print(Fore.RED + Style.BRIGHT + frame)
        time.sleep(0.5)
    print(Fore.RED + Style.BRIGHT + "\n💀 Out of attempts! The Hangman is dead\n")
    time.sleep(1)

def load_high_score():
    if not os.path.exists("highscore.txt"):
        return 0
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except ValueError:
        return 0

def save_high_score(new_score):
    with open("highscore.txt", "w") as file:
        file.write(str(new_score))

def main():
    words_data = {
        "Movies/Series": (
            ["Bahubali", "Starwars", "HarryPotter", "LordOfTheRings", "KGF", "MoneyHeist", "BreakingBad", "PeakyBlinders"],
            ["Epic movie", "Sci-fi classic", "Wizard boy", "Fantasy saga", "Rocky film", "Spanish heist series", "Chemistry teacher", "British gangsters"]
        ),
        "Sports": (
            ["Football", "Cricket", "Rugby", "Hockey", "Volleyball", "Basketball", "Badminton", "SRH", "CSK", "MI", "KKR", "DC", "RCB", "ManchesterUnited"],
            ["Most popular game", "Gentleman's game", "Oval ball", "Stick and puck", "Net game", "Court game", "Shuttle game", "IPL team", "IPL team", "IPL team", "IPL team", "IPL team", "IPL team", "Premier League team"]
        ),
        "Famous Personalities": (
            ["AbdulKalam", "Hitler", "ViratKholi", "Dhoni", "Sachin", "MikeTyson", "MuhammadAli", "LeBronJames", "Messi", "Ronaldo", "Neymar", "Einstein", "Tesla", "CVRaman", "Oppenheimer"],
            ["Missile Man", "German Dictator", "Indian cricketer", "Captain Cool", "Master Blaster", "Boxing legend", "Boxing legend", "Basketball icon", "GOAT in football", "Portuguese footballer", "Brazilian footballer", "Relativity scientist", "Inventor of AC", "Nobel laureate", "Manhattan Project leader"]
        ),
        "Places": (
            ["Hyderabad", "Golconda", "Udaipur", "Jaisalmer", "Amritsar", "Mysore", "Jaipur", "NewYork", "Germany", "Hiroshima", "Nagasaki", "WashingtonDC", "Barcelona", "Rome"],
            ["City in India", "Famous fort", "City of lakes", "Golden city", "Golden Temple city", "City of palaces", "Pink city", "Big Apple", "European country", "Bombed in WWII", "Bombed in WWII", "US capital", "City of Gaudí", "Ancient empire city"]
        ),
        "People from Class": (
            ["Saad", "Manideep", "Vedaditya", "Prahalad", "SaiCharan", "Rakesh", "Umesh", "Siddesh", "Aravind", "Lokesh"],
            ["Topper", "Dancer", "Topper", "Tall Guy", "Topper", "Tall Guy", "National kho-kho player", "CR", "Free fire player", "Ex - CR"],
            {
                "Saad": "Saad is 6 ft tall, but no one knows it.",
                "Manideep": "Did you know? With 2,403 followers on Instagram, his most viewed reel hit 152K views.",
                "Vedaditya": "Did you know? Vedaditya cracked his way to the top 7 in a local Rubik's Cube showdown.",
                "Umesh": "He's a national-level kho-kho player, and has amazing handwriting.",
                "SaiCharan": "Did you know? KV is a big fan of the cricketer Benstokes.",
                "Rakesh": "Did you know? Rakesh is a big fan of MMA."
            }
        )
    }

    score = 0
    high_score = load_high_score()
    playagain = True
    while playagain:
        print(Fore.CYAN + Style.BRIGHT + "\nChoose a category:")
        for i, category in enumerate(words_data.keys(), start=1):
            print(f"{i}. {category}")
        choice = input(Fore.LIGHTYELLOW_EX + "Enter your choice (1-5): ")

        try:
            category_key = list(words_data.keys())[int(choice) - 1]
        except (ValueError, IndexError):
            print(Fore.RED + "Invalid choice.")
            return

        data = words_data[category_key]
        word_list = data[0]
        hint_list = data[1]
        fact_dict = data[2] if len(data) > 2 else None

        index = random.randint(0, len(word_list) - 1)
        word = word_list[index]
        hint = hint_list[index]

        guessed = [0] * len(word)
        attempts_left = max_attempts
        used_letters = set()
        clear()
        print(Fore.YELLOW + Style.BRIGHT + "\n🔤 Starting the Hangman Game!")
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Current High Score:", high_score,Fore.LIGHTGREEN_EX + Style.BRIGHT +"Can you beat it?")

        while attempts_left > 0 and not word_guessed(guessed):
            print("\n" + Fore.MAGENTA + "Word:", display(word, guessed))
            print(Fore.BLUE + f"Attempts left: {attempts_left}")
            print(draw_hangman(attempts_left))

            if attempts_left == 3:
                print(Fore.CYAN + f"Hint: {hint}")

            guess = input(Fore.GREEN + "Guess a letter: ").strip().lower()
            if not guess or not guess.isalpha() or len(guess) != 1:
                print(Fore.RED + "Invalid input. Please enter a single letter.")
                continue
            if guess in used_letters:
                print(Fore.RED + "Already guessed that letter.")
                continue
            used_letters.add(guess)

            found = False
            for i, ch in enumerate(word):
                if ch.lower() == guess:
                    guessed[i] = 1
                    found = True

            if found:
                print(Fore.GREEN + "✅ Good guess!")
            else:
                print(Fore.RED + "❌ Wrong guess!")
                attempts_left -= 1

        if word_guessed(guessed):
            print(Fore.GREEN + Style.BRIGHT + f"\n🎉 Congratulations! You guessed the word: {word}")
            score += 1
            print(Fore.LIGHTMAGENTA_EX + "Total Score:", score)
        else:
            animation()
            if score > high_score:
                print("🔥 New High Score!")
                save_high_score(score)
                high_score = score
            print(Fore.RED + Style.BRIGHT + f"The word was: {word}")
            print(Fore.LIGHTMAGENTA_EX + "Final Score:", score)
            print(Fore.MAGENTA + Style.BRIGHT + "High Score:", high_score)
        if fact_dict and word in fact_dict:
            print(Fore.LIGHTCYAN_EX + f"📚 Fun Fact: {fact_dict[word]}")

        again = input(Fore.CYAN + "\nDo you want to play again? (y/n): ").strip().lower()
        if score > high_score:
            print("🔥 New High Score!")
            save_high_score(score)
            high_score = score
            print(Fore.MAGENTA + Style.BRIGHT + "New High Score:", high_score)
        if again != 'y':
            playagain = False
            print(Fore.LIGHTMAGENTA_EX + "Final Score:", score)
            print(Fore.MAGENTA + Style.BRIGHT + "High Score:", high_score)
            print(Fore.YELLOW + "Thanks for playing! Goodbye 👋")
main()