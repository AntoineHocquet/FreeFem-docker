# main.py
import argparse
from src.simulate import run_simulation
from src.visualize import generate_visualizations
from src.visualize_gif import generate_gif


def main():
    parser = argparse.ArgumentParser(description="FreeFEM Simulation Pipeline")
    parser.add_argument(
        "--run", choices=["sim", "viz", "gif", "all"], default="all",
        help="Choose whether to run the simulation, visualization, gif, or all"
    )
    args = parser.parse_args()

    if args.run in ["sim", "all"]:
        print("Running simulation...")
        run_simulation()

    if args.run in ["viz", "all"]:
        print("Generating visualization...")
        generate_visualizations()

    if args.run in ["gif", "all"]:
        generate_gif()

if __name__ == "__main__":
    main()
