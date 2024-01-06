from tui import TUI


class Disneyland:
    def __init__(self):
        self.file_path = "disneyland_reviews.csv"

    def line_dashes(self, title, chr):
        dash_line = chr * len(title)
        print(dash_line)
        print(title)
        print(dash_line)



    def run(self):
        title = "Disneyland review Analyser"
        self.line_dashes(title, "-")
        tui = TUI()
        tui.menu()


if __name__ == "__main__":
    main = Disneyland()
    main.run()
