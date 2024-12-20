#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <ctype.h>
const int max_attempts = 9;

void display(char word[], int guessed[]);
int wordG(int guessed[], int length);
void draw(int left);
int main() {
    int playagain = 1;
    while (playagain) 
    {
        char *ms[] = {"Bahubali", "Starwars", "HarryPotter", "LordOfTheRings", "KGF", "MoneyHeist", "BreakingBad", "PeakyBlinders"};
        char *sports[] = {"Football", "Cricket", "Rugby", "Hockey", "Volleyball", "Basketball", "Badminton", "SRH", "CSK", "MI", "KKR", "DC", "RCB", "ManchesterUnited"};
        char *famous[] = {"AbdulKalam", "Hitler", "ViratKholi", "Dhoni", "Sachin", "MikeTyson", "MuhammadAli", "LeBronJames", "Messi", "Ronaldo", "Neymar", "Einstein", "Tesla", "CVRaman", "Oppenheimer"};
        char *places[] = {"Hyderabad", "Golconda", "Udaipur", "Jaisalmer", "Amritsar", "Mysore", "Jaipur", "NewYork", "Germany", "Hiroshima", "Nagasaki", "WashingtonDC", "Barcelona", "Rome"};
        char *people[] = {"Saad", "Manideep", "Vedaditya", "Prahalad", "SaiCharan", "Rakesh", "Umesh", "Siddesh", "Aravind", "Lokesh"};

        char *msHints[] = {"Epic movie", "Sci-fi classic", "Wizard boy", "Fantasy saga", "Gold Mine", "Spanish heist series", "Chemistry teacher", "British gangsters"};
        char *sportsHints[] = {"Most popular game", "Gentleman's game", "Oval ball", "Stick and puck", "Net game", "Court game", "Shuttle game", "IPL team", "IPL team", "IPL team", "IPL team", "IPL team", "IPL team", "Premier League team"};
        char *famousHints[] = {"Missile Man", "German Dictator", "Indian cricketer", "Captain Cool", "Master Blaster", "Boxing legend", "Boxing legend", "Basketball icon", "GOAT in football", "Portuguese footballer", "Brazilian footballer", "Relativity scientist", "Inventor of AC", "Nobel laureate", "Father Of the Atomic Bomb"};
        char *placesHints[] = {"City in India", "Famous fort", "City of lakes", "Golden city", "Golden Temple city", "City of palaces", "Pink city", "Big Apple", "European country", "Bombed in WWII", "Bombed in WWII", "US capital", "City of Gaudí", "Ancient empire city"};
        char *peopleHints[] = {"Topper", "Dancer", "Topper", "Tall Guy", "Topper", "Tall Guy", "National kho-kho player", "CR", "Free fire player", "Ex - CR"};

        char **words;
        char **hints;
        int wc;

        int category;
        printf("Choose a category:\n1. Movies/Series\n2. Sports\n3. Famous Personalities\n4. Places\n5. People from our class\nEnter your choice: ");
        scanf("%d", &category);

        switch (category) {
            case 1:
                words = ms;
                hints = msHints;
                wc = sizeof(ms) / sizeof(ms[0]);
                break;
            case 2:
                words = sports;
                hints = sportsHints;
                wc = sizeof(sports) / sizeof(sports[0]);
                break;
            case 3:
                words = famous;
                hints = famousHints;
                wc = sizeof(famous) / sizeof(famous[0]);
                break;
            case 4:
                words = places;
                hints = placesHints;
                wc = sizeof(places) / sizeof(places[0]);
                break;
            case 5:
                words = people;
                hints = peopleHints;
                wc = sizeof(people) / sizeof(people[0]);
                break;
            default:
                printf("Invalid choice!\n");
                return 1;
        }


        srand(time(0));
        int RI = rand() % wc;
        char *sw = words[RI];
        char *hint = hints[RI];
        int wl = strlen(sw);


        int guessed[wl];
        for (int i = 0; i < wl; i++) {
            guessed[i] = 0;
        }

        int left = max_attempts;
        char guess;

        printf("\nStarting the Hangman Game!\n");

        while (left > 0 && !wordG(guessed, wl)) {
            printf("\nWord: ");
            display(sw, guessed);
            printf("\nAttempts left: %d", left);
            draw(left);

            if (left == 3) {
                printf("\nHint: %s", hint);
            }

            printf("\nGuess a letter: ");
            scanf(" %c", &guess);

            int found = 0;
            for (int i = 0; i < wl; i++) {
                if (tolower(sw[i]) == tolower(guess) && !guessed[i]) {
                    guessed[i] = 1;
                    found = 1;
                }
            }

            if (!found) {
                left--;
                printf("Incorrect guess!\n");
            } else {
                printf("Good guess!\n");
            }
        }

        if (wordG(guessed, wl)) {
            printf("\nCongratulations! You guessed the word: %s\n", sw);
        } else {
            printf("\nOut of attempts! The word was: %s\n", sw);
            draw(0);
        }
        char response;
        printf("\nDo you want to play again? (y/n): ");
        scanf(" %c", &response);
        if (tolower(response) != 'y') {
            playagain = 0;
            printf("Thank you for playing Hangman!\n");
        }
    }
    return 0;
}

void display(char word[], int guessed[]) {
    for (int i = 0; i < strlen(word); i++) {
        if (guessed[i]) {
            printf("%c", word[i]);
        } else {
            printf("_");
        }
        printf(" ");
    }
}

int wordG(int guessed[], int length) {
    for (int i = 0; i < length; i++) {
        if (!guessed[i]) {
            return 0;
        }
    }
    return 1;
}

void draw(int left) {
    printf("\n");
    printf(" _ _ _ _ _ _ _\n");
    printf("|      |\n");
    printf("|      %s\n", (left <= 8) ? "|" : "");
    printf("|      %s\n", (left <= 7) ? "O" : "");
    printf("|     %s%s%s\n", (left <= 6) ? "/" : " ", (left <= 5) ? "|" : " ", (left <= 4) ? "\\" : " ");
    printf("|      %s\n", (left <= 3) ? "|" : " ");
    printf("|     %s %s\n", (left <= 2) ? "/" : " ", (left <= 1) ? "\\" : " ");
    printf("|\n");
}