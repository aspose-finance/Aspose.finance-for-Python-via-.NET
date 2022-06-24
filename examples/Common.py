import pathlib

base_dir = pathlib.Path(__file__).parent.parent.absolute()
output_path = base_dir.joinpath("output")
data_path = base_dir.joinpath("data")


def get_output_path(fileName):
    if not output_path.exists():
        output_path.mkdir()
    return str(output_path.joinpath(fileName))

def get_data_path(fileName):
    if not data_path.exists():
        data_path.mkdir()
    return str(data_path.joinpath(fileName))
