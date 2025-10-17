from src.process_and_segment_data import DataProcessor
from src.generate_charts import ChartGenerator
from src.strategic_analysis import StrategicAnalyzer
import os
import glob

def find_latest_file(path, pattern):
    """
    Finds the latest file in a directory matching a pattern.
    """
    files = glob.glob(os.path.join(path, pattern))
    if not files:
        return None
    latest_file = max(files, key=os.path.getctime)
    return latest_file

def main():
    """
    Main function to run the analysis pipeline.
    """
    # Find the latest xlsx file in the assets directory
    input_file = find_latest_file('assets', '*.xlsx')

    if not input_file:
        print("No .xlsx file found in the assets directory.")
        return

    # 1. Process and segment the data
    data_processor = DataProcessor(
        input_file=input_file,
        output_dir='docs'
    )
    data_processor.process()

    # 2. Generate charts
    chart_generator = ChartGenerator(
        analysis_file='docs/analysis_by_profile.txt',
        plots_dir='plots'
    )
    chart_generator.generate()

    # 3. Perform strategic analysis
    strategic_analyzer = StrategicAnalyzer(
        analysis_file='docs/analysis_by_profile.txt',
        output_dir='docs'
    )
    strategic_analyzer.analyze()

if __name__ == "__main__":
    main()