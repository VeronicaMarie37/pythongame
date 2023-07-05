money = 0
tools = ["teeth"]
available_tools = ["scissors", "push lawnmower", "battery-powered lawnmower", "team of starving students"]
tool_count = 1  # Counter variable to track the number of tools acquired
prices = {
    "scissors": 5,
    "push lawnmower": 25,
    "battery-powered lawnmower": 250,
    "team of starving students": 500
}

earnings = {
    "teeth": 1,
    "scissors": 5,
    "push lawnmower": 50,
    "battery-powered lawnmower": 100,
    "team of starving students": 250
}

current_tool = "teeth"

def print_status():
    print("Current money: $" + str(money))
    print("Current tool: " + current_tool.capitalize())
    print("Owned tools:")
    for tool in tools:
        print(tool.capitalize())
    print("Available tools to buy:")
    for tool in available_tools:
        print(tool.capitalize() + ": $" + str(prices[tool]))
    print()

def buy_tool(tool):
    global money, current_tool, tool_count
    if tool not in prices:
        print("Invalid tool!")
        return
    if tool in tools:
        print("You already own that tool!")
        return
    if money >= prices[tool]:
        money -= prices[tool]
        tools.append(tool)
        available_tools.remove(tool)
        tool_count += 1
        print("You bought a " + tool + "!")
        print_status()
        check_win_condition()
    else:
        print("Not enough money to buy that tool!")

def switch_tool(tool):
    global current_tool
    if tool not in tools:
        print("You don't own that tool!")
        return
    current_tool = tool
    print("You switched to " + current_tool.capitalize() + "!")

def cut_grass():
    global money
    earnings_today = earnings[current_tool]
    money += earnings_today
    print("You earned $" + str(earnings_today) + " today!")
    print_status()

def check_win_condition():
    if tool_count == 4 and money >= 1000:
        print("Congratulations! You have won the game!")
        print("You own all the tools and have reached $1000 or more!")
        print("Thanks for playing!")
        exit()

def game_loop():
    while True:
        command = input("Enter a command (buy/switch/cut/status/quit): ").lower()
        if command == "quit":
            print("Thanks for playing!")
            break
        elif command == "buy":
            tool = input("Enter the name of the tool you want to buy: ").lower()
            buy_tool(tool)
        elif command == "switch":
            tool = input("Enter the name of the tool you want to switch to: ").lower()
            switch_tool(tool)
        elif command == "cut":
            cut_grass()
        elif command == "status":
            print_status()
        else:
            print("Invalid command!")

# Start the game
print("Welcome to Landscaper!")
print("You start with only your teeth. Use them to cut lawns and earn money.")
print("Buy new tools to cut more efficiently and earn more!")
game_loop()
