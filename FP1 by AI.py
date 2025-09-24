import random

def generate_powerball_numbers():
    """
    Generates and prints a set of Powerball numbers based on the game's rules,
    including greeting the user and specific output formatting.
    """

    # 1. Greeting and storing the user's name
    print("👋 Welcome to the Powerball Number Generator!")
    varUserName = input("What's your name? ")

    # 2. Greet the user by name
    print(f"\nHello, {varUserName}! Here are your lucky Powerball numbers:")
    print("----------------------------------------------------------")

    # 3. Generate random numbers for the white balls (1-69)
    # Storing each number in a separate variable as requested

    # Generate the first five numbers (white balls: 1-69)
    white_ball_1 = random.randint(1, 69)
    white_ball_2 = random.randint(1, 69)
    white_ball_3 = random.randint(1, 69)
    white_ball_4 = random.randint(1, 69)
    white_ball_5 = random.randint(1, 69)

    # Generate the sixth number (red Powerball: 1-26)
    powerball = random.randint(1, 26)

    # 4. Print the generated numbers with specific spacing
    # Two spaces between the first five, four spaces between the fifth and sixth
    
    # We use f-strings to convert the numbers to strings and control the spacing.
    # The '.>2' or similar formatting ensures numbers take up at least two characters
    # if you had numbers 1-9 to maintain alignment, but simple conversion is sufficient
    # for the required space characters.
    
    # Required spacing: [N1]  [N2]  [N3]  [N4]  [N5]    [N6]
    
    output_string = (
        f"{white_ball_1}  "
        f"{white_ball_2}  "
        f"{white_ball_3}  "
        f"{white_ball_4}  "
        f"{white_ball_5}    "
        f"{powerball}"
    )

    print(output_string)
    print("----------------------------------------------------------")

    # 5. Farewell message
    print("\nGood luck with your ticket! May the odds be ever in your favor. 🍀")
    print(f"Thanks for using the generator, {varUserName}! Goodbye!")

# Execute the function
generate_powerball_numbers()