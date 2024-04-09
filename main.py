import pandas as pd

from util.util import get_arguments, colored_print


class ProcessingUnity:
    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path
        self.data = pd.read_csv(input_path)

    def process_data_mean_to_output(self):
        """
        Process the data and calculate the mean and standard deviation of the data
        :return: None
        """
        colored_print("Running 'process_data_mean_to_output' action", "yellow")

        # identify machines
        data = []
        # TODO: generalize the columns
        columns = ["volt", "rotate", "pressure", "vibration"]
        # iterate over the data and identify the machines, then calculate the mean and standard deviation
        for machine in self.data['machineID'].unique():
            machine_row = [machine]  # save the machine ID
            for column in columns:
                machine_row.append(self.data[self.data['machineID'] == machine][column].mean())
                machine_row.append(self.data[self.data['machineID'] == machine][column].std())
            data.append(machine_row)

        result_data = pd.DataFrame(data, columns=["machine"] + [f"{name}_{metric}" for name in columns for metric in
                                                                ["mean", "std"]])
        result_data.to_csv(self.output_path, index=False)
        colored_print("Done with 'process_data_mean_to_output' action", "yellow")


if __name__ == '__main__':
    arguments = get_arguments()
    colored_print(arguments, "green")
    processing_unity = ProcessingUnity(arguments['input'], arguments['output'])

    match arguments['action']:
        case 'mean':
            processing_unity.process_data_mean_to_output()
        case _:  # default
            colored_print("Action not recognized", "red")

    colored_print("Data completely processed", "green")
