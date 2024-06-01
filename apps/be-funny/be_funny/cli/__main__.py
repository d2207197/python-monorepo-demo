import click

from be_funny import dataset


@click.group()
def main():
    print("cli:main")


@main.command()
@click.option("--target-folder", "-t", required=False, type=str, help="Target folder")
def load_data_to_hdfs(target_folder: str = None):
    click.echo("cli:load_data_to_hdfs")
    dataset.load_data_to_hdfs(target_folder=target_folder)

@main.command()
@click.option("--source-data-folder", "-s", required=False, type=str, help="Source data folder")
@click.option("--dataset-target-folder", "-t", required=False, type=str, help="Dataset target folder")
def create_dataset(source_data_folder: str = None, dataset_target_folder: str = None):
    click.echo("cli:create_dataset")
    dataset.create_dataset(source_data_folder=source_data_folder, dataset_target_folder=dataset_target_folder)


if __name__ == "__main__":
    main()