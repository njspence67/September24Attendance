import random
import time

# ANSI Escape Codes for coloring the output (Red)
RED = '\033[91m'
RESET = '\033[0m'

def generate_powerball_numbers():
    """
    Generates and prints a set of Powerball numbers with a delay and
    colors the final Powerball number red.
    """

    # 1. Greeting and storing the user's name
    print("👋 Welcome to the Powerball Number Generator!")
    varUserName = input("What's your name? ")

    # 2. Greet the user by name
    print(f"\nHello, {varUserName}! Here are your lucky Powerball numbers:")
    print("----------------------------------------------------------")

    # 3. Generate random numbers
    white_ball_1 = random.randint(1, 69)
    white_ball_2 = random.randint(1, 69)
    white_ball_3 = random.randint(1, 69)
    white_ball_4 = random.randint(1, 69)
    white_ball_5 = random.randint(1, 69)
    powerball = random.randint(1, 26)

    # 4. Timer Feature: Introduce a 0.25 second delay
    print("Generating numbers...")
    time.sleep(0.25)  # Pause the execution for 0.25 seconds

    # 5. Print the generated numbers with specific spacing and color
    # Required spacing: [N1]  [N2]  [N3]  [N4]  [N5]    [N6 in Red]

    # Use the ANSI RED code before the last number and RESET after it
    output_string = (
        f"{white_ball_1}  "
        f"{white_ball_2}  "
        f"{white_ball_3}  "
        f"{white_ball_4}  "
        f"{white_ball_5}    "
        f"{RED}{powerball}{RESET}"  # The Powerball is now red
    )

    print(output_string)
    print("----------------------------------------------------------")

    # 6. Farewell message
    print("\nGood luck with your ticket! May the odds be ever in your favor. 🍀")
    print(f"Thanks for using the generator, {varUserName}! Goodbye!")

# Execute the function
generate_powerball_numbers()