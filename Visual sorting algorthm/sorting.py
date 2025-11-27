
import tkinter as tk
from tkinter import ttk
import random


class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")

        self.data = []
        self.sorting = False
        self.sort_generator = None

        # ----- UI Layout -----
        control_frame = tk.Frame(root, padx=10, pady=10)
        control_frame.pack(fill="x")

        # Algorithm selection
        tk.Label(control_frame, text="Algorithm:").pack(side="left")
        self.algorithm_var = tk.StringVar(value="Bubble Sort")
        algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort"]
        algo_menu = ttk.Combobox(
            control_frame,
            textvariable=self.algorithm_var,
            values=algorithms,
            state="readonly",
            width=15,
        )
        algo_menu.pack(side="left", padx=5)

        # Size slider
        tk.Label(control_frame, text="Size:").pack(side="left", padx=(10, 0))
        self.size_scale = tk.Scale(
            control_frame, from_=10, to=100, orient="horizontal", length=150
        )
        self.size_scale.set(30)
        self.size_scale.pack(side="left", padx=5)

        # Speed slider
        tk.Label(control_frame, text="Speed:").pack(side="left", padx=(10, 0))
        self.speed_scale = tk.Scale(
            control_frame, from_=1, to=100, orient="horizontal", length=150
        )
        self.speed_scale.set(50)
        self.speed_scale.pack(side="left", padx=5)

        # Buttons
        generate_button = tk.Button(
            control_frame, text="Generate", command=self.generate_data
        )
        generate_button.pack(side="left", padx=(10, 5))

        start_button = tk.Button(
            control_frame, text="Start", command=self.start_sort
        )
        start_button.pack(side="left")

        # Canvas for drawing
        self.canvas = tk.Canvas(root, bg="white", height=400)
        self.canvas.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # Map names to algorithm functions
        self.algorithms = {
            "Bubble Sort": self.bubble_sort,
            "Selection Sort": self.selection_sort,
            "Insertion Sort": self.insertion_sort,
        }

        # Generate initial data
        self.generate_data()

    # ----- Data generation and drawing -----

    def generate_data(self):
        if self.sorting:
            return  # ignore while sorting

        size = self.size_scale.get()
        self.data = [random.randint(10, 100) for _ in range(size)]
        self.draw_data()

    def draw_data(self, color_positions=None):
        if color_positions is None:
            color_positions = {}

        self.canvas.delete("all")
        if not self.data:
            return

        c_width = self.canvas.winfo_width()
        c_height = self.canvas.winfo_height()

        n = len(self.data)
        bar_width = c_width / n
        max_value = max(self.data)

        for i, value in enumerate(self.data):
            # Normalize height
            x0 = i * bar_width
            x1 = (i + 1) * bar_width
            # 10 px margin at top and bottom
            y1 = c_height - 10
            bar_height = (value / max_value) * (c_height - 20)
            y0 = y1 - bar_height

            color = color_positions.get(i, "#4a90e2")  # default blue
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")

        self.root.update_idletasks()

    # ----- Sorting control -----

    def start_sort(self):
        if self.sorting or not self.data:
            return

        algo_name = self.algorithm_var.get()
        algo_func = self.algorithms.get(algo_name)
        if not algo_func:
            return

        self.sorting = True
        self.sort_generator = algo_func(self.data)
        self.animate()

    def animate(self):
        try:
            # Get next step from generator
            data, color_positions = next(self.sort_generator)
            self.data = data
            self.draw_data(color_positions)
            # Convert speed to delay (ms): higher slider -> faster (smaller delay)
            speed = self.speed_scale.get()
            delay = max(1, int(1000 / speed))
            self.root.after(delay, self.animate)
        except StopIteration:
            # Sorting finished
            self.sorting = False
            # Final draw with all bars in one color
            self.draw_data()

    # ----- Sorting algorithms (generators) -----

    def bubble_sort(self, data):
        a = data
        n = len(a)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                # Highlight compared items
                color_positions = {j: "red", j + 1: "orange"}
                yield a, color_positions
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    # Show after swap
                    yield a, color_positions
        yield a, {}

    def selection_sort(self, data):
        a = data
        n = len(a)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                color_positions = {i: "green", j: "red", min_idx: "orange"}
                yield a, color_positions
                if a[j] < a[min_idx]:
                    min_idx = j
                    color_positions = {i: "green", j: "orange"}
                    yield a, color_positions
            a[i], a[min_idx] = a[min_idx], a[i]
            color_positions = {i: "green", min_idx: "orange"}
            yield a, color_positions
        yield a, {}

    def insertion_sort(self, data):
        a = data
        n = len(a)
        for i in range(1, n):
            key = a[i]
            j = i - 1
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                color_positions = {j: "red", j + 1: "orange", i: "green"}
                yield a, color_positions
                j -= 1
            a[j + 1] = key
            color_positions = {j + 1: "green", i: "green"}
            yield a, color_positions
        yield a, {}


if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
