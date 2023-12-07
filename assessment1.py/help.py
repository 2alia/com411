
class UserInteraction:
    def get_user_input(self):
        user_name = input("Please enter your name: ")
        return user_name

# Usage
interaction = UserInteraction()
name = interaction.get_user_input()
print(f"Hello, {name}!")

