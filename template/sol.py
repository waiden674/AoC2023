import argparse

class Solution:
    def __init__(self, file_path) -> None:
        self.lines = None
        with open(file_path, "r") as f:
            self.lines = f.readlines
    
    def solve():
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str)
    args = parser.parse_args()
    solution = Solution(args.file_path)
    solution.solve()

