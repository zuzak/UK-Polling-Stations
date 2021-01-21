from data_importers.management.commands import BaseXpressDemocracyClubCsvImporter
from pathlib import Path


def make_base_folder_path():
    base_folder_path = Path.cwd() / Path("test_data/pollingstations_data/TEI")
    return str(base_folder_path)


class Command(BaseXpressDemocracyClubCsvImporter):
    local_files = True
    base_folder_path = make_base_folder_path()
    council_id = "E07000045"
    addresses_name = "Democracy_Club__12December2019tein.csv"
    stations_name = "Democracy_Club__12December2019tein.csv"
