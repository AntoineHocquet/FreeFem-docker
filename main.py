# main.py
import argparse
from src.simulate import run_simulation
from src.visualize import generate_visualizations

def main():
    parser = argparse.ArgumentParser(description="FreeFEM Simulation Pipeline")
    parser.add_argument(
        "--run", choices=["sim", "viz", "all"], default="all",
        help="Choose whether to run the simulation, visualization, or both"
    )
    args = parser.parse_args()

    if args.run in ["sim", "all"]:
        print("Running simulation...")
        run_simulation()

    if args.run in ["viz", "all"]:
        print("Generating visualization...")
        generate_visualizations()

if __name__ == "__main__":
    main()
