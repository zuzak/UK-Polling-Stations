from django.contrib.gis.geos import Point
from data_collection.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "E08000029"
    addresses_name = "parl.2019-12-12/Version 1/Democracy_Club__12December2019.CSV"
    stations_name = "parl.2019-12-12/Version 1/Democracy_Club__12December2019.CSV"
    elections = ["europarl.2019-05-23"]
    allow_station_point_from_postcode = False

    def station_record_to_dict(self, record):

        # 3x station changes for EU Parl elections
        if record.polling_place_id == "6775":
            record = record._replace(polling_place_name="Hampton in Arden Library")
            record = record._replace(polling_place_address_1="39 Fentham Road")
            record = record._replace(polling_place_address_2="Hampton in Arden")
            record = record._replace(polling_place_address_3="")
            record = record._replace(polling_place_address_4="")
            record = record._replace(polling_place_postcode="B92 0AY")
            record = record._replace(polling_place_easting="0")
            record = record._replace(polling_place_northing="0")
            record = record._replace(polling_place_uprn="200003829766")

        if record.polling_place_id == "7075":
            record = record._replace(
                polling_place_name="Monkspath Junior and Infant School"
            )
            record = record._replace(polling_place_address_1="Farmhouse Way")
            record = record._replace(polling_place_address_2="")
            record = record._replace(polling_place_address_3="")
            record = record._replace(polling_place_address_4="")
            record = record._replace(polling_place_postcode="B90 4EH")
            record = record._replace(polling_place_easting="0")
            record = record._replace(polling_place_northing="0")
            record = record._replace(polling_place_uprn="100071489020")

        if record.polling_place_id == "7049":
            record = record._replace(polling_place_name="Sharmans Cross Junior School")
            record = record._replace(polling_place_address_1="Sharmans Cross Road")
            record = record._replace(polling_place_address_2="")
            record = record._replace(polling_place_address_3="")
            record = record._replace(polling_place_address_4="")
            record = record._replace(polling_place_postcode="B91 1PH")
            record = record._replace(polling_place_easting="0")
            record = record._replace(polling_place_northing="0")
            record = record._replace(polling_place_uprn="100071401403")

        # The Loft Above Asda
        if record.polling_place_id == "6826":
            record = record._replace(polling_place_uprn="010023647341")

        # Tudor Grange Leisure Centre
        if record.polling_place_id == "7027":
            rec = super().station_record_to_dict(record)
            rec["location"] = Point(-1.7881577, 52.4124167, srid=4326)
            return rec

        # Three Trees Community Centre
        if record.polling_place_id == "6824":
            record = record._replace(polling_place_uprn="100071461342")

        # Elmwood Place
        if record.polling_place_id in ["7041", "7011"]:
            record = record._replace(polling_place_uprn="10090946409")

        # Auckland Hall
        if record.polling_place_id == "7004":
            record = record._replace(polling_place_uprn="200003829755")

        # Dorridge Methodist Church
        if record.polling_place_id == "7081":
            record = record._replace(polling_place_uprn="100071001475")

        # Catherine de Barnes Village Hall
        if record.polling_place_id == "6777":
            rec = super().station_record_to_dict(record)
            rec["location"] = Point(-1.7382134, 52.4203089, srid=4326)
            return rec

        return super().station_record_to_dict(record)

    def address_record_to_dict(self, record):
        rec = super().address_record_to_dict(record)
        uprn = record.property_urn.strip().lstrip("0")

        if uprn == "10090949380":
            rec["postcode"] = "B93 0FH"

        if (record.addressline1, record.addressline2) == (
            "101 Noble Way",
            "Cheswick Green",
        ):
            rec["uprn"] = "10090950327"
            rec["accept_suggestion"] = True

        if uprn in [
            "10090945527",  # B377RN -> B376RL : 3C Woodlands Way, Chelmsley Wood
            "10090945525",  # B377RN -> B376RL : 3A Woodlands Way, Chelmsley Wood
        ]:
            rec["accept_suggestion"] = True

        if record.addressline6 in [
            "B90 4AY",  # stray odd-looking property
            "CV7 7HL",  # single property with spurious-looking station
        ]:
            return None

        if uprn in [
            "100071001341",  # B911DA -> B911JW : 90 Grange Road, Solihull
            "10090946742",  # B901FT -> B930EJ : Apartment 16, Leasowes House, 3 Main Street, Dickens Heath, Solihull
            "10090948318",  # B901GL -> B913AB : Apartment 5, Market Court, 61 Old Dickens Heath Road, Shirley, Solihull
            "10090947804",  # CV49BN -> B901FT : 12 Eagle Drive, Solihull
            "200003834455",  # B927AW -> B927AH : St Michaels Residential Home, 251 Warwick Road, Solihull
            "10090946771",  # B920JP -> B930FD : Caravan Firs Farm, Barston Lane, Solihull
            "10090948319",  # B912AW -> B913AB : Flat 2, 58 Lode Lane, Solihull
            "100070965323",  # B376ES -> B376EU : 77 Overgreen Drive, Kingshurst
            "100070965320",  # B376ES -> B376EU : 77A Overgreen Drive, Kingshurst
            "100070965321",  # B376ES -> B376EU : 77B Overgreen Drive, Kingshurst
            "100070965322",  # B376ES -> B376EU : 77C Overgreen Drive, Kingshurst
        ]:
            rec["accept_suggestion"] = False

        return rec
